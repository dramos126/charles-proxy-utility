import subprocess
import os
import socket
import sys
from presets import control_url

class Charles:
    
    def __init__(self, url, port):
            self.url = url if url != "none" else socket.gethostbyname(socket.gethostname())
            self.port = str(port if port != "none" else 8888)
    
    this_dir = os.path.dirname(os.path.realpath(__file__))
    
    def get_output_dir(self):
        logs_dir = this_dir + "/logs/"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        return logs_dir
    
    output_dir = self.get_output_dir()
   
    def send_command(self, command):
        curlCommand = "curl -x -v {0}:{1} {2}".format(self.url, self.port, command)
        subprocess.call(curlCommand)

    def save_file(self, filename, control_url):
        curlCommand = "curl -o {0} -x {1}:{2}, {3}.".format(filename, self.url, self.port, control_url)
        subprocess.call(curlCommand)

    def save_session_as_har(self, filename):
        har_file = output_dir + filename
        save_file(har_file, control_url.export_har)    

    def delete_old_logs(self):
        os.removedirs(self.output_dir)
