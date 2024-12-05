# Provided to help with creating "actions"
# You may choose to use this structure, or choose to make your own system.
# Each action is placed as its own python file in this folder.

__all__ = ["brick", "port_scan"] # List of actions here.

# Example use:

# from ..actions.port_scan import scan_ports
# scan_ports(whatever arguments)
# where a function called scan_ports is defined inside of port_scan.py
# if you have the name of the action in a string, you can use importlib:
# port_scan = importlib.import_module("..actions.port_scan")
# port_scan.scan_ports()
# If you standardize the function name to something like "run()",
# then this dynamic import will work for all actions! Just be careful
# to pass in the correct/same arguments as python is expecting!