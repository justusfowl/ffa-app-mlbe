import sys
import argparse
import logging
import os
import warnings

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

from ffacoach.API.API import initAPI

app = initAPI()
app.run(host=os.environ.get("API_HOST_IP"), port=os.environ.get("API_HOST_PORT"))