
from conf import settings
import os
import json



def save(user_dict):
    username = user_dict.get('username')
    file_path = os.path.join(settings.DB_DIR,f'{username}.json')
    with open(file_path,'w',encoding='utf8')as f:
        json.dump(user_dict,f,ensure_ascii=False)


def select(username):
    file_path = os.path.join(settings.DB_DIR,f'{username}.json')
    if os.path.exists(file_path):
        with open(file_path,'r',encoding='utf8')as f:
            return json.load(f)




def delete(username):
    file_path = os.path.join(settings.DB_DIR, f'{username}.json')
    os.remove(file_path)