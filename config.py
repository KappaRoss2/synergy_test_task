import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')


INST_USERNAME = os.getenv('INST_USERNAME')
INST_PASSWORD = os.getenv('INST_PASSWORD')
TARGET_USERNAME = os.getenv('TARGET_USERNAME')
FOLLOWERS_COUNT = int(os.getenv('FOLLOWERS_COUNT'))
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('TABLE_NAME')
