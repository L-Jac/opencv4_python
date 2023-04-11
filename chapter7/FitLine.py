# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np


if __name__ == '__main__':
    # 生成float32类型的20 * 2 矩阵表示2D点集
    points = np.array([[[0.0, 0.0], [10.0, 11.0], [21.0, 20.0], [30.0, 30.0], [40.0, 42.0],
                       [50.0, 50.0], [60.0, 60.0], [70.0, 70.0], [80.0, 80.0], [90.0, 92.0],
                       [100.0, 100.0], [110, 110.0], [120.0, 120.0], [136.0, 130.0], [138.0, 140.0],
                       [150.0, 150.0], [160.0, 163.0], [175.0, 170.0], [181.0, 180.0], [200.0, 190.0]]],
                      dtype='float32')

    # 设置参数
    param = 0                          # 距离模型中的数值参数C
    reps = 0.01                        # 坐标原点与直线之间的距离精度
    aeps = 0.01                        # 角度精度

    # 进行直线拟合
    line = cv.fitLine(points, cv.DIST_L1, param, reps, aeps)

    k = (line[1] / line[0])[0]
    x = (line[2])[0]
    y = (line[3])[0]
    print('直线斜率为：{}'.format(k))
    print('直线上一点的坐标为：({}，{})'.format(x, y))
    print('拟合直线解析式为：y = {} (x - {}) + {}'.format(k, x, y))
