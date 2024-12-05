import socket
from ..commands import Command # Required
from .. import actions # Example to import the actions folder
import time
import subprocess


def udp_scan(target: str, port_range: tuple[int, int]) -> list[int]:


    start_port, end_port = port_range
    
    try:
        # calling Nmap with subprocess
        result = subprocess.run(
            ["sudo", "nmap", "-sU", "-p", f"{start_port}-{end_port}", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        
        # check if there were errors
        if result.stderr:
            print(f"Error during Nmap scan: {result.stderr}")
            return

        # print Nmap's output
        print("Nmap Scan Results:\n")
        print(result.stdout)

    except Exception as e:
        print(f"An error occurred while running Nmap: {e}")
    

class UdpScan(Command):
    def do_command(self, lines: str, *args):
        args = lines.split()
        udp_scan(args[0], (int(args[1]), int(args[2])))

command = UdpScan


