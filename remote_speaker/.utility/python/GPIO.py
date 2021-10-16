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

def write(value):
   """
   设置GPIO电平值，GPIO引脚为输出模式时可用

   :param value: 待写入的数据
   :returns: 0: 成功，其他: 失败
   :raises OSError: EINVAL
   """
   pass

def read():
   """
   读取GPIO电平值，输入模式和输出模式时均可用

   :param 空: 
   :returns: 0: 低电平，1:高电平 其他: 失败
   :raises OSError: EINVAL
   """
   pass

def enableIrq(callback):
   """
   使能GPIO中断功能，并设置回调函数

   :param callback: 回调函数 
   :returns: 0: 成功 其他: 失败
   :raises OSError: EINVAL
   """
   pass

def disableIrq():
   """
   关闭中断功能

   :param 空: 
   :returns: 0: 成功 其他: 失败
   :raises OSError: EINVAL
   """
   pass

def clearIrq():
   """
   清楚中断

   :param 空: 
   :returns: 0: 成功 其他: 失败
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

