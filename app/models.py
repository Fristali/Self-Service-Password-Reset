import sqlite3
import os
from datetime import datetime, timedelta

LOCKOUT_DB = os.path.join(os.path.dirname(__file__), '../infra/lockout.sqlite3')

def get_db():
    conn = sqlite3.connect(LOCKOUT_DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS lockouts (
            username TEXT PRIMARY KEY,
            attempts INTEGER,
            locked_until TEXT
        )
    ''')
    conn.commit()
    conn.close()

def record_attempt(username, success):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT attempts, locked_until FROM lockouts WHERE username=?', (username,))
    row = c.fetchone()
    now = datetime.utcnow()
    if row:
        attempts = row['attempts']
        locked_until = row['locked_until']
        if locked_until and now < datetime.fromisoformat(locked_until):
            conn.close()
            return False  # Still locked
        if success:
            c.execute('DELETE FROM lockouts WHERE username=?', (username,))
        else:
            attempts += 1
            if attempts >= 3:
                locked_until = (now + timedelta(minutes=15)).isoformat()
                c.execute('UPDATE lockouts SET attempts=?, locked_until=? WHERE username=?', (attempts, locked_until, username))
            else:
                c.execute('UPDATE lockouts SET attempts=?, locked_until=NULL WHERE username=?', (attempts, username))
    else:
        if not success:
            c.execute('INSERT INTO lockouts (username, attempts, locked_until) VALUES (?, ?, NULL)', (username, 1))
    conn.commit()
    conn.close()
    return True

def is_locked(username):
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT locked_until FROM lockouts WHERE username=?', (username,))
    row = c.fetchone()
    conn.close()
    if row and row['locked_until']:
        return datetime.utcnow() < datetime.fromisoformat(row['locked_until'])
    return False
