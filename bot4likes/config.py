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

bot_top_size = configuration['bot']['top_size']

log_level = getattr(logging, configuration['log']['level'])
log_fmt = configuration['log']['fmt']

vk_group_id = configuration['vk']['group_id']
vk_url = 'https://vk.com/'
vk_photo_url_pattern = vk_url + 'photo{}'
vk_user_url_pattern = vk_url + 'id{}'
