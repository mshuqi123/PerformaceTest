#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, time, shutil
from utile import setting


def del_data():
    """备份当日数据"""
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    dir = os.listdir(setting.BASE_DIR + "\output")
    for i in dir:
        if int(date) == int(i):
            path = setting.BASE_DIR + "\output" + "\\" + date
            # shutil.rmtree(path)   #删除非空文件夹
            try:
                os.rmdir(path)
            except:
                # 当日文件夹备份
                os.rename(os.path.join(setting.BASE_DIR + "\output" + "\\", date), os.path.join(setting.BASE_DIR + "\output" + "\\", date + "-" + str(int(time.time()))))
    return dir


if __name__ == '__main__':
    dirs = del_data()
    print(dirs)





