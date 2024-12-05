from ..commands import Command
import socket


def process_lines(dst_ip, dst_port):
    data_to_send = "cron_job END"

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


class CronJobExploit(Command):
    """Create or edit cron jobs via socket communication."""

    def do_command(self, lines: str, *args):
        """
        Parses input and sends commands to create/edit cron jobs.
        """
        args = lines.split(" ", 1)
        if len(args) != 2:
            return

        dst_ip = args[0]
        dst_port = args[1]

        process_lines(dst_ip, dst_port)


command = CronJobExploit
# startup_scripts 192.168.20.129 5050 ~/.bashrc echo hi