''' CPU & Memory Data processing'''
#coding:utf-8
import os,time
import sys
import linecache
import xlwt
from utile import setting
import types
from pyecharts import Line
import subprocess

def IntoExcel_row(Sheet,Data,row):
    for i in range(len(Data)):
        Sheet.write(row,i,Data[i])


'''CPU data is writed into excel'''
def CPUintoExcel(cpufile,Sheet):
    row=0
    row_cpu=1
    for line in cpufile:
        if row_cpu%2==1:
            line=line.split(' ')
            cpudata=[line[i] for i in (2,4,7)]
            #cpudata=[line[i] for i in (0,1,2)]
            IntoExcel_row(Sheet,cpudata,row)
            row += 1
        row_cpu += 1
    
'''Memory data is writed into excel'''

def MemintoExcel(memfile,Sheet):
    native = subprocess.getoutput(' grep "Native Heap " %s |awk \'{print $3}\' ' % memfile).split('\n')
    native.insert(0,'Native')
    # print (len(native))
    # print (native)
    dalvik = subprocess.getoutput(' grep "Dalvik Heap " %s |awk \'{print $3}\' '% memfile).split('\n')
    dalvik.insert(0,'Dalvik')
    # print (dalvik)
    total = subprocess.getoutput('grep "TOTAL:" %s |awk \'{print $2}\' ' % memfile).split('\n')
    total.insert(0,'Total')
    #mem=[list(i) for i in zip(native,dalvik,total)]
    for i in range(len(native)):
        Sheet.write(i,0,native[i])
    for i in range(len(dalvik)):
        Sheet.write(i,1,dalvik[i])
    for i in range(len(total)):
        Sheet.write(i,2,total[i])


def MemintoChart(memfile, name):
    native = subprocess.getoutput(' grep "Native Heap " %s |awk \'{print $3}\' ' % memfile).split('\n')
    native.insert(0, 'Native')
    print(native)
    dalvik = subprocess.getoutput(' grep "Dalvik Heap " %s |awk \'{print $3}\' '% memfile).split('\n')
    dalvik.insert(0, 'Dalvik')
    print (dalvik)
    total = subprocess.getoutput('grep "TOTAL:" %s |awk \'{print $2}\' ' % memfile).split('\n')
    total.insert(0, 'Total')
    id = []
    for i in range(len(native)-1):
        id.append(i)
    bar = Line(f"{name}__内存数据图形报表", "图表纵轴为数据大小，横轴为时间节点，直线为平均值")
    bar.add("native", id, native[1:], label_color=['#800080'], mark_line=["average"],
            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    bar.add("dalvik", id, dalvik[1:], label_color=['#0000FF'], mark_line=["average"],
            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    # bar.add("total", id, total[1:], label_color=['#2E8B57'], mark_line=["average"],
    #         mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    bar.use_theme("vintage")
    t = time.time()
    bar.render('%s\\memory%s.html' % (setting.data, int(t)))

def CPUintoChart(cpufile, name):
    row = []
    row_cpu = 1
    for line in cpufile:
        if row_cpu%2 == 1:
            line = line.split(' ')
            cpudata = [line[i] for i in (2, 4, 7)]
            row.append(cpudata)
        row_cpu += 1
    data = []
    for i in row:
        if i[1][0].isdigit() is False:
            pass
        else:
            data.append(i)
    package = []
    user = []
    kernel = []
    for j, k, l in data:
        package.append(j[0:-1])
        user.append(k[0:-1])
        kernel.append(l[0:-1])
    package.insert(0, 'package')
    user.insert(0, 'user')
    kernel.insert(0, 'kernel')
    print(package)
    print(user)
    print(kernel)
    id = []
    for i in range(len(package) - 1):
        id.append(i)
    bar = Line(f"{name}__CPU数据图形报表", "图表纵轴为数据大小，横轴为时间节点，直线为平均值")
    bar.add("package", id, package[1:], label_color=['#800080'], mark_line=["average"],
            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    bar.add("user", id, user[1:], label_color=['#0000FF'], mark_line=["average"],
            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    bar.add("kernel", id, kernel[1:], label_color=['#2E8B57'], mark_line=["average"],
            mark_point=["max", "min"], xaxis_interval=0, xaxis_rotate=90)
    bar.use_theme("vintage")
    t = time.time()
    bar.render('%s\\cpu%s.html' % (setting.data, int(t)))


# date = time.strftime("%Y%m%d", time.localtime(time.time()))
date = 20210122
Path = setting.BASE_DIR + r'\output\{}'.format(date) + '\\'
# print(Path)
cpufile = Path+'{}_cpu.txt'.format(setting.device_id)
memfile = Path+'{}_mem.txt'.format(setting.device_id)
# print(memfile)
# file1 = open('%s' % cpufile)
# file2 = open('%s' % memfile)
# wbk = xlwt.Workbook()
# sheet1 = wbk.add_sheet('cpu')
# sheet2 = wbk.add_sheet('memory')

# CPUintoExcel(file1,sheet1)
# MemintoExcel(memfile,sheet2)
# wbk.save('%s\\performance.xls'% setting.data)
CPUintoChart(open(cpufile), setting.name[3])

# MemintoChart(memfile, setting.name[3])

