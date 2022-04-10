from interface import user_interface, bank_interface, shop_interface, admin_interface
from lib import common

is_login = {'username': None}


def register():
    username = input('请输入要注册的用户名>>>>>>>:').strip()
    password = input('请输入要注册的密码>>>>>>>>>:').strip()
    confm_pwd = input('请确认密码>>>>>>>>>>:').strip()
    if not password == confm_pwd:
        return '两次密码不一致!!!!'
    flag, msg = user_interface.register_interface(username, password)
    return msg


def login():
    username = input('请输入您的用户名>>>>>>>>:').strip()
    password = input('请输入您的密码>>>>>>>>:').strip()
    flag, msg = user_interface.login_interface(username, password)
    if flag:
        is_login['username'] = username
        return msg
    return msg


@common.login_outh
def check_account():
    flag, msg = bank_interface.check_account(is_login.get('username'))
    return f'您的余额为：{msg}'


@common.login_outh
def withdraws():
    target_money = input('请输入您要提现的金额>>>>>>>>:').strip()
    if not target_money.isdigit():
        return '输入的金额必须是数字!!!'
    target_money = int(target_money)
    flag, msg = bank_interface.withdraws_interface(is_login.get('username'), target_money)
    return msg


@common.login_outh
def repay():
    target_money = input('请输入要充值的金额>>>>>>:').strip()
    if not target_money.isdigit():
        return '输入的金额必须是数字!!!'
    target_money = int(target_money)
    flag,msg = bank_interface.repay_interface(is_login.get('username'),target_money)
    return msg


@common.login_outh
def transfer():
    target_user = input('输入要转账的用户>>>>>>>>:').strip()
    target_money = input('请输入要转账的金额>>>>>>>:').strip()
    if not target_money.isdigit():
        return '金额必须是纯数字!!!!'
    target_money = int(target_money)
    flag,msg = bank_interface.transfer_interface(is_login.get('username'),target_user,target_money)
    return msg


@common.login_outh
def check_flow():
    flag,msg = bank_interface.check_flow_interface(is_login.get('username'))
    if flag:
        for flow in msg:
            print(flow)
        return '流水查看完毕!!!!'



@common.login_outh
def add_car():
    flag,msg = shop_interface.add_car_interface(is_login.get('username'))
    return msg



@common.login_outh
def check_car():
    flsg,msg = shop_interface.check_car_interface(is_login.get('username'))
    if True:
        for goods in msg:
            print(goods)
        return '商品信息如上'



@common.login_outh
def clear_car():
    flag, msg = shop_interface.clear_car_interface(is_login.get('username'))
    return msg


@common.login_outh
def admin():
    flag,msg = admin_interface.admin_interface(is_login.get('username'))
    return msg

func_dict = {
    '1': register,
    '2': login,
    '3': check_account,
    '4': withdraws,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': add_car,
    '9': check_car,
    '10': clear_car,
    '11': admin
}
while True:
    print("""
    ===========================================
                    1.用户注册
                    2.用户登录
                    3.查看余额
                    4.余额提现
                    5.账户充值
                    6.账户转账
                    7.查看流水
                    8.添加购物车
                    9.查看购物车
                    10.结算购物车
                    11.管理员
    ===========================================
    """)
    choice = input('请输入您要选择的功能编号或按q退出>>>>>>>:').strip()
    if choice == 'q':
        print('欢迎下次光临')
        break
    if not choice.isdigit():
        print('输入功能编号必须是数字!!!!')
        continue
    if choice not in func_dict:
        print('您选择的功能编号不存在!!!!')
        continue
    if choice in func_dict:
        func_name = func_dict.get(choice)
        res = func_name()
        print(res)
