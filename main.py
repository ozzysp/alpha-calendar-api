# This application is a simple backend for the frontend calendar

import os
import sys
import json
import datetime
import calendar
import requests
import time
import logging
import logging.config
import argparse
import configparser
import pprint
import re
import subprocess
import urllib.parse
import urllib.request
import urllib.error


# Global variables
# ------------------------------------------------------------------------------
# The config file is read from the current directory
config_file = 'config.ini'
# The config file is read from the current directory
log_file = 'logging.ini'
# The config file is read from the current directory
calendar_file = 'calendar.json'
# The config file is read from the current directory
calendar_file_backup = 'calendar.json.bak'


# Functions
# ------------------------------------------------------------------------------
def get_config(config_file):
    """
    Read the config file and return the config object
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config


def get_logger(log_file):
    """
    Read the log config file and return the logger object
    """
    logging.config.fileConfig(log_file)
    return logging.getLogger('main')

