import paho.mqtt.client as mqtt
import sqlite3
import json

BROKER = "3c61b0b772e9493ea7da66fbbc85cd63.s1.eu.hivemq.cloud"
PORT = 8883

USERNAME = "Logan X"
PASSWORD = "Bangalore2025"

TOPIC = "battery/cells"

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


def on_connect(client, userdata, flags, rc):

    print("Connected to HiveMQ")

    client.subscribe(TOPIC)

    print("Subscribed to:", TOPIC)


def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    cursor.execute("""
    INSERT INTO battery_data
    (timestamp, cell1, cell2, cell3, cell4,
     temperature, current, soc,
     voltage_difference, status)

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["timestamp"],
        data["cell1"],
        data["cell2"],
        data["cell3"],
        data["cell4"],
        data["temperature"],
        data["current"],
        data["soc"],
        data["voltage_difference"],
        data["status"]
    ))

    conn.commit()

    print("Data stored in SQLite:")
    print(data)


client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()