from time import time
import logging
import configparser

import os


def configure_logger():
    try:
        os.makedirs(log_dir)
    finally:
        logging.basicConfig(filename=log_file, filemode='w+', format=log_fmt, level=log_level)


configuration = configparser.RawConfigParser()
configuration.read(['security.properties', 'application.properties'])

api_group_token = configuration['api']['group_token']
api_service_token = configuration['api']['service_token']

db_user = configuration['db']['user']
db_host = configuration['db']['host']
db_database = configuration['db']['database']
db_password = configuration['db']['password']

bot_top_size = int(configuration['bot']['top_size'])

log_dir = configuration['log']['dir']
log_fmt = configuration['log']['fmt']
log_file = '{}/log{}.log'.format(log_dir, int(time()))
log_level = getattr(logging, configuration['log']['level'])

vk_url = 'https://vk.com/'
