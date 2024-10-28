# utils/password_reset.py
import subprocess
import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(characters) for _ in range(length))

def reset_password(email):
    new_password = generate_password()
    powershell_script = f"""
    $username = '{email}'
    $newPassword = '{new_password}'
    Import-Module ActiveDirectory
    Set-ADAccountPassword -Identity $username -Reset -NewPassword (ConvertTo-SecureString -AsPlainText $newPassword -Force)
    """
    try:
        # Using `pwsh` for Linux compatibility
        subprocess.run(["pwsh", "-Command", powershell_script], check=True)
        return new_password
    except subprocess.CalledProcessError as e:
        print("Failed to reset password:", e)
        return None
