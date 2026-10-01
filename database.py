import sqlite3

conn = sqlite3.connect("battery.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS battery_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    cell1 REAL,
    cell2 REAL,
    cell3 REAL,
    cell4 REAL,
    temperature REAL,
    current REAL,
    soc REAL,
    voltage_difference REAL,
    status TEXT
)
""")

conn.commit()

print("Database and table created successfully!")

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

print("Tables:", cursor.fetchall())

conn.close()