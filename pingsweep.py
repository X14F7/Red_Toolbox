
import platform
import subprocess
#Testprefix
#Use your target Network prefix
prefix = '192.168.10.'

def ping_host(ip):
    #Check if Windows or else UNIX
    param = "-n" if platform.system().lower() == "windows" else "-c"
    if platform.system().lower() == "windows":
        cmd = ["ping", param, "1", "-w", "500", ip]
    else:
        cmd = ["ping", param, "1", "-W", "1", ip]

    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=2, encoding="cp1252", errors="ignore")
    except subprocess.TimeoutExpired:
        return False
    
    if "TTL" in result.stdout:
        return True
    else:
        return False
    

def ping_sweep(prefix):
    for i in range(1,255):
        ip = f"{prefix}{i}"
        if(ping_host(ip)):
            print(f"{ip} is UP!")


ping_sweep(prefix)