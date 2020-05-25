# -*- coding:utf-8 -*-
import subprocess
import os
import time
from myThread import myThread
from pullhprof import getDeviceidList


def performance_info(deviceid,package1,save_path):
    time.sleep(3)
    os.popen('adb -s %s shell dumpsys cpuinfo | grep %s >> ./%s/%s_cpu.txt' %(deviceid, package1, save_path, deviceid))
    os.popen('adb -s %s shell dumpsys meminfo -a %s >> ./%s/%s_mem.txt' % (deviceid, package1, save_path, deviceid))


def run_performance(query_number):
    count = 0
    # Query = open("./sayquery.txt", "r")

    for line in range(query_number):
        print(line)
        time.sleep(5)
        for deviceid in devicelist:
            performance_info(deviceid, package, save_path = result_path)

        time.sleep(5)
        count += 1
        print (count)
        if count > query_number:
            # Query.close()
            break


if __name__ == '__main__':
    package = 'c.l.a'
    deviceidlist = getDeviceidList()
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    # global result_path
    result_path = "./output/" + date
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    devicelist = getDeviceidList()
    threads = []


    for deviceid in devicelist:
        thread = myThread(deviceid, result_path)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for deviceid in deviceidlist:
        run_performance(10000)

    time.sleep(10)

    for thread in threads:
        thread.setPause(1)




