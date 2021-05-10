import subprocess
import os

class Charles:
    this_dir = os.path.dirname(os.path.realpath(__file__))
    
    def __init__(self, url = None, port = None):
            self.url = url
            self.port = port
    
    def get_output_dir(self):
        logs_dir = this_dir + "/logs/"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        return logs_dir
   
    def sendCommand(self, command):
        curlCommand = "curl -x -v {0}:{1} {2}".format(self.url, str(self.port), command)
        subprocess.call(curlCommand, shell=True)

    def saveFile(self, filename, format):
        curlCommand = "curl -o {0} -x {1}:{2}, {3} > {4}.".format()

   

    

