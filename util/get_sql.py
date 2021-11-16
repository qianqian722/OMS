# -*- coding: utf-8 -*-
# @Time    : 2021/10/8 2:16 下午
# @Author  : 可以是创建人信息
# @Site    : 
# @File    : get_sql.py
# @Software: PyCharm
# import pymysql
# from sshtunnel import SSHTunnelForwarder
#
# with SSHTunnelForwarder(
#     ssh_address_or_host=('47.97.216.184', 22),       # ssh 目标服务器 ip 和 port
#     ssh_username="zhangqiuhong",     # ssh 目标服务器用户名
#     #ssh_password= "",           # ssh 目标服务器用户密码
#     ssh_pkey="C:\\Users\\Administrator\\.ssh\\id_rsa",   # ssh 目标服务器证书
#     #ssh_private_key_password="",  # ssh 目标服务器证书密码
#     remote_bind_address=('10.10.xx.xxx', 3306),     # mysql 服务ip 和 port
#     local_bind_address=('127.0.0.1', 5143)                     # ssh 目标服务器的用于连接 mysql 或 redis 的端口，该 ip 必须为 127.0.0.1
# ) as server:
#     conn = pymysql.connect(
#         host=server.local_bind_host,                # server.local_bind_host 是 参数 local_bind_address 的 ip
#         port=server.local_bind_port,                # server.local_bind_host 是 参数 local_bind_address 的 port
#         user="name",
#         password="password",
#         db="test_data",
#         charset="utf8"
#     )
#     cursor = conn.cursor()
#     sql = "SELECT * FROM satel_report WHERE id = 1"
#     try:
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         print(data)
#     except:
#         print("SQL执行失败")

import pymysql
from sshtunnel import SSHTunnelForwarder

# with SSHTunnelForwarder(
#         ('跳板机外网IP', 端口),
#         ssh_username="ly",
#         ssh_password="123123",
#         remote_bind_address=('MSYQL真实IP', 3306)) as server:
#     conn = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
#                            port=server.local_bind_port,
#                            user='ly',
#                            passwd='123123',
#                            db='')


with SSHTunnelForwarder(
         ('47.97.216.184', 22),    #B机器的配置
         ssh_password="zhangqiuhong",
         ssh_username="zhangqiuhong",
         remote_bind_address=('47.97.216.18', 3306),
)as server:  #A机器的配置

    conn = pymysql.connect(host='127.0.0.1',              #此处必须是127.0.0.1
                           port=3306,
                           user='zhangqiuhong',
                           passwd='zhangqiuhong',
                           db='yaoyu_dev')

# )as server:
#     cursor = conn.cursor()
#         sql = "SELECT * FROM orders WHERE oid = 881912"
#         try:
#             cursor.execute(sql)
#             data = cursor.fetchall()
#             print(data)
#         except:
#             print("SQL执行失败")
print('ok')