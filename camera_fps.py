import cv2
import os
import time
from datetime import datetime

def main():
    # 接入内窥镜
    camera_index = 1
    cap = cv2.VideoCapture(camera_index,cv2.CAP_DSHOW) # DSHOW代表使用 Windows 的 DirectShow API 来打开和读取摄像头设备

    if not cap.isOpened():
        print("无法打开摄像头")
        return 

    # 设置分辨率
    width = 1280
    height = 720
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

    # 显示当前实际分辨率
    cur_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cur_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"当前画面分辨率为{cur_w}×{cur_h}")

    # 创建截图保存目录
    save_dir = "picture"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # 窗口标题
    window_name = "Endoscope Live Feed (S: Save, Q: Quit)"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    # 计算FPS
    prev_time = time.time()
    fps = 0.0

    while True:
        ret,frame = cap.read()
        if not ret:
            print("无法读取视频帧")
            return

        cur_time = time.time()
        time_diff = cur_time - prev_time
        prev_time = cur_time

        if time_diff > 0:
            instant_fps = 1.0 / time_diff
            # 指数平滑算法，避免数值快速剧烈抖动
            fps = 0.9 * fps + 0.1 * instant_fps if fps != 0.0 else instant_fps

        # 显示FPS
        display_frame = frame.copy() #深拷贝当前处理的图像 frame ，避免污染原图像
        fps_text = f"FPS:{fps:.1f}"

        # 左上角绿色显示实时FPS
        cv2.putText(display_frame, fps_text, (20, 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow(window_name,display_frame)

        # 按键检测与截图保存
        key = cv2.waitKey(1) & 0xFF

        # 空格键保存
        if key == 32: #ASCII码值
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
            filename = os.path.join(save_dir, f"endoscope_{timestamp}.jpg")

            # 保存原始画质帧
            cv2.imwrite(filename,frame)
            print(f"截图已经保存到{filename}")


            # 截图保存成功提示
            flash_frame = display_frame.copy()
            cv2.putText(flash_frame, "SAVED!", (200, 40), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow(window_name, flash_frame)
            cv2.waitKey(200)

        # ESC键退出程序
        elif key == 27:
            print("退出程序")
            break

    cap.release
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

            


