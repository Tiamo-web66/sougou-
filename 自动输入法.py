"""
Python实现模拟按键刷搜狗拼音输入法字数
"""
import time
import win32con
import win32api

print("倒计时结束之前，请对焦到可以输入的地方。。。")
print("ESC键可对此程序进行退出。。。")


# 请求用户需要输入的文字
text_input = input("请输入逆向输入的文字拼音（以1结尾，例如：nihaoshijie1）：")

# 请求用户输入倒计时秒数
user_input = input("请输入倒计时秒数（秒）后回车：")
try:
    countdown_seconds = int(user_input)  # 尝试将输入转换为整数
    if countdown_seconds < 0:
        print("倒计时秒数不能为负数。")
        exit()  # 如果输入无效，退出程序
except ValueError:
    print("无效的输入，请输入一个整数。")
    exit()  # 如果输入无法转换为整数，退出程序

# 根据用户输入的秒数进行倒计时
for i in range(countdown_seconds, 0, -1):
    print(f"{i}秒后自动输入法开始。。。")
    time.sleep(1)

print("自动输入法开始。。。")



VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'clear': 0x0C,
    'enter': 0x0D,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'caps_lock': 0x14,
    'esc': 0x1B,
    'spacebar': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'select': 0x29,
    'print': 0x2A,
    'execute': 0x2B,
    'print_screen': 0x2C,
    'ins': 0x2D,
    'del': 0x2E,
    'help': 0x2F,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'F13': 0x7C,
    'F14': 0x7D,
    'F15': 0x7E,
    'F16': 0x7F,
    'F17': 0x80,
    'F18': 0x81,
    'F19': 0x82,
    'F20': 0x83,
    'F21': 0x84,
    'F22': 0x85,
    'F23': 0x86,
    'F24': 0x87,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '+': 0xBB,
    ',': 0xBC,
    '-': 0xBD,
    '.': 0xBE,
    '/': 0xBF,
    '`': 0xC0,
    ';': 0xBA,
    '[': 0xDB,
    '\\': 0xDC,
    ']': 0xDD,
    "'": 0xDE,
    '`': 0xC0
}

# 初始化输入字数计数器
total_chars = 0
def key_input(input_words=''):
    global total_chars  # 声明使用全局变量
    """
    输入要操作的键(多个),电脑自动模拟输入
    如:sasdj
    :param input_words:
    :return:
    """
    for word in input_words:
        win32api.keybd_event(VK_CODE[word], 0, 0, 0)
        time.sleep(0.01)
        win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
        total_chars += 1  # 每输入一个字符，计数器递增
    time.sleep(0.01)

def key_even(input_key):
    """
    输入要操作的键(单个),电脑自动模拟输入
    如:w
    :param input_key:
    :return:
    """
    win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)


# 增加检测ESC键的循环
while True:
    if win32api.GetAsyncKeyState(VK_CODE['esc']) == -32767:  # 检测ESC键是否被按下
        print("检测到ESC按键，程序即将退出。")
        break  # 退出循环，结束程序

    time.sleep(0.01)  # 避免CPU占用过高

    # 方法调用
    key_input(text_input)  # 如果需要，取消注释来执行按键输入

print("程序即将退出。")
# 打印输入的总字数
print(f"程序已退出。共输入了 {total_chars} 个字。")