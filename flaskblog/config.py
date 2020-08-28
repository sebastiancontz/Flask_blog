from dotenv import load_dotenv
import os
load_dotenv()

KEY = os.getenv("SECRET_KEY")
DB_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
EMAIL_SV = os.getenv("MAIL_SERVER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_USER = os.getenv("EMAIL_USER")


class Config:
    SECRET_KEY = KEY
    SQLALCHEMY_DATABASE_URI = DB_URI
    MAIL_SERVER = EMAIL_SV
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = EMAIL_PASS
    MAIL_PASSWORD = EMAIL_PASS
