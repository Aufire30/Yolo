"""
阶段 0 练习：读取一张图片并在窗口里显示。
用法：python show_image.py 图片路径
没给路径时自动使用一张系统壁纸。
"""
import sys

import cv2

# 1. 拿到图片路径
if len(sys.argv) < 2:
    # 没给路径时，自动用系统自带的一张壁纸图片
    img_path = "C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg"
    print("未提供图片路径，使用默认壁纸：", img_path)
else:
    img_path = sys.argv[1]

# 2. 读取图片（读进来就是一个 numpy 数组，每个像素是 BGR 三个值）
img = cv2.imread(img_path)

if img is None:
    print("读不到图片，请检查路径是否正确")
    sys.exit(1)

# 3. 显示图片（imshow 会弹出一个窗口）
cv2.imshow("口腔龋病AI - 图片显示", img)

print("图片尺寸:", img.shape)  # (高, 宽, 3)
print("按任意键关闭窗口")

# 4. 等待按键；waitKey(0) 表示一直等，直到用户按任意键
cv2.waitKey(0)

# 5. 关闭所有窗口
cv2.destroyAllWindows()