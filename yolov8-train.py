from ultralytics import YOLO

if __name__ == '__main__':
    # 1. 加载预训练模型
    model = YOLO('yolov8n.pt')

    # 2. 开始训练
    model.train(
        data='yolo-bvn.yaml',
        workers=1,
        epochs=50,      # 总训练轮数
        patience=25,     # 连续 25 轮 mAP 无提升就自动停止
        batch=16,        #一次性喂给模型16张图片
        name='train',
        exist_ok=True
    )