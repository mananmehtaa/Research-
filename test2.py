import open3d as o3d
import numpy as np
import os

# Ensure output folder exists
output_folder = "simulated_lidar_dataset"
os.makedirs(output_folder, exist_ok=True)

def generate_pose(label):
    if label == "sitting":
        return np.random.normal(loc=[0, 0, 0.6], scale=0.2, size=(600, 3))
    elif label == "walking_gait":
        leg1 = np.random.normal(loc=[-0.2, 0, 0.5], scale=0.05, size=(200, 3))
        leg2 = np.random.normal(loc=[0.2, 0, 0.5], scale=0.05, size=(200, 3))
        torso = np.random.normal(loc=[0, 0, 1.4], scale=0.15, size=(300, 3))
        return np.vstack((leg1, leg2, torso))
    elif label == "room_activity":
        return np.random.normal(loc=[0, 0, 1.2], scale=1.0, size=(1000, 3))
    elif label == "bed_exit":
        body = np.random.normal(loc=[0, 0, 0.4], scale=0.1, size=(400, 3))
        head = np.random.normal(loc=[0.3, 0, 0.8], scale=0.1, size=(100, 3))
        return np.vstack((body, head))
    else:
        return np.random.rand(500, 3)

def save_pcd(points, filename):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.io.write_point_cloud(filename, pcd)

# Generate 10 samples for each category
labels = ["sitting", "walking_gait", "room_activity", "bed_exit"]
for label in labels:
    for i in range(10):
        pts = generate_pose(label)
        save_pcd(pts, os.path.join(output_folder, f"{label}_{i:03}.pcd"))

print("✅ Dataset created in folder: simulated_lidar_dataset")
