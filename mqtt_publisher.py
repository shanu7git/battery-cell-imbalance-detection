import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

load_dotenv()

BROKER = os.getenv("HIVEMQ_BROKER")
PORT = int(os.getenv("HIVEMQ_PORT", 8883))
USERNAME = os.getenv("Logan X")
PASSWORD = os.getenv("Bangalore2025")

TOPIC = "battery/cells"