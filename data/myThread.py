# -*- coding:utf-8 -*-
import os
import threading
import time
from pullhprof import activityRecord, pullHprof
from utile import setting


class myThread(threading.Thread):
    def __init__(self, deviceid, result_path):
        threading.Thread.__init__(self)
        self.deviceid = deviceid
        self.result_path = result_path
        self.pause = 0

    def setPause(self, pause):
        self.pause = pause

    def getPauseStatues(self):
        return self.pause

    def run(self):
        while self.pause == 0:
            run_pull(self.deviceid, self.result_path)
            time.sleep(600)


def run_pull(deviceid, result_path):
    package = setting.package
    _hprof_save_path = result_path + "/%s" % deviceid
    if not os.path.exists(_hprof_save_path):
        os.makedirs(_hprof_save_path)

    filename = result_path + "/%s_activity_record.txt" % deviceid
    print (filename)
    activityRecord(deviceid, filename)
    time.sleep(1)
    pullHprof(deviceid, package, _hprof_save_path)


# if  __name__ == '__main__':
# #
# #     devicelist = getDeviceidList()
# #
# #     threads = []
# #
# #     for deviceid in devicelist:
# #         thread= myThread(deviceid)
# #         threads.append(thread)
# #
# #     for thread in threads:
# #         thread.start()
# #     time.sleep(10)
#
#     for thread in threads:
#         thread.setPause(1)




