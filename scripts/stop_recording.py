import os
from src.charles_lib import Charles
from src import control_url
from scripts import get_args

url = get_args.url
port = get_args.port
Charles(url, port).sendCommand(control_url.stop_recording)