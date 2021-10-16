# * coding: UTF8 *
"""

=================================================================================================

"""

def PWM(id):
   """
   创建一个具有给定id的PWM对象。 id 的值取决于特定端口及其硬件, 不同设备支持的PWM端口号数目不同，请参考具体电路手册获取。


   若无额外参数，创建PWM对象但未进行初始化（该对象有来自PWM最后一次初始化的设置，若存在的话）。 

   
   若给定额外参数，则初始化总线。初始化参数，请参见 init 函数。

      .. admonition:: 提前注意事项
         :class: important

         建议在创建PWM对象的同时进行初始化。
   """
   pass


def init(freq, duty):
   """
   初始化PWM的频率和占空比。

   :param freq: 频率
   :param duty: 占空比， 取值范围为（0，100）
   :returns: None
   """
   pass


def deinit():
   """
   关闭PWM设备

   :param 空:
   :returns: None
   """
   pass


def freq(x):
   """
   该方法允许设置并获取频率值，这取决于是否提供了参数 x。

   如果没有提供参加，则该方法获取当前的频率值；如果提供了参数值，则该方法设置新的频率值
   
   :param x: 新频率值 或 None  
   :returns: None(提供了参数) 或 int 值(未提供参数）
   """
   pass


def duty(x):
   """
   该方法允许设置并获取占空比值，这取决于是否提供了参数 x。

   如果没有提供参加，则该方法获取当前的占空比值；如果提供了参数值，则该方法设置新的占空比值
   
   :param x: 新频率值 或 None  
   :returns: None(提供了参数) 或 int 值(未提供参数）
   """
   pass


def freqduty(freq, duty):
   """
   同时设置PWM设备的频率和占空比

   :param freq:  新频率值
   :param freq:  新占空比值
   :returns: None
   """
   pass

