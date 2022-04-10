from db import db_handler

from lib import common
logger = common.get_logger('银行记录')

def check_account(username):
    user_dict = db_handler.select(username)
    return True,user_dict.get('balance')


def withdraws_interface(username,target_money):
    user_dict = db_handler.select(username)
    if target_money > user_dict.get('balance'):
        return False,'您的账户余额不足!!!'
    user_dict['balance'] -= target_money
    user_dict['flow'].append(f'{username}提现了{target_money}')
    logger.debug(f'{username}提现了{target_money}')
    db_handler.save(user_dict)
    return True,'提现成功!!!!'


def repay_interface(username,target_money):
    user_dict = db_handler.select(username)
    user_dict['balance'] += target_money
    user_dict['flow'].append(f'{username}充值了{target_money}')
    logger.debug(f'{username}充值了{target_money}')
    db_handler.save(user_dict)
    return True, '充值成功!!!'



def transfer_interface(username, target_user, target_money):
    if not db_handler.select(target_user):
        return False, '接收转账的用户不存在!!!!'
    user_dict1 = db_handler.select(username)
    user_dict2 = db_handler.select(target_user)
    if target_money > user_dict1.get('balance'):
        return False, '钱不够，你个穷逼!!!'
    user_dict1['balance'] -= target_money
    user_dict1['flow'].append(f'{username}转账给{target_user}{target_money}元')
    user_dict2['balance'] += target_money
    user_dict2['flow'].append(f'{target_user}收到{username}转账的{target_money}元')
    db_handler.save(user_dict1)
    db_handler.save(user_dict2)
    logger.debug(f'{username}转账给{target_user}{target_money}元')
    return True, '转账成功'


def check_flow_interface(username):
    user_dict = db_handler.select(username)
    logger.info(f'{username}查看了余额')
    return True, user_dict.get('flow')


