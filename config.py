import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://admin:testtest@db-project.ceaomtz44zvm.us-east-1.rds.amazonaws.com:3306/ecommerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False