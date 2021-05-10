import os
from src.charles_lib import Charles
from scripts import get_args

url = get_args.url
port = get_args.port
filename = get_args.filename
Charles(url, port).saveSessionAsHar(filename))