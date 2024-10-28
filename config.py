# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    ADMIN_USER = os.getenv('ADMIN_USER')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    SMS_API_KEY = os.getenv('SMS_API_KEY')
    SMS_GATEWAY_URL = os.getenv('SMS_GATEWAY_URL')
