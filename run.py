#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time,os
from myThread import myThread


if __name__ == '__main__':
    package = "c.l.a"

    '''Start pulling hprof files on each device'''
    print ("-------Start pulling hpro files-------")


    threads = []

    thread1 = myThread("S4SODIHAZ5JB4SLJ","C:\liuti\self\PerformaceTest\data")
    thread1.start()
    # thread2 = myThread("PullHprof","C:\liuti\self\PerformaceTest\data")
    # thread2.start()
    threads.append(thread1)
    # threads.append(thread2)
    # while True:
    #     print (thread1.isAlive())
    #     time.sleep(5)

    # for deviceid in deviceidlist:
    #     thread = myThread()
    #     threads.append(thread)

    # 开启新线程
    # for thread in threads:
    #     thread.start()
    #     print thread.name



    # time.sleep(30)
    # for thread in threads:
    #     thread.setPause(1)

    '''开启性能测试'''
    os.system('python performance.py')
