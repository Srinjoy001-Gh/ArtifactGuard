import sqlite3
from datetime import datetime
import pandas as pd

def convert_chrome_timestamp(micro_secs):
    """Convert Chrome Webkit microsecond timestamp to readable UTC datetime string."""
    if not micro_secs or micro_secs == 0:
        return "N/A"
    try:
        # Chrome epoch starts at Jan 1, 1601
        epoch_start = datetime(1601, 1, 1)
        delta = pd.Timedelta(microseconds=micro_secs)
        actual_time = epoch_start + delta
        return actual_time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return "Invalid Timestamp"

def parse_chrome_history(db_path):
    """Connects to Chrome History SQLite DB and extracts url, title, visit count, and timestamp."""
    try:
        conn = sqlite3.connect(db_path)
        query = """
            SELECT url, title, visit_count, last_visit_time 
            FROM urls
        """
        df = pd.read_sql_query(query, conn)
        conn.close()

        # Convert timestamps
        df['last_visit_time'] = df['last_visit_time'].apply(convert_chrome_timestamp)
        return df
    except Exception as e:
        print(f"[!] Error parsing database: {e}")
        return None