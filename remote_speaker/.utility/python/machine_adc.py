# * coding: UTF8 *
"""

=================================================================================================

"""

def ADC(channel):
   """
   创建 ADC 类对象

   :param channel(int): 通道索引号，每个硬件设备支持的通道数目受硬件限制，具体通道数目请参考硬件手册。HaaS硬件默认提供两个通道。
   :returns: ADC 类句柄
   :raises ValueError: EINVAL
   """
   pass


def read_u16():
   """
   读取打开的ADC通道的数据，返回无符号16bits数据。

   :param 空:
   :returns: ADC数值。
   """
   pass


def read():
   """
   读取打开的ADC通道的数据，返回无符号16bits数据。

   :param 空:
   :returns: ADC数值。
   """
   pass


def atten(value):
   """
   衰减数值，单位是dB。HaaS平台暂时不支持这个功能。

   :param value(int): 衰减数值
   :returns: 空
   """
   pass


def width(value):
   """
   设置采样位宽，支持的数据位宽为 WIDTH_9BIT, WIDTH_10BIT, WIDTH_11BIT, WIDTH_12BIT, WIDTH_13BIT

   :param value(int): 采样位宽
   :returns: 空
   """
   pass

