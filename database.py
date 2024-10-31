import sqlite3

def init_db():
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            first_name TEXT,
            language TEXT,
            phone_number TEXT,
            location TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS buttons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            button_text TEXT,
            button_type TEXT,
            button_action TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_user(user_id, first_name, language):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO users (user_id, first_name, language) VALUES (?, ?, ?)', (user_id, first_name, language))
    conn.commit()
    conn.close()

def save_contact(user_id, phone_number):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET phone_number = ? WHERE user_id = ?', (phone_number, user_id))
    conn.commit()
    conn.close()

def save_location(user_id, location):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET location = ? WHERE user_id = ?', (location, user_id))
    conn.commit()
    conn.close()
