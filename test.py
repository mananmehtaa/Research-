import open3d as o3d
import numpy as np

def generate_body_posture(label):
    if label == "stand":
        # Tall vertical point cloud (like a person standing)
        points = np.random.normal(loc=[0, 0, 1.5], scale=0.2, size=(500, 3))
    elif label == "fall":
        # Horizontal spread point cloud (like someone fallen)
        points = np.random.normal(loc=[0, 0, 0.2], scale=0.2, size=(500, 3))
    else:
        points = np.random.rand(500, 3)
    return points

def save_pcd(points, filename):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    o3d.io.write_point_cloud(filename, pcd)

# Simulate 10 samples each
for i in range(10):
    points = generate_body_posture("stand")
    save_pcd(points, f"simulated_stand_{i:03}.pcd")

for i in range(10):
    points = generate_body_posture("fall")
    save_pcd(points, f"simulated_fall_{i:03}.pcd")

print("✅ Simulated dataset generated.")
