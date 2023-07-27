from pyproj import Proj

# 定义两个UTM投影坐标系统
utm114 = Proj("+proj=tmerc +lon_0=114 +y_0=0 +x_0=500000 +ellps=IAU76 \
+towgs84=-8.023502,19.076435,12.698081,0.803741,-1.663943,3.283334,-3.339526 +units=m +no_defs")

utm113 = Proj("+proj=tmerc +lon_0=113.35 +y_0=0 +x_0=500000 +ellps=IAU76 \
+towgs84=-7.849095,18.661172,12.682502,0.809388,-1.667217,-56.719783,-3.30421e-007 +units=m +no_defs")
# 输入待转换的50坐标系中的x、y、z坐标数据（以米为单位）
x = 506087.165667
y = 3510120.516667
z = 123.456
# 将50坐标系中的x、y、z坐标转换为WGS84经纬度
coordX, coordY = utm113(x, y, inverse=True)  # 使用UTM113投影坐标转换
# 以度为单位输出WGS84经纬度坐标\nprint('转换后的WGS84经纬度坐标为：')
print('经度：', coordX)
print('纬度：', coordY)
# print('海拔：', alt)