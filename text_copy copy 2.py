import open3d as o3d

# 读取点云数据
point_cloud = o3d.io.read_point_cloud("../flood/30jiami/17520/XYDpH.las")

# 可视化点云数据
o3d.visualization.draw_geometries([point_cloud])