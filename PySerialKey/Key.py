import pyautogui
import serial
import serial.tools.list_ports
import keyboard


def list_serial():
    ports_list = list(serial.tools.list_ports.comports())
    if len(ports_list) <= 0:
        print("无串口设备。")
    else:
        print("可用的串口设备如下：")
        for comport in ports_list:
            print(list(comport)[0], list(comport)[1])


def get_ble_key():
    ser = serial.Serial("COM14", 9600, 5)
    if ser.isOpen():  # 判断串口是否成功打开
        print("打开串口成功！")
        print(ser.name)  # 输出串口号
        while True:
            com_input = ser.read(4)
            if com_input:  # 如果读取结果非空，则输出
                send_key(com_input)
    else:
        print("打开串口失败。")


def convert_scan_code_to_key(scan_code):
    keys = keyboard.key_to_scan_codes(scan_code)
    if keys:
        return keys[0]
    return None


def send_key(key):
    print(key)
    # pyautogui.keyDown('ctrl')
    # pyautogui.keyDown('c')
    # pyautogui.keyUp('c')
    # pyautogui.keyUp('ctrl')
    if key == b'0001':
        pyautogui.press("enter")


if __name__ == '__main__':
    list_serial()
    while True:
        try:
            get_ble_key()
        except:
            pass