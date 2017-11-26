import logging
import configparser

security = configparser.RawConfigParser()
security.read('security.properties')

api_group_token = security['api']['group_token']
api_service_token = security['api']['service_token']

db_database = security['db']['database']
db_user = security['db']['user']
db_password = security['db']['password']
db_host = security['db']['host']

vk_url = 'https://vk.com/'
vk_photo_url_pattern = vk_url + 'photo{}'
vk_user_url_pattern = vk_url + 'id{}'
vk_group_id = -153773856

bot_top_size = 10
bot_like_cost = 10
bot_liketime_cost = 1000

log_level = logging.INFO
log_fmt = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
