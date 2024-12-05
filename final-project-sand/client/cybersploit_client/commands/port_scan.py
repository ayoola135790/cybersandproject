import socket
from ..commands import Command # Required
from .. import actions # Example to import the actions folder
import time

def port_scan(target: str, port_range: tuple[int, int]) -> list[int]:

    # Create a list to store open ports
    open_ports = []
    
    # Iterate over the range of ports
    for i in range(port_range[0], port_range[1]+1):
        
        # For each port:
        # - Create a socket
        # - Attempt to connect to the ip and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((target, i))

        if not result:
            open_ports.append(i)

    # Return the list of found open ports
    print("PORT       | SERVICE")

    for p in open_ports:
        service = socket.getservbyport(p)
        print(f"{p:<10} | {service}")
    
    # Connect to port
    for p in open_ports:
        # connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(1)
        client_socket.connect((target, p))
        
        # response = client_socket.recv(2048)

        try:
            response = client_socket.recv(2048)
            if response:
                print(f"Data received from server on port {p} -->\n", response.decode('utf-8', errors='replace'))
        except socket.timeout:
            try:
                client_socket.sendall(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                response = client_socket.recv(1024)
                print(f"HTTP response from port {p} -->\n", response.decode('utf-8', errors='replace'))
            except:
                print(f"Port {p} not a web server. No data received")

        # close socket
        client_socket.close()

class PortScan(Command):
    def do_command(self, lines: str, *args):
        args = lines.split()
        port_scan(args[0], (int(args[1]), int(args[2])))

command = PortScan


