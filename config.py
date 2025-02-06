import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'db-project.ceaomtz44zvm.us-east-1.rds.amazonaws.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False