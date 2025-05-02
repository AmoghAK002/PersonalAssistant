import sqlite3

# Function to get the database connection and cursor
def get_db_connection():
    conn = sqlite3.connect('jarvis.db', check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor

# Export cursor and connection to be used elsewhere
conn, cursor = get_db_connection()

# Create tables (only if they don't exist)
def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sys_command(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            path VARCHAR(1000)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS web_command(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            path VARCHAR(1000)
        )
    """)
    conn.commit()

# Insert websites into the web_command table
def insert_websites():
    websites = [
        ('pinterest', 'https://www.pinterest.com/'),
        ('snapchat', 'https://www.snapchat.com/'),
        ('tiktok', 'https://www.tiktok.com/'),
        ('duckduckgo', 'https://www.duckduckgo.com/'),
        # Add all other websites as needed
    ]
    for name, url in websites:
        cursor.execute("INSERT INTO web_command (name, path) VALUES (?, ?)", (name, url))
    conn.commit()

# Create tables and insert data if not already done
create_tables()
insert_websites()

# Export the cursor and connection explicitly for use in other files
__all__ = ['conn', 'cursor']
