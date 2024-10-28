# app/routes.py
from flask import Blueprint, render_template, request, flash
from .forms import ResetForm
from utils.password_reset import reset_password
from utils.sms_gateway import send_sms
from .auth import basic_auth_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/reset_password', methods=['GET', 'POST'])
@basic_auth_required
def reset_password_route():
    form = ResetForm()
    if form.validate_on_submit():
        email = form.email.data
        new_password = reset_password(email)
        if new_password:
            phone_number = fetch_user_phone(email)
            message = f"Your new password is: {new_password}"
            send_sms(phone_number, message)
            flash('Password reset successfully and sent via SMS.')
        else:
            flash('Error resetting password.', 'danger')
    return render_template('reset_form.html', form=form)
