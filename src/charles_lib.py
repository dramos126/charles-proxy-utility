
import subprocess
import os
import socket
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.presets import control_url


class Charles:
    
    def __init__(self, url, port):
            self.url = url if url != "none" else socket.gethostbyname(socket.gethostname())
            self.port = str(port if port != "none" else 8888)
    
    this_dir = os.path.dirname(os.path.realpath(__file__))


    logs_dir = this_dir + "/logs/"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)      
    output_dir = logs_dir
   
    def send_command(self, command):
        curlCommand = "curl -v -x {0}:{1} {2}".format(self.url, self.port, command)
        subprocess.call(curlCommand, shell=True)

    def save_file(self, filename, control_url):
        curlCommand = "curl -o {0} -x {1}:{2}, {3}.".format(filename, self.url, self.port, control_url)
        subprocess.call(curlCommand, shell=True)

    def save_session_as_har(self, filename):
        har_file = "{0}{1}.har".format(self.output_dir, filename)
        self.save_file(str(har_file), control_url.export_har)    

    def delete_old_logs(self):
        os.removedirs(self.output_dir)
