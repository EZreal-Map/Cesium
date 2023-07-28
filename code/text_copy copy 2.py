import laspy

# 读取地理坐标数据
input_file = "../flood/center1.txt"
data = []
with open(input_file, "r") as f:
    for line in f:
        x, y, z = map(float, line.strip().split(','))
        data.append((x, y, z))

# 创建LAS文件
out_las_file = "output_point_cloud.las"
out_las = laspy.create(point_format=1)
out_las.x = [point[0] for point in data]
out_las.y = [point[1] for point in data]
out_las.z = [point[2] for point in data]

# 设置LAS文件头部的缩放因子和偏移量来转换地理坐标（WGS84经纬度）
# WGS84 经度范围为 -180 到 180 度
# WGS84 纬度范围为 -90 到 90 度

# 计算 X（经度）坐标的缩放因子和偏移量
longitude_range = 360.0  # -180 到 180 度
out_las.header.scale[0] = longitude_range / (2 ** 32)  # 假设 X 坐标使用 32 位整数
out_las.header.offset[0] = -180.0

# 计算 Y（纬度）坐标的缩放因子和偏移量
latitude_range = 180.0  # -90 到 90 度
out_las.header.scale[1] = latitude_range / (2 ** 32)  # 假设 Y 坐标使用 32 位整数
out_las.header.offset[1] = -90.0

# 如果需要，还可以计算 Z（高程）坐标的缩放因子和偏移量，方法与上述类似
# 缩放因子的计算可基于实际高程数据的范围

# 写入并保存LAS文件
out_las.write(out_las_file)

print("转换完成！")
