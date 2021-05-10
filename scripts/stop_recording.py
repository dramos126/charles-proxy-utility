import os
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.charles_lib import Charles
from src.presets import control_url
from scripts import get_args

Charles(get_args.url, get_args.port).send_command(control_url.stop_recording)