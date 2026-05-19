"""
system_health.py
----------------
A lightweight system diagnostic tool that checks CPU, RAM, disk,
and network health. Built to demonstrate
IT support automation skills.

Author: Cannon
"""

import psutil
import socket
import datetime
import subprocess
import platform


def print_header():
    print("=" * 50)
    print("       SYSTEM HEALTH CHECK REPORT")
    print(f"       {datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}")
    print("=" * 50)


def check_cpu():
    print("\n[ CPU ]")
    usage = psutil.cpu_percent(interval=1)
    cores = psutil.cpu_count(logical=True)
    print(f"  Usage:  {usage}%  {'⚠ High load' if usage > 80 else '✓ Normal'}")
    print(f"  Cores:  {cores} logical cores")


def check_ram():
    print("\n[ MEMORY (RAM) ]")
    ram = psutil.virtual_memory()
    total_gb = ram.total / (1024 ** 3)
    used_gb = ram.used / (1024 ** 3)
    available_gb = ram.available / (1024 ** 3)
    print(f"  Total:     {total_gb:.1f} GB")
    print(f"  Used:      {used_gb:.1f} GB ({ram.percent}%)")
    print(f"  Available: {available_gb:.1f} GB  {'⚠ Low memory' if ram.percent > 85 else '✓ Normal'}")


def check_disk():
    print("\n[ DISK ]")
    disk = psutil.disk_usage('/')
    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    print(f"  Total:  {total_gb:.1f} GB")
    print(f"  Used:   {used_gb:.1f} GB ({disk.percent}%)")
    print(f"  Free:   {free_gb:.1f} GB  {'⚠ Low disk space' if disk.percent > 90 else '✓ Normal'}")


def check_network():
    print("\n[ NETWORK ]")
    try:
        # Check internet connectivity by connecting to Google DNS
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        print("  Internet:  ✓ Connected")
    except OSError:
        print("  Internet:  ✗ No connection detected")

    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except Exception:
        local_ip = "Unable to retrieve"

    print(f"  Hostname:  {hostname}")
    print(f"  Local IP:  {local_ip}")


def check_system_info():
    print("\n[ SYSTEM INFO ]")
    print(f"  OS:       {platform.system()} {platform.release()}")
    print(f"  Machine:  {platform.machine()}")
    print(f"  User:     {psutil.users()[0].name if psutil.users() else 'Unknown'}")


def check_top_processes():
    print("\n[ TOP 5 PROCESSES BY CPU ]")
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    # Sort by CPU usage
    top = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    for p in top:
        print(f"  PID {p['pid']:<6} {p['name']:<30} CPU: {p['cpu_percent']}%")


def print_footer():
    print("\n" + "=" * 50)
    print("  Scan complete. Review any ⚠ warnings above.")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    print_header()
    check_system_info()
    check_cpu()
    check_ram()
    check_disk()
    check_network()
    check_top_processes()
    print_footer()
