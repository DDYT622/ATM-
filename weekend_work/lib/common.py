import hashlib
from core import src
from conf import settings
import logging
import logging.config

def get_md5(data):
    md5 = hashlib.md5()
    md5.update(bytes(data.encode('utf8')))
    return md5.hexdigest()

def login_outh(func_name):
    def inner(*args,**kwargs):
        if src.is_login.get('username'):
            res = func_name(*args,**kwargs)
            return res
        else:
            print('您还未登录，请先登录!!!')
            res = src.login()
            return res
    return inner



def get_logger(title):
    logging.config.dictConfig(settings.LOGGING_DIC)  # 自动加载字典中的配置
    logger1 = logging.getLogger(title)
    return logger1