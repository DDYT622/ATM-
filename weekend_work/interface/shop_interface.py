from db import db_handler
from lib import common
logger = common.get_logger('购物记录')

goods_list = [
        ['兰州拉面',10],
        ['胡辣汤',15],
        ['飞科剃须刀',200],
        ['漫威手办',2000],
        ['iphone14',10000]
    ]


def add_car_interface(username):
    temp_car = {}
    while True:
        for i,j in enumerate(goods_list,start=1):
            print(f"""商品编号: {i}  商品名称:  {j[0]}     商品价格:  {j[1]}""")
        choice = input('请输入您要选择的商品编号或按y结束添加>>>>>>>:').strip()
        if choice == 'y':
            user_dict = db_handler.select(username)
            for goods in temp_car:
                if goods not in user_dict.get('shop_car'):
                    user_dict['shop_car'][goods] = temp_car.get(goods)
                else:
                    user_dict['shop_car'][goods][1] += temp_car[goods][1]
            db_handler.save(user_dict)
            logger.info(f'{username}添加了商品')
            return True,'添加成功'
        if not choice.isdigit():
            print('商品编号必须是数字!!!!')
            continue
        choice = int(choice)
        if choice > len(goods_list):
            print('您挑选的商品编号不存在!!!!')
            continue
        target_num = input('请输入您要购买的数量>>>>>>:').strip()
        if not target_num.isdigit():
            print('喂喂喂!!!挑选的数量必须是数字!!!')
            continue
        target_num = int(target_num)
        user_goods_list = goods_list[choice-1]
        goods_list_name = user_goods_list[0]
        goods_list_price = user_goods_list[1]
        if goods_list_name not in temp_car:
            temp_car[goods_list_name] = [goods_list_price,target_num]
        else:
            temp_car[goods_list_name][1] += target_num




def clear_car_interface(username):
    user_dict = db_handler.select(username)
    money = user_dict.get('balance')
    total_money = 0
    for i in user_dict.get('shop_car').values():
        price, num = i
        total_money += price*num
    if total_money > money:
        return False, '钱不够，穷逼，快去充值!!!'
    user_dict['balance'] -= total_money
    user_dict['shop_car'] = {}
    user_dict['flow'].append(f'{username}结算购物车花了{total_money}')
    db_handler.save(user_dict)
    logger.debug(f'{username}结算购物车花了{total_money}')
    return True, '结算成功'




def check_car_interface(username):
    user_dict = db_handler.select(username)
    logger.info(f'{username}查看了购物车')
    return True,user_dict.get('shop_car').items()



