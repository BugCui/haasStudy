# * coding: UTF8 *
"""

=================================================================================================

"""

def WDT(id, timeout):
   """
   构造一个具有给定id的WDT对象。

   :param id: 看门狗索引号，每个硬件设备支持的数目受硬件限制，具体数目请参考硬件手册。
   :param timeout: 超时参数，单位是ms。在timeout时间之内内有喂狗则重启系统。
   :returns: WDT 类句柄
   :raises ValueError: EINVAL
   """
   pass


def feed():
   """
   喂狗操作，应用程序连续两次喂狗时间不超过 timeout 

   :param 空:
   :returns: None
   """
   pass
