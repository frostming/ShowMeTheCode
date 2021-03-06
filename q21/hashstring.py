#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
# @Author: Frost Ming
# @Email: mianghong@gmail.com
# @Date: 2016/3/7

import os
from hashlib import sha256
from hmac import HMAC
import getpass


def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)  # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result


def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])


if __name__ == '__main__':
    password = getpass.getpass('Please input your password: ')
    hashed = encrypt_password(password)
    print "Encrypted:", hashed
    input_passwd = getpass.getpass('Please input password again: ')
    assert validate_password(hashed, input_passwd)
