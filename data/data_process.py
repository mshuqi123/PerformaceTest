#!/usr/bin/env python
# coding:utf-8
import os
import sys
import linecache
import xlwt
import types
import subprocess
import time


def IntoExcel_row(Sheet, Data, row):
    for i in range(len(Data)):
        Sheet.write(row, i, Data[i])


'''CPU data is writed into excel'''


def CPUintoExcel(cpufile, Sheet):
    row = 0
    row_cpu = 1
    for line in cpufile:
        if row_cpu % 2 == 1:
            line = line.split(' ')
            cpudata = [line[i] for i in (2, 4, 7)]
            IntoExcel_row(Sheet, cpudata, row)
            row += 1
        row_cpu += 1


'''Memory data is writed into excel'''


def MemintoExcel(memfile, Sheet):
    native = subprocess.getoutput(' grep "Native Heap " %s |awk \'{print $3}\' ' % memfile).split('\n')
    native.insert(0, 'Native')
    dalvik = subprocess.getoutput(' grep "Dalvik Heap " %s |awk \'{print $3}\' ' % memfile).split('\n')
    dalvik.insert(0, 'Dalvik')
    print (dalvik)
    total = subprocess.getoutput('grep "TOTAL:" %s |awk \'{print $2}\' ' % memfile).split('\n')
    total.insert(0, 'Total')
    for i in range(len(native)):
        Sheet.write(i, 0, native[i])
    for i in range(len(dalvik)):
        Sheet.write(i, 1, dalvik[i])
    for i in range(len(total)):
        Sheet.write(i, 2, total[i])

def search_cpufile():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    result_path = "./output/" + date
    print (result_path)
    #os.path.basename
    for each in os.listdir(result_path):
        all_path = os.path.join(result_path,each)
        if os.path.isfile(all_path):
            fname = os.path.splitext(each)[0]
            if "cpu" in fname:
                return


            #os.path.splitext(each)[0]

    
# if __name__ == '__main__':
#     main()