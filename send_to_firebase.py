import firebase_admin
from firebase_admin import credentials, db
import time

# Step 1: Load credentials
cred = credentials.Certificate("firebase_key.json")

# Step 2: Initialize Firebase app
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-lidar-default-rtdb.asia-southeast1.firebasedatabase.app/'
})


# Step 3: Example data (replace with real predictions)
prediction = {
    "timestamp": time.time(),
    "activity": "bed_exit",   # replace with actual prediction
    "confidence": 0.98        # optional: confidence score
}

# Step 4: Push to Realtime Database
ref = db.reference('/activity_predictions')
ref.push(prediction)

print("Sent to Firebase!")
