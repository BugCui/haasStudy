# -*- coding: UTF-8 -*-
"""
| 

"""

class Client(object):

    """
    初始化client类，获取mqtt client实例

    :param 空:
    :returns: client对象

    """
    def __init__(self):
        pass

    def on_subcribe(self, id, func):
        """
        设置MQTT订阅回调函数


        :param id(int): 注册的订阅回调ID
        :param func(fucntion): 订阅回调函数
        :returns: 0

        """
        pass

    def username_pw_set(self,  username, pwd):
        """
        设置用户名和密码

        :param username(str): 用户名
        :param pwd(str): 密码
        :returns: 0: 成功，其他: 失败

        """
        pass

    def connect(self,  host, port, interval):
        """
        MQTT连接请求

        :param host(str): 待连接主机
        :param port(str): 待连接端口号
        :param interval(int): 重试周期，单位为毫秒
        :returns: 0: 成功，其他: 失败

        """
        pass

    def publish(self, topic, payload, qos):
        """
        MQTT发布主题


        :param topic(str): MQTT发布的主题
        :param payload(str): MQTT发布的消息主题
        :param qos(int): 服务质量
        :returns: 0: 成功，其他: 失败

        """
        pass

    def subscribe(self, subtopic, qos):
        """
        MQTT订阅主题

        :param subtopic(str): MQTT订阅的主题
        :param qos(int): 服务质量
        :returns: 0: 成功，其他: 失败

        """
        pass

    def loop(self, timeout):
        """
        MQTT等待响应

        :param timeout(int): 等待时间

        :returns: 0: 成功，其他: 失败

        """
        pass

    def disconnect(self):
        """
        断开MQTT连接

        :param url(str): 请求的url
        :param path(str): 保存的文件路径
        :returns: 0

        """
        pass



