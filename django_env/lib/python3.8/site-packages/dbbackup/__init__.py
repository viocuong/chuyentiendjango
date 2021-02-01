__version__ = "0.1.0"

"""
* Written by: Emmanuel DISCORS
* This is __init__.py module for loggin configuration 
* it's call for example with: from dbbackup import cleandbbackup
* yam style configuration is use to prevent tracking sensitive smtp information in git (.gitignore)
* yaml style configure smtp and console loggin
* python style for the rest of loggin configuration
*
"""

# TODO:
# try all arguments to: RotatingFileHandler

from decouple import config
import os, os.path
import yaml
import logging
import logging.config
from logging.handlers import RotatingFileHandler

# get .env variables from decouple
YAML_CONFIG_FILE = config('YAML_CONFIG_FILE')
LOGS_PATH = config('LOGS_PATH')

# configure the loggin python module for smtp and console msg (yam style):
with open(YAML_CONFIG_FILE, 'r') as f:
    config_backup = yaml.safe_load(f.read())
    logging.config.dictConfig(config_backup)

if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

simple_formater = logging.Formatter('%(asctime)s %(name)-20s %(levelname)-20s %(message)s','%m-%d-%Y %H:%M')

# config logging files for levels:
levels = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
for level in levels:
    # RotatingFileHandler: 10485760 # 10MB with 50 keep
    handler = RotatingFileHandler(LOGS_PATH + f"level-{level.lower()}.log", 
        mode="a+", maxBytes=10485760, backupCount=50, encoding="utf-8")
        
    handler.setLevel(getattr(logging, level))
    handler.setFormatter(simple_formater)
    logger.addHandler(handler)

# config logging files for modules (must be call from the module itself):
def add_module_handler(logger, level=logging.DEBUG):
    # RotatingFileHandler: 10485760 # 10MB with 50 keep
    handler = RotatingFileHandler(LOGS_PATH + f"module-{logger.name.replace('.', '-')}.log", 
        mode="a+", maxBytes=10485760, backupCount=50, encoding="utf-8")

    handler.setLevel(level)
    handler.setFormatter(simple_formater)
    logger.addHandler(handler)

