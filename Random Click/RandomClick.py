import time
import random
import pyautogui
import datetime
import keyboard

# 配置项
stop_minutes = 30  # 停止时间，单位：分钟
max_clicks = 100  # 最大点击次数
min_delay = 50  # 最小点击延迟，单位：毫秒
max_delay = 500  # 最大点击延迟，单位：毫秒
STOP_KEY = 'esc'  # 定义停止快捷键

# 计算停止时间戳
stop_time = time.time() + (stop_minutes * 60)

# 记录当前点击次数
click_count = 0

# 全局开关：通过修改该变量可以停止程序
is_running = True

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def stop_program():
    global is_running
    is_running = False
    print(f"\n你按下了 {STOP_KEY}! 程序正在停止...")

# 注册停止快捷键
keyboard.on_press_key(STOP_KEY, lambda _: stop_program())

print(f"程序已启动，按 {STOP_KEY} 键停止程序...")
print("3秒后开始运行...")
time.sleep(3)  # 添加3秒延迟

# 开始随机点击循环
while is_running:
    current_time = time.time()

    # 检查是否到达停止条件（时间或点击次数）
    if current_time >= stop_time or click_count >= max_clicks:
        print("到达设定条件，程序已停止运行。")
        is_running = False
    else:
        # 获取屏幕尺寸
        screen_width, screen_height = pyautogui.size()

        # 定义中心区域的边界比例（10%的边距）
        margin_ratio = 0.3
        min_x, max_x = screen_width * margin_ratio, screen_width * (1 - margin_ratio)
        min_y, max_y = screen_height * margin_ratio, screen_height * (1 - margin_ratio)

        # 在中心区域内生成随机位置
        x = random.randint(int(min_x), int(max_x))
        y = random.randint(int(min_y), int(max_y))

        # 执行实际的点击操作
        pyautogui.click(x, y)

        # 增加点击计数
        click_count += 1

        # 输出调试信息
        current_formatted_time = get_current_time()
        delay = min_delay + random.random() * (max_delay - min_delay)
        print(f"点击位置: ({x}, {y}), 当前点击次数: {click_count}, 当前时间: {current_formatted_time}, 下次点击延迟: {delay:.2f}ms")

        # 安排下一次点击
        time.sleep(delay / 1000)  # 将毫秒转换为秒

print("脚本已停止。")