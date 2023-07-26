import pyproj

def mercator_to_latlon(x, y):
    # 定义墨卡托投影和经纬度投影
    mercator = pyproj.Proj(init='epsg:3857')
    latlon = pyproj.Proj(init='epsg:4326')
    
    # 坐标转换
    lon, lat = pyproj.transform(mercator, latlon, x, y)
    return lat, lon

# 示例用法
x_mercator = 506087.165667
y_mercator = 3510120.516667
latitude, longitude = mercator_to_latlon(x_mercator, y_mercator)
print("经度:", longitude)
print("纬度:", latitude)
