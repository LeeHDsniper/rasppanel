# -*-coding:utf-8-*-
import os
import re
# Return CPU temperature as a character string


def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=", "").replace("'C\n", ""))

# Return RAM information (unit=kb) in a list
# Index 0: total RAM
# Index 1: used RAM
# Index 2: free RAM


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string


def getCPUuse():
    p = os.popen("vmstat 2 5")
    lines = p.readlines()
    sum=0
    for i in range(2,7):
        m=re.findall("(\d+)",lines[i])
        sum=sum+int(m[14])
    return 100-sum/5

# Return information about: disk space as a list (unit included)
# Index 0: total disk space
# Index 1: used disk space
# Index 2: remaining disk space
# Index 3: percentage of disk used


def getCPUfrequence():
    p = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")
    freq = p.readline().replace("\n", "")
    return freq


def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return(line.split()[1:5])


def getCoreVolt():
    p = os.popen("/opt/vc/bin/vcgencmd measure_volts").readline()
    return(p.replace("volt=", "").replace("V\n", ""))


def getUptime():
    p = os.popen("uptime -p").readline()
    p = p.replace("up ","")
    p = p.replace("\n","")
    return p


def getUsers():
    p = os.popen("who -H")
    lines = p.readlines()
    data = []
    for i in range(1, len(lines)):
        m = re.findall("([^ ]+)", lines[i].replace("\n", ""))
        for n in range(len(m), 5):
            m.append("")
        temp = {"user": m[0], "line": m[1],
                "time": m[2] + ',' + m[3], "comment": m[4]}
        data.append(temp)
    return data
