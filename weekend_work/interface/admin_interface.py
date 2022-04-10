from db import db_handler
from interface import shop_interface
from lib import common
logger = common.get_logger('管理员记录')


def lock_user():
    target_user = input('请输入您要冻结的账户>>>>>>:').strip()
    if not db_handler.select(target_user):
        return '没有此用户'
    user_dict = db_handler.select(target_user)
    user_dict['is_lock'] = True
    admin_user = is_admin_user.get('username')
    logger.debug(f'{admin_user}冻结了{target_user}')
    db_handler.save(user_dict)
    return f'{target_user}冻结成功'


def change_balance():
    target_user = input('请输入您要修改的账户>>>>>>:').strip()
    if not db_handler.select(target_user):
        return '没有此用户'
    user_dict = db_handler.select(target_user)
    new_balance = input('请输入新的额度>>>>>>:').strip()
    if not new_balance.isdigit():
        return '额度必须是数字'
    user_dict['balance'] = new_balance
    admin_user = is_admin_user.get('username')
    logger.debug(f'{admin_user}修改了{target_user}的额度')
    db_handler.save(user_dict)
    return '额度修改成功'


def del_user():
    target_user = input('请输入您要删除的账户>>>>>>:').strip()
    if not db_handler.select(target_user):
        return '没有此用户'
    confm_command = input('确认要删除此用户吗 y/n ？>>>>>>>:').strip()
    if confm_command == 'n':
        return '谢谢您的慎重考虑!!!'
    if confm_command == 'y':
        db_handler.delete(target_user)
        admin_user = is_admin_user.get('username')
        logger.debug(f'{admin_user}删除了{target_user}')
        return '用户删除成功'
    else:
        return '命令错误!!!'


def add_goods():
    goods_name = input('请输入要添加的商品的名称>>>>>>:').strip()
    for name in shop_interface.goods_list:
        if goods_name == name[0]:
            return '商品已存在!!!'
        else:
            goods_price = input('请输入要添加的商品的价格>>>>>>:').strip()
            shop_interface.goods_list.append([goods_name,goods_price])
            admin_user = is_admin_user.get('username')
            logger.debug(f'{admin_user}添加了商品{goods_name}')
            return '添加成功'




def del_goods():
    while True:
        for number, name in enumerate(shop_interface.goods_list,start=1):
            print(f'编号:  {number}  商品名称:   {name[0]}')
        goods_num = input('请输入要删除的商品的编号或按q退出>>>>>>:').strip()
        if goods_num == 'q':
            return '删除成功'
        if not goods_num.isdigit():
            print('请输入数字!!!!')
            continue
        goods_num = int(goods_num)
        if goods_num <= len(shop_interface.goods_list):
            del shop_interface.goods_list[goods_num - 1]
            print('删除成功')
            admin_user = is_admin_user.get('username')
            logger.debug(f'{admin_user}删除了编号为{goods_num}的商品')
            continue
        else:
            print('商品不存在!!!')
            continue


fun_dict = {
    '1': lock_user,
    '2': change_balance,
    '3': del_user,
    '4': add_goods,
    '5': del_goods
}
is_admin_user = {'username': None}

def admin_interface(username):
    user_dict = db_handler.select(username)
    if user_dict.get('is_admin') == False:
        return False, '您没有此权限'
    if user_dict.get('is_admin') == True:
        is_admin_user['username'] = username
        while True:
            print("""
            欢迎管理员回家
            ===========================================
                            1.冻结账户
                            2.修改额度
                            3.删除用户
                            4.添加商品
                            5.下架商品
            ===========================================
            """)
            choice = input('请选择功能编号或输入q退出>>>>>>:').strip()
            if choice == 'q':
                break
            if not choice.isdigit():
                print('这是管理员界面，不要随便尝试错误命令')
                continue
            if choice in fun_dict:
                func_name = fun_dict.get(choice)
                res = func_name()
                print(res)
            else:
                print('功能编号不存在!!!!')
        return True,'bye bye 下次再见'
