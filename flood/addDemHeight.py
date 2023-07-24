from osgeo import gdal

# 读取center1.txt文件并处理数据
with open('clearcenter1.txt', 'r') as center1_file:
    lines = center1_file.readlines()

output_lines = []

# 使用GDAL库读取DEM数据
dem_file = '5.tif'
dataset = gdal.Open(dem_file)

if dataset is not None:
    for line in lines:
        # 解析每一行经度（x）与纬度（y）
        longitude, latitude, height = line.strip().split(',')
        x, y,z = float(longitude), float(latitude),float(height)

        # 根据经度（x）与纬度（y）获取高度
        band = dataset.GetRasterBand(1)
        cols = dataset.RasterXSize
        rows = dataset.RasterYSize
        transform = dataset.GetGeoTransform()
        x_index = int((x - transform[0]) / transform[1])
        y_index = int((y - transform[3]) / transform[5])
        Demheight = band.ReadAsArray(x_index, y_index, 1, 1)[0][0]

        # 将高度信息与经度（x）和纬度（y）拼接为新的一行
        output_line = f"{longitude},{latitude},{height},{Demheight}\n"
        output_lines.append(output_line)

    # 将处理后的数据保存为center1H.txt文件
    with open('clearcenter1dem.txt', 'w') as output_file:
        output_file.writelines(output_lines)

    print("高度数据已保存到clearcenter1dem.txt文件中。")
else:
    print("无法打开DEM文件。")
