import sys
import socket
import re

sys_args = sys.argv

def url():
    url = "none"
    if len(sys_args) > 1:
        if is_valid_ip(sys_args[1]):
            return sys_args[1]
    return url

def port():
    port = "none"
    if len(sys_args) > 2:
        if is_valid_port(sys_args[2]):
            port = sys_args[2]
    return port
    
def filename():
    sys_args.pop(0)
    filename = ""
    if len(sys_args) >= 1:
        for arg in sys_args:
            if not is_valid_ip(arg) and not is_valid_port(arg):
                filename = filename + "{0}-".format(arg)
        return filename.rstrip("-")
    raise Exception("session filename not provided!")
    
def is_valid_ip(addr):
    if re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", addr):
        return True
    return False

def is_valid_port(port):
    if re.match("\b\d{4,5}\b", port):
        return True
    return False