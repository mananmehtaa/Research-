import open3d as o3d
import numpy as np
import os
import pandas as pd

folder = "simulated_lidar_dataset"  # your dataset folder

data = []

def extract_features(pcd):
    points = np.asarray(pcd.points)
    if len(points) == 0:
        return [0, 0, 0]
    avg_height = np.mean(points[:, 2])
    spread_x = np.std(points[:, 0])
    spread_y = np.std(points[:, 1])
    return [avg_height, spread_x, spread_y]

for filename in sorted(os.listdir(folder)):
    if filename.endswith(".pcd"):
        pcd = o3d.io.read_point_cloud(os.path.join(folder, filename))
        features = extract_features(pcd)

        if "sit" in filename:
            label = "sitting"
        elif "stand" in filename:
            label = "standing"
        elif "walk" in filename:
            label = "walking"
        elif "fall" in filename:
            label = "fall"
        elif "room" in filename:
            label = "room_activity"
        elif "bed" in filename:
            label = "bed_exit"
        else:
            label = "unknown"

        data.append([filename] + features + [label])

df = pd.DataFrame(data, columns=["frame", "avg_height", "spread_x", "spread_y", "label"])
df.to_csv("lidar_activity_dataset.csv", index=False)
print("✅ CSV created: lidar_activity_dataset.csv")
