这是 2019 人工智能基础的一个课程设计项目 “发型推荐软件”，利用人脸的特征点坐标分类脸型，并据此推荐发型。已经初步完成了一个具有**简陋**图形界面的成品。

## 环境要求

+ python 3
+ keras
  + 使用 `pip install keras` 安装
+ PIL
  + 使用 `pip install Pillow` 安装
+ aip
  + 使用 `pip install baidu-aip` 安装

## 使用方法

+ 联网的情况下，在命令行或者 IDE 中运行 hair_style.py
+ 等待一段时间，在弹出图形界面中，点击 “路径选择” 选取一张自己的正脸图片，选择性别 “男” 或 “女”，最后点击 “开始分析” 生成 “脸型分析” 和 “发型推荐”。

## 界面展示

![简单展示](D:\Learn me\USTC\2019春季\2019春 人工智能\Lab\AI2019_lab03\hair_style\简单展示.PNG)