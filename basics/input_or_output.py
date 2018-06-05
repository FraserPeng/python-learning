# 输入输出
# 计算圆的面积 πr²=S

import math
print("圆面积 选择 ", 1)
print("圆周长 选择 ", 2)
print("矩形面积 选择 ", 3)
print("矩形周长 选择 ", 4)
choice = int(input("请选择你需要计算的公式"))

if choice == 1:
    r = float(input('请输入圆的半径：'))
    s_circle = math.pi * pow(r, 2)
    print('圆的面积是', s_circle)
elif choice == 2:
    r = float(input('请输入圆的半径：'))
    l_circle = math.pi * 2 * r
    print('圆的面积是', l_circle)
elif choice == 3:
    h = float(input('请输入矩形长：'))
    w = float(input('请输入矩形宽：'))
    s_rect = h * w
    print('矩形的面积是', s_rect)
elif choice == 4:
    h = float(input('请输入矩形长：'))
    w = float(input('请输入矩形宽：'))
    l_rect = 2 * h + 2 * w
    print('矩形的面积是', l_rect)
