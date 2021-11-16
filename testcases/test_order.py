# -*- coding: utf-8 -*-
# @Time    : 2021/10/13 4:43 下午
# @Author  : 可以是创建人信息
# @Site    :
# @File    : saveorder.py
# @Software: PyCharm
import json
import allure
import pytest
import requests
from data.operatexcel import OperationExcel
from data.getdata import GetTestdata
from data import getdata
from util import base_request
from util import Assert

class TestOrder:
    # def __init__(self,):
    #     self.gt = getdata.GetTestdatas()
    #     print(self.gt)


# def __init__(self, interface_name):
#     #     getdatas = get_datas(interface_name)
#     #     url = getdatas[0]
#     #     datas = getdatas[1]
#     #     header = getdatas[2]
#     #     print(url)
#     #     print(datas)
#     #     print(header)
#     getdatas = get_datas("下订单")
#     datas = getdatas[2]
#     # print(datas)
#     # print(type(getdatas))
#     @pytest.mark.parametrize("data", datas)
#     def test_saveorder(self, data):
#         testassert = Assert.Assertions()
#         getdatas = get_datas("下订单")
#         url = getdatas[0]
#         header = getdatas[1]
#         request = base_request.Request()
#         response = request.post_request(url, header, data)

# print(header)
# print(data)
# print(type(response))
# assert testassert.assert_code(response['code'], '200')

    gt = GetTestdata()

    @pytest.mark.parametrize("data", gt.get_testdata("下订单"))
    def test_saveorder(self, data):
        gt = GetTestdata().get_datas("下订单")
        print(gt)
        url = gt[0]
        header = gt[1]
        request = base_request.Request()
        response = request.post_request(url, header, data)
        print(response["code"])
        testassert = Assert.Assertions()
        assert testassert.assert_code(response["code"], 200)