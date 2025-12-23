import socket
from concurrent.futures import ThreadPoolExecutor

#Replace with target IP
ip = '127.0.0.1'
#Replace with max range. Default(1000)
max_port = 1000


def scan(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        if (sock.connect_ex((ip, port)) == 0):
            print(f"Open Port: {port}")


#Multithreading for faster scan
with ThreadPoolExecutor(max_workers=128) as executor: 
        executor.map(scan, range(1,max_port))


    