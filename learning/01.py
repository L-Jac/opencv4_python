# 第二章
import cv2 as cv
# TODO
# numpy对图像的切割分离
#   chapter2/Numpy_Operations.py

# NumPy在对图像进行通道分离时表现良好
#   numpy将BGR图像转为RGB图像以及使用切片和索引时间
#   快于opencv的函数(cv.cvtColor(),cv.split())
#   chapter2/Compare_opencv_numpy.py

# 窗口函数
thewindow = cv.nameWindow("windowname", [cv.WINDOW_AUTOSIZE | cv.WINDOW_KEEPRATIO | cv.WINDOW_GUI_EXPANDED])
