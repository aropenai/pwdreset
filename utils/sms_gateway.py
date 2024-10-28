# utils/sms_gateway.py
import requests
from flask import current_app

def send_sms(phone_number, message):
    url = current_app.config['SMS_GATEWAY_URL']
    payload = {
        "to": phone_number,
        "message": message,
        "api_key": current_app.config['SMS_API_KEY']
    }
    response = requests.post(url, json=payload)
    return response.status_code == 200
