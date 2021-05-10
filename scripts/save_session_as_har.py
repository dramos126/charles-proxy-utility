import os
from src.charles_lib import Charles
from get_sys_argv import Get

url = Get.url()
port = Get.port()
filename = Get.fileanem()
Charles(url, port).saveSessionAsHar(filename))