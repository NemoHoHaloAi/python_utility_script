import cv2
import numpy as np

# 指定每张图片展示的持续时间和视频的帧率
duration = 10  # 每张图片展示的秒数
fps = 1  # 每秒帧数

# 图片文件的路径列表
image_paths = [
    'combined_1.jpg',
    'combined_2.jpg',
    'combined_3.jpg',
]

# 用于将图片转换成视频帧的函数
def convert_image_to_frame(image_path, video_format='mp4v'):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image.shape[2] == 4:  # 如果图片有透明度通道
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    elif image.shape[2] == 1:  # 如果图片是灰度
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    return image

# 存储每张图片尺寸的列表
image_sizes = []

# 读取每张图片的尺寸
for path in image_paths:
    img = convert_image_to_frame(path)
    height, width, layers = img.shape
    image_sizes.append((width, height))

# 确认所有图片有相同的分辨率
max_width = max(size[0] for size in image_sizes)
max_height = max(size[1] for size in image_sizes)

# 定义视频编码和创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 视频编码
video_path = './slideshow.mp4'
video = cv2.VideoWriter(video_path, fourcc, fps, (max_width, max_height))

# 将每张图片添加到视频中
for path in image_paths:
    img = convert_image_to_frame(path)
    img_resized = cv2.resize(img, (max_width, max_height))  # 将图片调整为视频分辨率
    for i in range(fps * duration):
        video.write(img_resized)  # 将图片帧写入视频

# 释放视频写入对象
video.release()

# 视频文件的路径
print(f"Video saved to {video_path}")

