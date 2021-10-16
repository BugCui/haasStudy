# -*- coding: UTF-8 -*-
"""

"""



def init(data):
    """
    初始化ota服务

    :param data(dict): 字典中key'device_handle' 为必选，它的值是连接物联网平台返回的device_handle
    :returns: 0: 成功，其他: 失败

    """

    pass

def on(id,func):
    """
    注册ota升级相关的回调函数

    :param id(int): 回调函数的id
    :param func(function): id 所对应的回调函数

    :returns: 0: 成功，其他: 失败

    """
    pass


def report(data):
    """
    上报ota升级版本号，模块名等信息

    :param data(dict): data是一个字典，字典信息如下

      .. list-table::

        * - 属性
          - 类型
          - 必填
          - 说明
        * - device_handle
          - native返回的指针变量
          - 是
          - 通过这个指针，获取mqtt连接相关信息
        * - product_key
          - 字符串
          - 是
          - 物联网平台的产品key
        * - device_name
          - 字符串
          - 是
          - 物联网平台的设备名称
        * - module_name
          - 字符串
          - 是
          - 需要升级的模块名称，app升级是'default'
        * - version
          - 字符串
          - 是
          - python轻应用的版本号
    :returns: 0: 成功，其他: 失败

    """
    pass



def download(data):
    """
    下载ota升级包

    :param data(dict): data是一个字典，字典信息如下

      .. list-table::

        * - 属性
          - 类型
          - 必填
          - 说明
        * - url
          - 字符串
          - 是
          - 目标ota的下载链接
        * - store_path
          - 字符串
          - 是
          - ota包的保存路径

    :returns: 0: 成功，其他: 失败

    """
    pass


def verify(data):
    """
    升级包校验
    
    :param data(dict): data是一个字典，字典信息如下

      .. list-table::

        * - 属性
          - 类型
          - 必填
          - 说明
        * - length
          - 整形数字
          - 是
          - 目标ota的升级包大小
        * - store_path
          - 字符串
          - 是
          - ota包的保存路径
        * - hash
          - 字符串
          - 是
          - 目标ota的hash值
        * - hash_type
          - 字符串
          - 是
          - ota包的hash签名类型

    :returns: 0: 成功，其他: 失败

    """
    pass


def upgrade(data):
    """
    执行ota升级操作


    :param data(dict): data是一个字典，字典信息如下

      .. list-table::

        * - 属性
          - 类型
          - 必填
          - 说明
        * - length
          - 整形数字
          - 是
          - 目标ota的升级包大小
        * - store_path
          - 字符串
          - 是
          - ota包的保存路径
        * - install_path
          - 字符串
          - 是
          - 目标ota包的安装路径

    :returns: 0: 成功，其他: 失败

    """
    pass


