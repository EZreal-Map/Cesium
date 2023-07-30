import numpy as np
import open3d as o3d

# 假设你已经有一个点云points，每个点都有一个对应的颜色colors
# 假设你已经进行了曲面重构，得到了一个mesh
# 生成一个简单的点云数据
points = np.random.rand(1000, 3)  # 1000个随机点
colors = np.random.rand(1000, 3)  # 每个点对应的随机颜色
# 将点云和颜色转换为Open3D格式的PointCloud对象
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# 进行曲面重构，生成mesh
mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd)

# 将颜色信息传递给生成的曲面对象
mesh.vertex_colors = pcd.colors

# 可视化彩色的曲面
o3d.visualization.draw_geometries([mesh])
