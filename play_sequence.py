import open3d as o3d
import os
import time

# Set your folder containing all frames
folder = "simulated_lidar_dataset"

# Get all .pcd files, sorted for playback
pcd_files = sorted([f for f in os.listdir(folder) if f.endswith(".pcd")])

# Open3D visualizer
vis = o3d.visualization.Visualizer()
vis.create_window(window_name="FULL ACTIVITY SEQUENCE", width=800, height=600)

for i, filename in enumerate(pcd_files):
    file_path = os.path.join(folder, filename)
    pcd = o3d.io.read_point_cloud(file_path)

    if i == 0:
        vis.add_geometry(pcd)
    else:
        vis.update_geometry(pcd)

    vis.poll_events()
    vis.update_renderer()
    time.sleep(0.3)  # adjust speed here

vis.destroy_window()
