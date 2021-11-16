# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 11:09 上午
# @Author  : 可以是创建人信息
# @Site    : 
# @File    : datamod.py
# @Software: PyCharm
"""
定义测试数据
"""
import os
from data.operatexcel import *
from util import Log

log = Log.MyLog()


# path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
class GetTestdata:


    def get_datas(self, interface_name):
        datas = []
        operation_excel = OperationExcel()
        exceldatas = operation_excel.get_exceldatas(interface_name)
        # print(exceldatas)
        for i in range(0, len(exceldatas)):
            datas.append((exceldatas[i]["data"]))
        url = exceldatas[0]["url"]
        header = eval(exceldatas[0]["header"])
        return url, header, datas


    def get_testdata(self,interface_name):
        gts = GetTestdata().get_datas(interface_name)
        testdata = gts[2]
        return testdata

# a=GetTestdata().get_testdata("下订单")
# print(a)
# def get_parameter(name):
#     data = datamod.GetPages().get_page_list()
#     param = data[name]
#     return param
#
#
# class Basic:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Param/Basic.yaml')
#     params = get_parameter('Basic')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Collections:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Param/Collections.yaml')
#     params = get_parameter('Collections')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
#
#
# class Personal:
#     log.info('解析yaml, Path:' + path_dir + '/Params/Param/Personal.yaml')
#     params = get_parameter('Personal')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])
