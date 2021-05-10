import sys

class Get:
    sys_args = sys.argv

    def url():
        url = "none"
        if len(sys_args) > 1:
            url = sys_args[1]
        return url

    def port():
        port = "none"
        if len(sys_args) > 2:
            port = sys_args[2]
        return port
    
    def filename():
        if not len(sys_args) > 3:
            raise Exception("Charles session filename not provided!")
        return sys_args[3]