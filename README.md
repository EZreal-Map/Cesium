# Cesium

## 1、洪水数据的预处理

> 拼接每个时刻的经纬度、R(半径)、H(水深)、S(地形高度)
>
> > 其中经纬度、R(半径)，存放在 初始文件的center.txt
>
> > 其中H(水深)、S(地形高度DEM)有多份，每一个时刻都有一份，在每个文件夹里面(如360、420、480、600...)

### 1.1、getLLRHD.py

> 读取初始时刻文件夹里面的center.txt文件、和每个时刻对应的文件夹里面的H、S文件。

在初始时刻文件夹里面生成一个subcontent.txt文件，便于JavaScript获取子目录。（PS:JavaScript不容易获取正在运行子目录）

在每一时刻文件夹里面生成一个LLRHD.txt文件，这些文件是程序主要目的，用于Cesium渲染不同时刻的洪水数据。

> LLRHD.txt每行有5列，从左到右依次是LLRHD（Longitude,Latitude,Radius,Height,DEM）

### 1.2、clearLLRHD.py

> 读取上一步在每一时刻文件夹里面生成的LLRHD.txt文件。

清除H(水深)小于阈值的数据，比如`threshold = 0.01  #阈值`，生成精简后的洪水数据文件clearLLRHD.py

## 2、Cesium进行洪水渲染