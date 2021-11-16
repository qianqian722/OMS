# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 10:32 上午
# @Author  : 可以是创建人信息
# @Site    : 
# @File    : shell.py
# @Software: PyCharm
"""
封装执行shell语句方法
"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o