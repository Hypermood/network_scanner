import sys

import netifaces
import subprocess
import re

def get_network_connections():
    # This function gathers network connection information.
    # The implementation will vary based on the OS.
    connections = []
    if sys.platform == "win32":
        connections = get_windows_connections()
    elif sys.platform == "darwin" or sys.platform.startswith("linux"):
        connections = get_unix_connections()
    return connections

def get_windows_connections():
    result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
    return result.stdout.splitlines()

def get_unix_connections():
    result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
    return result.stdout.splitlines()

def get_unique_ips(connections):
    # Extract unique IP addresses from the connections
    # unique_ips = set()
    # for line in connections:
    #     parts = line.split()
    #     if len(parts) > 4:
    #         ip = parts[4].split(':')[0]
    #         if ip != '127.0.0.1':
    #             unique_ips.add(ip)
    # return list(unique_ips)

    ip_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    unique_ips = set()

    for line in connections:
        # Find all IP addresses in the line
        ips = ip_regex.findall(line)
        for ip in ips:
            # Exclude localhost IP
            if ip != '127.0.0.1' and ip != '0.0.0.0':
                unique_ips.add(ip)

    return unique_ips
