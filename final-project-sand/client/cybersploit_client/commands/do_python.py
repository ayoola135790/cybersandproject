# Example of how to send data
# File is incomplete - fill in the blanks

from ..commands import Command
import socket


def process_lines(dst_ip, dst_port, command):
    data_to_send = "python " + command + "END"

    # connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((dst_ip, int(dst_port)))

    # send data to server and print response
    client_socket.send(data_to_send.encode())
    response = client_socket.recv(2048) # Can call multiple times to get more data
    print(
        "Data received from server -->\n", response.decode()
    )  # Decode bytes to string before printing

    # close socket
    client_socket.close()

class DoPython(Command):
    """Send data over the socket"""
    
    def do_command(self, lines: str, *args):
        args = lines.split(" ", 2)
        process_lines(args[0], args[1], args[2])

command = DoPython