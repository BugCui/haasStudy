# * coding: UTF8 *
"""

=================================================================================================

"""

def DAC(channel):
   """
   创建 DAC 类对象

   :param channel(int): 通道索引号，每个硬件设备支持的通道数目受硬件限制，具体通道数目请参考硬件手册。
   :returns: DAC 类句柄
   :raises ValueError: EINVAL
   """
   pass


def write(value):
   """
   将value数据写入DAC通道。

   :param value(int):  写入数字数值到DAC通道，value数据范围为（0-255）
   :returns: 空
   """
   pass
