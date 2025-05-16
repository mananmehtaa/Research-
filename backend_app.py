# backend_app.py
from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sqlite3
import time
import random

app = FastAPI()

# Initialize SQLite database
conn = sqlite3.connect("imu_data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS imu_data (
        timestamp REAL,
        id INTEGER,
        qx REAL,
        qy REAL,
        qz REAL,
        qw REAL,
        timedelay INTEGER
    )
""")

# Pydantic model (optional for future use)
class IMUData(BaseModel):
    timestamp: float
    id: int
    qx: float
    qy: float
    qz: float
    qw: float
    timedelay: int

# Simulate IMU messages every 0.5s
def read_serial():
    id = 1
    while True:
        try:
            timestamp = time.time()
            qx = round(random.uniform(-0.001, 0.001), 4)
            qy = round(random.uniform(0.002, 0.003), 4)
            qz = round(random.uniform(-0.27, -0.23), 4)
            qw = round(random.uniform(0.96, 0.97), 4)
            timedelay = random.randint(5000, 6000)

            cursor.execute("INSERT INTO imu_data VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (timestamp, id, qx, qy, qz, qw, timedelay))
            conn.commit()

            id += 1
            time.sleep(0.5)
        except Exception as e:
            print(f"Simulation error: {e}")

# Start simulation thread
threading.Thread(target=read_serial, daemon=True).start()

# API endpoint to return recent IMU data
@app.get("/data")
def get_data():
    cursor.execute("SELECT * FROM imu_data ORDER BY timestamp DESC LIMIT 50")
    return cursor.fetchall()
