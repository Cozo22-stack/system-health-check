# System Health Check Tool

A Python-based diagnostic script that automates first-line system triage — the kind of checks an IT support technician performs when troubleshooting a user's machine.

## What It Does

Runs a full health report on the local machine, checking:

- **CPU** — current usage % and core count, flags high load
- **RAM** — total, used, and available memory with warnings
- **Disk** — storage usage and free space with low-space alerts
- **Network** — internet connectivity, hostname, and local IP address
- **System Info** — OS version, machine type, and logged-in user
- **Top Processes** — lists the 5 processes consuming the most CPU

## Example Output

```
==================================================
       SYSTEM HEALTH CHECK REPORT
       2026-05-18 10:32 AM
==================================================

[ SYSTEM INFO ]
  OS:       Windows 11
  Machine:  AMD64
  User:     Cannon

[ CPU ]
  Usage:  14.0%  ✓ Normal
  Cores:  8 logical cores

[ MEMORY (RAM) ]
  Total:     16.0 GB
  Used:      8.3 GB (52.0%)
  Available: 7.7 GB  ✓ Normal

[ DISK ]
  Total:  476.8 GB
  Used:   210.4 GB (44.0%)
  Free:   266.4 GB  ✓ Normal

[ NETWORK ]
  Internet:  ✓ Connected
  Hostname:  DESKTOP-CANNON
  Local IP:  192.168.1.105

[ TOP 5 PROCESSES BY CPU ]
  PID 4521   chrome.exe                     CPU: 6.3%
  PID 1204   python.exe                     CPU: 2.1%
  ...

==================================================
  Scan complete. Review any ⚠ warnings above.
==================================================
```

## Installation & Usage

**1. Install the dependency:**
```bash
pip install psutil
```

**2. Run the script:**
```bash
python system_health.py
```

## Why I Built This

As someone transitioning into IT support, I built this to demonstrate that I understand what first-line triage looks like — and that I can automate repetitive diagnostic tasks. Help desk techs check these exact metrics (CPU, RAM, disk, network) every time a user reports a slow or unresponsive machine. This script does it in seconds.

## Tech Used

- Python 3
- `psutil` — cross-platform system monitoring library
- `socket`, `platform`, `subprocess` — standard library modules
