from time import time
import logging
import configparser

configuration = configparser.RawConfigParser()
configuration.read(['security.properties', 'application.properties'])

api_group_token = configuration['api']['group_token']
api_service_token = configuration['api']['service_token']

db_database = configuration['db']['database']
db_user = configuration['db']['user']
db_password = configuration['db']['password']
db_host = configuration['db']['host']

bot_top_size = int(configuration['bot']['top_size'])

log_level = getattr(logging, configuration['log']['level'])
log_dir = configuration['log']['dir']
log_file = '{}/log{}.log'.format(log_dir, int(time()))
log_fmt = configuration['log']['fmt']

vk_url = 'https://vk.com/'
