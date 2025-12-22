import socket 

#Replace with target IP
ip = '127.0.0.1'

#Replace with specific Ports to scan
#Here are some example Ports
ports = [22, 80, 443]


for i in range(len(ports)):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        if sock.connect_ex((ip, ports[i])) == 0:
            print(f'Open Port: {ports[i]}')
    sock.settimeout(1)