import os
import platform
import subprocess

def ping(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def scan_network(base_ip):
    print(f"فحص الشبكة: {base_ip}.0/24")
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping(ip):
            print(f"[+] نشط: {ip}")

if __name__ == "__main__":
    network_prefix = input("أدخل نطاق الشبكة (مثال: 192.168.1): ")
    scan_network(network_prefix)
