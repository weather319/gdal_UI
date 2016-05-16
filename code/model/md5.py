# -*- coding: utf-8 -*-
"""
这是一个md5加密用户名密码的程序
"""
import hashlib
import sql


db = {}

def get_md5(str):
    md5=hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(username, password): 
    db[username] = get_md5(password + username + 'python')
    conn = sql.get_conn()
    print ('注册成功！')
    

def login(username,password):
    try:  
        if get_md5(password + username + 'python') == db[username]:
            print('登陆成功！')
    except KeyError:
        print ("用户名或密码错误")
    
    

print ('请注册一个用户')
user = raw_input('请输入注册用户名: ')
pw = raw_input('请输入注册密码: ') 
register(user,pw)

print ('请登陆')
username2 = raw_input('请输入登陆用户名: ')
password2 = raw_input('请输入登陆密码: ')  
login(username2,password2)