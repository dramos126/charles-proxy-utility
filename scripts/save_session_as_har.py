import os
from src.Charles_Lib import Charles
from src.Control_URL import Control_URL
from get_sys_argv import Get

url = Get.url()
port = Get.port()
filename = Get.fileanem()
Charles(url, port).saveSessionAsHar(filename))