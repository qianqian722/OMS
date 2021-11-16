# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 4:03 下午
# @Author  : 可以是创建人信息
# @Site    : 
# @File    : base_request.py
# @Software: PyCharm
# import requests
# import logging
# class BaseRequest:
#
#     def send_get(self, url, data, header=None, cookie=None):
#         """
#         Requests发送Get请求
#         :param url：请求地址
#         :param data：Get请求参数
#         :param cookie：cookie参数
#         :param header：header参数
#         """
#         response = requests.get(url=url, params=data, cookies=cookie, headers=header)
#         return response
#
#     def send_post(self, url, data, header=None, cookie=None):
#         """
#         Requests发送Post请求
#         :param url：请求地址
#         :param data：Post请求参数
#         :param data：Post请求参数
#         :param cookie：cookie参数
#         :param header：header参数
#         """
#         response = requests.post(url=url, json=data, cookies=cookie, headers=header)
#         return response
#
#         # 主函数调用
#
#     def run_main(self, method, url, data, header, cookie=None):
#         try:
#             result = ''
#             if method.upper() == 'GET':
#                 result = self.send_get(url, data, header, cookie)
#             elif method.upper() == 'POST':
#                 result = self.send_post(url, data, header, cookie)
#             return result
#         except Exception as e:
#
#             logger.exception('请求主函数调用失败：{}'.format(e))

"""
封装request
"""
import json
import os
import random
import requests
import util.Consts
from util import session
from requests_toolbelt import MultipartEncoder


class Request:

    # def __init__(self, env):
    #     """
    #     :param env:
    #     """
    #     self.session = session.Session()
    #     self.get_session = self.session.get_session(env)

    def get_request(self, url, data, header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :param cookie:
        :return:
        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)

        try:
            if data is None:
                response = requests.get(url=url, headers=header)
            else:
                response = requests.get(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        util.consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        return response_dicts

    def post_request(self, url, header, data):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        data = json.dumps(json.loads(data))
        # print("data: ", data)
        # try:
        if data is None:
            response = requests.post(url=url, headers=header)
        else:
            response = requests.post(url, headers=header, data=data)
        # except requests.RequestException as e:
        #     print('%s%s' % ('RequestException url: ', url))
        #     print(e)
        #     return ()
        #
        # except Exception as e:
        #     print('%s%s' % ('Exception url: ', url))
        #     print(e)
        #     return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        util.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        # print(response_dicts)
        # print(type(response_dicts))
        return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                header['Content-Type'] = enc.content_type
                response = requests.post(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds/1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        util.consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        util.consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts