import sys
USER = "ubuntu"
HOST = "54.172.236.36"
AWS = sys.platform != 'darwin'
private_key =  "~/.ssh/cs5356"
CONFIG_PATH = __file__.split('settings.py')[0]

BUCKET_NAME = "aub3visualsearch"
PREFIX = "nyc"
INDEX_PATH = "/mnt/nyc_index/"
DATA_PATH ="/mnt/nyc_images/"
