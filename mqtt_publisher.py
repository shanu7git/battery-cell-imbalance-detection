import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

BROKER = "3c61b0b772e9493ea7da66fbbc85cd63.s1.eu.hivemq.cloud"
PORT = 8883

USERNAME = "Logan X"
PASSWORD = "Bangalore2025"

TOPIC = "battery/cells"

client = mqtt.Client()

client.username_pw_set(USERNAME, PASSWORD)

client.tls_set()

print("Connecting to HiveMQ Cloud...")

client.connect(BROKER, PORT)

print("Connected to HiveMQ Cloud!")

while True:

    cell1 = round(random.uniform(3.65, 3.75), 3)
    cell2 = round(random.uniform(3.65, 3.75), 3)
    cell3 = round(random.uniform(3.65, 3.75), 3)
    cell4 = round(random.uniform(3.40, 3.75), 3)

    cells = [cell1, cell2, cell3, cell4]

    max_voltage = max(cells)
    min_voltage = min(cells)

    difference = round(max_voltage - min_voltage, 3)

    if difference > 0.05:
        status = "IMBALANCE"
    else:
        status = "BALANCED"

    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cell1": cell1,
        "cell2": cell2,
        "cell3": cell3,
        "cell4": cell4,
        "temperature": round(random.uniform(25, 40), 2),
        "current": round(random.uniform(1, 10), 2),
        "soc": round(random.uniform(50, 100), 2),
        "voltage_difference": difference,
        "status": status
    }

    message = json.dumps(data)

    client.publish(TOPIC, message)

    print("Data sent:")
    print(message)

    time.sleep(5)