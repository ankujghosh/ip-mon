#!/usr/bin/env python3

import subprocess
import datetime
import time


'#This function is called initially to check if the provided ipv4 address is ping-able'


def rpm(ipv4_addr):
    try:
        subprocess.check_output(["ping", "-c 1", "-W 1", "-s 1", ipv4_addr])
        return 'passed'
    except Exception:
        return 'failed'


'#This function is called when the ping status is passed'


def rpmp(ipv4_addr, retry_interval_sec, threshold_count, ping_status, f_epoch):
    c_epoch = time.time()
    n = int("1")
    while n <= threshold_count:
        try:
            if c_epoch <= f_epoch:
                subprocess.check_output(["ping", "-c 1", "-W 1", "-s 1", ipv4_addr])
                n = int("1")
                c_epoch = time.time()
            else:
                log = str(str(datetime.datetime.now()) + " - Monitoring time expired - Stopping RPM\n")
                log_file_update(log)
                ping_status = "stopped"
                return ping_status
        except Exception:
            ping_status = "failed"
            n = n + int("1")
        time.sleep(retry_interval_sec)
    return ping_status


'#This function is called when the ping status is failed'


def rpmf(ipv4_addr, retry_interval_sec, threshold_count, ping_status, f_epoch):
    c_epoch = time.time()
    n = int("1")
    while n <= threshold_count:
        try:
            subprocess.check_output(["ping", "-c 1", "-W 1", "-s 1", ipv4_addr])
            ping_status = "passed"
            n = n + int("1")
        except Exception:
            if c_epoch <= f_epoch:
                n = int("1")
                c_epoch = time.time()
            else:
                log = str(str(datetime.datetime.now()) + " - Monitoring time expired - Stopping RPM\n")
                log_file_update(log)
                ping_status = "stopped"
                return ping_status
            pass
        time.sleep(retry_interval_sec)
    return ping_status


'#This function is called to collect ping and mtr report on fail'


def tshoot_log(ipv4_addr):
    ping = subprocess.Popen(['ping', '-c', '1', ipv4_addr], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    out, error = ping.communicate()
    if out:
        log = str("\n" + str(out) + "\n")
        log_file_update(log)
    elif error:
        log = str("\n" + str(error) + "\n")
        log_file_update(log)

    ping = subprocess.Popen(['mtr', '-nrc', '1', ipv4_addr], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            universal_newlines=True)
    out, error = ping.communicate()
    if out:
        log = str("\n" + str(out) + "\n")
        log_file_update(log)
    elif error:
        log = str("\n" + str(error) + "\n")
        log_file_update(log)


'#This function is called to create or update rpm.log file'


def log_file_update(log):
    try:
        f = open("/var/log/rpm.log", mode='a', encoding='utf-8')
        f.write(log)
        f.close()
    except Exception:
        pass
    finally:
        f.close()


'#This is the mail function which carries out the entire operation of this code'


def main():

    ipv4_addr = input("Enter the IPv4 address to probe: ")
    retry_interval_sec = int(input("Enter the delay between pings in seconds: "))
    threshold_count = int(input("Enter the threshold value before the connection is marked pass or fail: "))
    user_datetime = input("Enter the target date and time for monitoring in DD.MM.YYYY<space>HH:MM:SS :")
    '#ipv4_addr = "8.8.8.8"'
    '#retry_interval_sec = int("5")'
    '#threshold_count = int("3")'
    '#user_datetime = "21.12.2018 20:22:30"'
    pattern = '%d.%m.%Y %H:%M:%S'
    if user_datetime:
        f_epoch = int(time.mktime(time.strptime(user_datetime, pattern)))
        log = str(str(datetime.datetime.now()) + " - RPM will run until " + user_datetime + "\n")
        log_file_update(log)
    else:
        f_epoch = 2145914969
    c_epoch = time.time()
    ping_status = rpm(ipv4_addr)
    time_stamp = str(datetime.datetime.now())
    log = str(time_stamp + " - Network connection to " + ipv4_addr + " has " + ping_status + "\n")
    log_file_update(log)

    while c_epoch <= f_epoch:
        if ping_status == "passed":
            ping_status = rpmp(ipv4_addr, retry_interval_sec, threshold_count, ping_status, f_epoch)
            c_epoch = time.time()
            time_stamp = str(datetime.datetime.now())
            if ping_status == "passed" or ping_status == "failed":
                log = str(time_stamp + " - Network connection to " + ipv4_addr + " has " + ping_status + "\n")
                log_file_update(log)

        if ping_status == "failed":
            tshoot_log(ipv4_addr)
            ping_status = rpmf(ipv4_addr, retry_interval_sec, threshold_count, ping_status, f_epoch)
            c_epoch = time.time()
            time_stamp = str(datetime.datetime.now())
            if ping_status == "passed" or ping_status == "failed":
                log = str(time_stamp + " - Network connection to " + ipv4_addr + " has " + ping_status + "\n")
                log_file_update(log)


'#This triggers the entire program'


if __name__ == '__main__':
    try:
        time_stamp = str(datetime.datetime.now())
        log = str(time_stamp + " - Starting RPM - Monitoring network now\n")
        log_file_update(log)
        main()
    except KeyboardInterrupt:
        time_stamp = str(datetime.datetime.now())
        log = str(time_stamp + " - Stopping RPM - No more monitoring network\n")
        log_file_update(log)
        print("\nProgram Stopped")


