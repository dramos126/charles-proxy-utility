import sys
import socket
import re

sys_args = sys.argv

def url():
    url = "none"
    if len(sys_args) > 1:
        if valid_ip(sys_args[1]):
            return sys_args[1]
    return url

def port():
    port = "none"
    if len(sys_args) > 2:
        if valid_port(sys_args[2]):
            port = sys_args[2]
    return port
    
def filename():
    sys_args.pop(0)
    filename = None
    if len(sys_args) >= 1:
        for arg in sys_args:
            if not valid_ip(arg) and not valid_port(arg):
                filename = filename + "{0}-".format(arg)
        return filename[:-1]
    raise Exception("session filename not provided!")
    
def valid_ip(addr):
    if len(sys_args) > 1:
        try:
            socket.inet_aton(sys_args[1])
            return True
        except socket.error:
            print("not a valid IP - " + addr)
    return False

def valid_port(port):
    if re.match("\b\d{4,5}\b", port):
        return True
    print("not a valid port - " + port)
    return False