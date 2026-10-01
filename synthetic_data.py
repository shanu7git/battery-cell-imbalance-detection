import random
import time
from datetime import datetime

while True:

    cell1 = round(random.uniform(3.65, 3.75), 3)
    cell2 = round(random.uniform(3.65, 3.75), 3)
    cell3 = round(random.uniform(3.65, 3.75), 3)
    cell4 = round(random.uniform(3.40, 3.75), 3)

    temperature = round(random.uniform(25, 40), 2)
    current = round(random.uniform(1, 10), 2)
    soc = round(random.uniform(50, 100), 2)

    cells = [cell1, cell2, cell3, cell4]

    max_voltage = max(cells)
    min_voltage = min(cells)

    difference = round(max_voltage - min_voltage, 3)

    if difference > 0.05:
        status = "IMBALANCE"
    else:
        status = "BALANCED"

    print({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cell1": cell1,
        "cell2": cell2,
        "cell3": cell3,
        "cell4": cell4,
        "temperature": temperature,
        "current": current,
        "soc": soc,
        "voltage_difference": difference,
        "status": status
    })

    time.sleep(5)