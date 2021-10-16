# * coding: UTF8 *
"""

=================================================================================================

"""


def SoftTimer(id):
   """
   创建一个具有给定id的新软件定时器对象。

   :param id: 定时器索引号，不受硬件系统限制。
   :returns: SoftTimer 类句柄
   :raises ValueError: EINVAL
   """
   pass


def init(mode, period, callback=None):
   """
   初始化定时器。示例:
   :: 

      tim.init(period=100)                         # 周期为100ms
      tim.init(mode=SoftTimer.ONE_SHOT, period=1000)   # 1000毫秒后触发

   :param mode: 定时器工作模式，可以是其中之一：
      
      - SoftTimer.ONE_SHOT - 定时器运行一次，直到通道的配置时间到期为止。
      - SoftTimer.PERIODIC - 定时器按通道的配置频率周期性地运行。

   :param period: 定时周期，单位是毫秒(ms)
   :param callback: 定时器时间到了之后的回调函数
   :returns: None
   """
   pass


def deinit():
   """
   反初始化定时器。停止定时器，并禁用定时器外设。

   :param 空:
   :returns: None
   """
   pass


def start():
   """
   启动定时器

   :param: None
   :returns: None
   """
   pass


def stop():
   """
   暂停定时器

   :param: None
   :returns: None
   """
   pass


def period(value):
   """
   修改定制器周期

   :param value: 新定时周期参数，单位是ms
   :returns: None
   """
   pass


def value():
   """
   获取定制器当前时间参数。HaaS设备暂不支持该接口。

   :param: 
   :returns: None
   """
   pass
