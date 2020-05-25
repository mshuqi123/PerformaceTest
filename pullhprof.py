#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
可拉取测试包的hprof文件，并获得当时在运行的activities
'''

import os
import time


def getDeviceidList():
    res = os.popen('adb devices')
    devices = res.read().replace('List of devices attached', '').replace('\t', '').replace('\n', '')
    devicelist = devices.strip('').split('device')
    for deviceid in devicelist:
        if len(deviceid) == 0:
            devicelist.remove(deviceid)
    return devicelist


def pullHprof(deviceid, package, _save_path):
    '''
    pull Hprpf文件到本地
    '''

    datetime = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    ps = "adb shell ps | findstr %s" % package
    fps = os.popen(ps)
    pid = str(fps.readline()).split(" ")[5]
    os.popen("adb -s %s shell am dumpheap %s /data/local/tmp/%s.hprof" % (deviceid, pid, deviceid))
    # os.popen("adb -s %s shell am dumpheap 28276 /data/local/tmp/%s.hprof" % (deviceid, deviceid))
    time.sleep(100)
    os.popen('adb -s %s pull /data/local/tmp/%s.hprof  %s/%s_%s.hprof' % (deviceid, deviceid, _save_path, deviceid, datetime))


def activityRecord(deviceid, record_filename):
    '''
    pull Hprpf文件时，记录当前的activities
    '''
    datetime = time.strftime("%Y%m%d %H:%M:%S ", time.localtime(time.time()))
    activities = os.popen(" adb -s %s shell dumpsys activity activities | sed -En -e '/Running activities/,/Run #0/p'" % deviceid)
    file_w = open(record_filename, 'a')
    file_w.writelines("===============================================================" + "\n")
    file_w.writelines(datetime + "\n")
    file_w.writelines(activities)
    file_w.writelines("==============================================================="+ "\n")
    file_w.close()


