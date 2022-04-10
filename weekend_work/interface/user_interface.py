from db import db_handler
from lib import common
logger = common.get_logger('用户记录')

def register_interface(username,password):
    if db_handler.select(username):
        return False,'用户名已存在!!!'
    password = common.get_md5(password)
    user_dict = {
        'username': username,
        'password': password,
        'balance': 15000,
        'shop_car': {},
        'flow': [],
        'is_lock': False,
        'is_admin': False
    }
    db_handler.save(user_dict)
    logger.info(f'{username}进行了注册')
    return True, '用户注册成功!!!'


def login_interface(username,password):
    if not db_handler.select(username):
        return False,'没有此用户!!!'
    password = common.get_md5(password)
    user_dict = db_handler.select(username)
    if not password == user_dict.get('password'):
        return False,'密码错误'
    if user_dict.get('is_lock') == True:
        return False,'您的账户已经冻结，请联系管理员解冻'
    logger.info(f'{username}登录了系统')
    return True,'登录成功!!!'

