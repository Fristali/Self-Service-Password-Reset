from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import csv
import os
import json
from datetime import datetime
from .models import init_db, record_attempt, is_locked

bp = Blueprint('main', __name__)

def load_users():
    users = {}
    with open(current_app.config['USERS_CSV'], newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users[row['username']] = row
    return users

def log_attempt(username, status, reason):
    log_dir = current_app.config['LOG_DIR']
    os.makedirs(log_dir, exist_ok=True)
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "username": username,
        "status": status,
        "reason": reason,
        "ip": request.remote_addr
    }
    fname = f"{log_dir}/{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}_{username}.json"
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(log_entry, f)

@bp.before_app_first_request
def setup():
    init_db()

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        users = load_users()
        if username not in users:
            flash('User not found.', 'danger')
            log_attempt(username, 'fail', 'user_not_found')
            return render_template('index.html')
        if is_locked(username):
            flash('Account is locked. Try again later.', 'danger')
            log_attempt(username, 'fail', 'locked')
            return render_template('index.html')
        return redirect(url_for('.security_questions', username=username))
    return render_template('index.html')

@bp.route('/security/<username>', methods=['GET', 'POST'])
def security_questions(username):
    users = load_users()
    if username not in users:
        flash('User not found.', 'danger')
        return redirect(url_for('.index'))
    questions = current_app.config['SECURITY_QUESTIONS']
    if request.method == 'POST':
        answers = [request.form.get(f'q{i}') for i in range(1, 4)]
        if all(answers[i].strip().lower() == users[username][f'q{i+1}'].strip().lower() for i in range(3)):
            return redirect(url_for('.reset_password', username=username))
        else:
            record_attempt(username, False)
            log_attempt(username, 'fail', 'security_answers')
            flash('Incorrect answers.', 'danger')
            return render_template('security.html', username=username, questions=questions)
    return render_template('security.html', username=username, questions=questions)

@bp.route('/reset/<username>', methods=['GET', 'POST'])
def reset_password(username):
    users = load_users()
    if username not in users:
        flash('User not found.', 'danger')
        return redirect(url_for('.index'))
    if is_locked(username):
        flash('Account is locked. Try again later.', 'danger')
        return redirect(url_for('.index'))
    if request.method == 'POST':
        password = request.form['password']
        confirm = request.form['confirm']
        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('reset.html', username=username)
        if not validate_password(password):
            flash('Password does not meet policy.', 'danger')
            return render_template('reset.html', username=username)
        # To enable real AD resets, configure the app to call 'real_ad_reset_password.ps1' on your domain-joined Windows server.
        # By default, mock/demo scripts are used for safe local testing.
        # Simulate PowerShell call
        # In production, call PowerShell script here
        record_attempt(username, True)
        log_attempt(username, 'success', 'reset')
        flash('Password reset successful.', 'success')
        return redirect(url_for('.index'))
    return render_template('reset.html', username=username)

def validate_password(password):
    policy = current_app.config['PASSWORD_POLICY']
    if len(password) < policy['min_length']:
        return False
    if sum(1 for c in password if c.isupper()) < policy['upper']:
        return False
    if sum(1 for c in password if c.islower()) < policy['lower']:
        return False
    if sum(1 for c in password if c.isdigit()) < policy['number']:
        return False
    if sum(1 for c in password if not c.isalnum()) < policy['special']:
        return False
    return True
