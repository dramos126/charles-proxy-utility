import os
from src.charles_lib import Charles
from src.control_url import Control_URL
from get_sys_argv import Get

url = Get.url()
port = Get.port()
Charles(url, port).sendCommand(Control_URL.clear_session)