# -*- coding:utf-8 -*-
#site-packages/
"""
实现用户注册登录功能
"""

__author__ = 'mm'

import hashlib
from collections import defaultdict


db = defaultdict(lambda : 'N/A')

def register():
    username = raw_input('请输入账号...')
    password = raw_input('请输入密码...')
    db[username] = getmd5(password + username + "the Salt")
    print('注册成功！')

def login():
    username = raw_input('请输入账号...')
    password = raw_input('请输入密码...')
    if db[username] == getmd5(password + username + "the Salt"):
        print('登录成功！')
        return True
    else :
        print('账号或密码错误！')
        return False

def getmd5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def main():
    print('开始注册...')
    register()
    print('开始登录...')
    b = login()
    while not b:
        b = login()

if __name__ == '__main__':
    main()