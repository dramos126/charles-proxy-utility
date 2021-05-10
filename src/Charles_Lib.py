import subprocess
import os
import socket
import sys
from src.Control_URL import Control_URL

class Charles:
    
    def __init__(self, url = "none", port = "none"):
            self.url = url if url != "none" else socket.gethostbyname(socket.gethostname())
            self.port = str(port if port != "none" else 8888)
    
    this_dir = os.path.dirname(os.path.realpath(__file__))
    
    def get_output_dir(self):
        logs_dir = this_dir + "/logs/"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        return logs_dir
    
    output_dir = get_output_dir()
   
    def sendCommand(self, command):
        curlCommand = "curl -x -v {0}:{1} {2}".format(self.url, self.port, command)
        subprocess.call(curlCommand)

    def saveFile(self, filename, control_url):
        curlCommand = "curl -o {0} -x {1}:{2}, {3}.".format(filename, self.url, self.port, control_url))
        subprocess.call(curlCommand)

    def saveSessionAsHar(self, filename):
        har_file = output_dir + filename
        saveFile(har_file, Control_URL().export_har)

    

    

