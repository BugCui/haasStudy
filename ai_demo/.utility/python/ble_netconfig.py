# * coding: UTF8 *
"""
ble_netconfig模块具体接口和参数。

==========================================================================================

"""

def init():
   """
   初始化蓝牙配置功能。

   :param 空:
   :returns: 0: 成功，其他: 失败
   """
   pass

def start():
   """
   开始进行蓝牙配置，并打开设备端蓝牙。

   :param 空:
   :returns: 0: 成功，其他: 失败
   """
   pass

def stop():
   """
   停止蓝牙配置。

   :param 空:
   :returns: 0: 成功，其他: 失败
   """
   pass

def ble_netconfig_get_wifi_status():
   """
   获取蓝牙配网后的wifi状态

   :param 空:
   :returns: wifi dict 包含SSID, IP, MAC, RSSI信息
   """
   pass

def ble_netconfig_get_status():
   """
   获取蓝牙配网状态

   :param 空:
   :returns: 0: 成功，其他: 失败
   """
   pass

