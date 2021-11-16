# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 11:08 上午
# @Author  : 可以是创建人信息
# @Site    : 
# @File    : operatexcel.py
# @Software: PyCharm
import json
import os
import xlrd
import re
import threading
from datetime import datetime
from json import JSONDecodeError
class OperationExcel:

    # proDir = os.path.split(os.path.realpath(__file__))[0]
    # configPath = os.path.join(proDir, "config.ini")

    def get_sheet(self):

        book = xlrd.open_workbook(r"/Users/mac/PycharmProjects/OMS/data/OMS数据.xlsx")
        return book.sheet_by_index(0)

    def get_exceldatas(self, interface_name, sheet_name=None):
        col = 0
        exceldatas = []
        title = self.get_sheet().row_values(0)
        for i in range(0, len(title)):
            if title[i] == "interface_name":
                col = i
        # print(column)

        for row in range(1, self.get_sheet().nrows):
            row_value = self.get_sheet().row_values(row)
            # print(row_value)
            if row_value[col] == interface_name:
                exceldatas.append(dict(zip(title, row_value)))

        # print(exceldatas)
        return exceldatas

    # def get_exceldatas(self, interface_name=None, sheet_name=None):
    #
    #     exceldata = []
    #     data = []
    #     title = self.get_sheet().row_values(0)
    #
    #     for row in range(1, self.get_sheet().nrows):
    #         row_value = self.get_sheet().row_values(row)
    #
    #         exceldata.append(dict(zip(title, row_value)))
    #
    #     # print(exceldata)
    #     return exceldata

# oe=OperationExcel()
# oe.get_exceldatas(r"供应商")





    #
    # import openpyxl
    # import xlrd
    # from openpyxl.styles import NamedStyle, PatternFill
    # from xlrd import xldate_as_tuple
    # # 这下面的，是我自己写的几个工具方法，可以给出来，但是需要其他组件
    # # xls_dict 是一个 dict 可以用来修改文件中的一些数据
    # #  my_pow  封装了 pow（）函数
    # from config.XLS_DICT import xls_dict, my_pow
    #
    # # logger 日志输出组件，可以替换成 print（）
    # from utils.Logger_util import logger
    #
    # # execute_sel_sql_return_one 查询数据库的，如果没有可以 写一个空的
    # from utils.Mysql_util import execute_sel_sql_return_one
    #
    # # file_isexists输出文件的时候， 判断文件是否已经存在
    # from utils.basics_util import file_isexists
    #
    # # object_dir 一个 str 保存的是路径
    # from variable.basics_var_class import object_dir