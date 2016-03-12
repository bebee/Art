__author__ = 'aub3'
import jinja2,os
TEST = True
DBNAME = 'visiondb'
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
S3BUCKET = ""
CONFIG_PATH = __file__.split('__init__.py')[0]
EC2_MODE = False
AMI = ''
USER = "root"
HOST = "104.131.6.105"
private_key = "~/.ssh/linode" # cs5356"