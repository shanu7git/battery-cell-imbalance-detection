import paho.mqtt.client as mqtt

BROKER = "3c61b0b772e9493ea7da66fbbc85cd63.s1.eu.hivemq.cloud"
PORT = 8883

USERNAME = "Logan X"
PASSWORD = "Bangalore2025"

TOPIC = "battery/cells"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HiveMQ Cloud!")
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)
    else:
        print("Connection failed:", rc)

def on_message(client, userdata, msg):
    print("\nMessage received:")
    print("Topic:", msg.topic)
    print("Data:", msg.payload.decode())

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to HiveMQ Cloud...")
client.connect(BROKER, PORT)

client.loop_forever()