import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.charles_lib import Charles
from scripts import get_args

Charles(get_args.url(), get_args.port()).save_session_as_har(get_args.filename())