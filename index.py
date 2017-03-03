# -*-coding:utf-8-*-
import json
from flask import Flask
from flask import render_template
from utils import *
from config import *

app = Flask(__name__)


@app.route('/')
def index():
    # CPU informatiom
    CPU_temp = getCPUtemperature()
    CPU_usage = ""
    CPU_freq = str(int(getCPUfrequence()) / 1000)
    # RAM information
    # Output is in kb, here I convert it in Mb for readability

    RAM_stats = getRAMinfo()
    RAM_total = str(round(int(RAM_stats[0]) / 1000, 1))
    RAM_used = str(round(int(RAM_stats[1]) / 1000, 1))
    RAM_free = str(round(int(RAM_stats[2]) / 1000, 1))

    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = str(DISK_stats[0]).replace("G", "")
    DISK_used = str(DISK_stats[1]).replace("G", "")
    DISK_perc = str(DISK_stats[3]).replace("%", "")

    # Internal voltages for core
    CORE_volt = getCoreVolt()

    # System runtime
    SYS_runtime = getUptime()
    # Get users
    SYS_users=str(getUsers())

    return render_template("index.html", CPU_temp=CPU_temp,
                           CPU_usage=CPU_usage, CPU_freq=CPU_freq,
                           RAM_total=RAM_total, RAM_used=RAM_used,
                           RAM_free=RAM_free, DISK_total=DISK_total,
                           DISK_used=DISK_used, DISK_perc=DISK_perc,
                           CORE_volt=CORE_volt, SYS_runtime=SYS_runtime,
                           SYS_users=SYS_users)


@app.route('/refresh')
def refresh():
    # CPU informatiom
    CPU_temp = getCPUtemperature()
    CPU_usage = ""
    CPU_freq = str(int(getCPUfrequence()) / 1000)
    # RAM information
    # Output is in kb, here I convert it in Mb for readability

    RAM_stats = getRAMinfo()
    RAM_total = str(round(int(RAM_stats[0]) / 1000, 1))
    RAM_used = str(round(int(RAM_stats[1]) / 1000, 1))
    RAM_free = str(round(int(RAM_stats[2]) / 1000, 1))

    # Disk information
    DISK_stats = getDiskSpace()
    DISK_total = str(DISK_stats[0]).replace("G", "")
    DISK_used = str(DISK_stats[1]).replace("G", "")
    DISK_perc = str(DISK_stats[3]).replace("%", "")

    # Internal voltages for core
    CORE_volt = getCoreVolt()

    # System runtime
    SYS_runtime = getUptime()
    data = {"cputemp": CPU_temp, "cpuusage": CPU_usage,
            "cpufreq": CPU_freq, "ramtotal": RAM_total,
            "ramused": RAM_used, "ramfree": RAM_free,
            "disktotal": DISK_total, "diskused": DISK_used,
            "diskperc": DISK_perc, "corevolt": CORE_volt,
            "runtime": SYS_runtime}
    return json.dumps(data)


@app.route('/cpuusage')
def cpuusage():
    return str(getCPUuse())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

