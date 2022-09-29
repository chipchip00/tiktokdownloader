import os
from web_api import app
import configparser

app_config = configparser.ConfigParser()
app_config.read('config.ini', encoding='utf-8')
api_config = app_config['Web_API']
if os.environ.get('PORT'):
    port = int(os.environ.get('PORT'))
else:
    # 默认端口
    port = api_config['Port']
app.run(host='0.0.0.0', port=port)