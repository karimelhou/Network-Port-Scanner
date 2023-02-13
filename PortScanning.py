import socket

def scan_ports(host, start, end):
    open_ports = []
    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == '__main__':
    host = '192.168.1.1' #Choose the IP address of the target you want to scan, in my case it's the IP address of the router.
    open_ports = scan_ports(host, 20, 25) # choose the range of ports to scan 
    print(f"Open ports on {host}: {open_ports}")
