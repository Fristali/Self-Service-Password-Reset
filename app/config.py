import os

# To enable real AD resets, configure the app to call 'real_ad_reset_password.ps1' on your domain-joined Windows server.
# By default, mock/demo scripts are used for safe local testing.

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SECURITY_QUESTIONS = [
        "What is your mother's maiden name?",
        "What was the name of your first pet?",
        "What is your favorite color?"
    ]
    USERS_CSV = os.path.join(os.path.dirname(__file__), '../infra/users.csv')
    LOCKOUT_DB = os.path.join(os.path.dirname(__file__), '../infra/lockout.sqlite3')
    LOG_DIR = os.path.join(os.path.dirname(__file__), '../elk/sample_logs/')
    SERVICE_ACCOUNT = 'svc-pwdreset'
    DOMAIN = 'company.local'
    PASSWORD_POLICY = {
        'min_length': 8,
        'upper': 1,
        'lower': 1,
        'number': 1,
        'special': 1
    }
    MAX_ATTEMPTS = 3
    LOCKOUT_MINUTES = 15
