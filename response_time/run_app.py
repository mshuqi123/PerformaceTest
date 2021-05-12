#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, time
from utile import setting


def start_app():
    cmd = os.popen(f'adb -s {setting.device_id} shell am start -W -n {setting.launchable_activity}').read()
    t = cmd.split("WaitTime:")[1].split("Complete")[0].replace(" ", "").replace("\n", "")
    with open(setting.data + f'\\{setting.device_id}_time.txt', 'a+') as file:
        file.write(t + '\n')
    return f"该应用启动时间为：{t} 毫秒"


def stop_app():
    os.popen(f"adb -s {setting.device_id} shell am force-stop {setting.package}")
    return "关闭应用"

def get_mean_value():
    data = []
    with open(setting.data + f'\\{setting.device_id}_time.txt', 'r') as file:
        d = file.readlines()
        for i in d:
            data.append(int(i.replace("\n", "")))
    return f"该应用 {len(data)} 次的平均启动时间为：{sum(data) / len(data)} 毫秒"


def run(data):
    try:
        os.remove(setting.data + f'\\{setting.device_id}_time.txt')
    except:
        pass
    second = 0
    while second < data:
        t = start_app()
        print(t)
        time.sleep(15)
        s = stop_app()
        time.sleep(5)
        print(s)
        second += 1
    time.sleep(5)
    print(get_mean_value())



if __name__ == '__main__':
    run(5)
























