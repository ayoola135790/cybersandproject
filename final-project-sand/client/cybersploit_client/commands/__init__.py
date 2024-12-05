from abc import ABC

# Commands must be added here to be used
__all__ = [
    "exit",
    "send_data",
    "port_scan",
    "send_email",
    "do_python",
    "do_bash",
    "log4shell",
    "udp_scan",
    "broken_file",
    "shellshocker",
    "do_chmod",
    "startup_scripts",
    "cron_job"
]


class Command(ABC):
    """A command that does something"""

    def do_command(self, lines: str, *args):
        raise NotImplementedError()
