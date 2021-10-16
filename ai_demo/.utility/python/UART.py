# * coding: UTF8 *
"""

=================================================================================================

"""

def open(type):
   """
   打开实例,type 定义在Board.json 文件中

   :param type: 对象类型
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

def setBaudRate(baud_rate):
   """
   设置串口波特率

   :param baud_rate: 波特率值
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

def write(dataBuffer):
   """
   发送串口数据，该函数为阻塞函数，串口发送完成后才会返回

   :param dataBuffer: 待写入的数据
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

def read(dataBuffer):
   """
   主动读取指定bytes的串口数据

   :param dataBuffer: 读出来数据的存储空间
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

def close():
   """
   关闭实例

   :param 空:
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

