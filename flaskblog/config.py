import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgres://kqqxrgvgdbvlep:929b56ef466794807c974cb616e89c7ee1c1df25a8222678d32b3f8ca780fac8@ec2-52-205-61-230.compute-1.amazonaws.com:5432/dbg91tmdj86m5n'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')