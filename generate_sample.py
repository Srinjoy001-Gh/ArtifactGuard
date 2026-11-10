import sqlite3
import os

# Create sample_data directory
os.makedirs('sample_data', exist_ok=True)
db_path = 'sample_data/History'

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the urls table (mimicking Chrome's structure)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY,
        url TEXT,
        title TEXT,
        visit_count INTEGER,
        last_visit_time INTEGER
    )
''')

# Insert dummy forensic data (timestamps are in Chrome WebKit microseconds)
dummy_data = [
    ('https://github.com', 'GitHub: Let''s build from here', 42, 13322256000000000),
    ('https://stackoverflow.com', 'Stack Overflow - Where Developers Learn', 15, 13322342400000000),
    ('https://cyberdefenders.org', 'CyberDefenders | Blue Team Training', 7, 13322428800000000),
    ('https://mail.google.com', 'Gmail', 120, 13322515200000000),
    ('http://suspicious-domain.evil', 'Free Downloads', 1, 13322601600000000)
]

cursor.executemany('INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)', dummy_data)
conn.commit()
conn.close()

print("[+] Success! Dummy Chrome History file created safely at 'sample_data/History'")