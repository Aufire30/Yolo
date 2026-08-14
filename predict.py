from ultralytics import YOLO

# 1. 加载刚刚训练好的最佳模型
model = YOLO(r'F:\God_road\Yolo\runs\detect\train\weights\best.pt')

# ---------------- 选项 A：测试单张图片 ----------------
# 替换为你想测试的牙齿图片路径
#image_path = r'F:\God_road\Yolo\datasets\valid\images\xxx.jpg' 

# 进行预测，conf=0.25 表示置信度大于 25% 就框出，save=True 表示把画框结果保存下来
#results = model.predict(source=image_path, save=True, conf=0.25)

#print("预测结果图已保存在:", results[0].save_dir)


# ---------------- 选项 B：连接内窥镜/摄像头实时检测 ----------------
# 提示：如果是 USB 内窥镜摄像头，把 source 改为 0 或 1 (代表摄像头编号)
model.predict(source=1, show=True, conf=0.25)