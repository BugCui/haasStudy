# * coding: UTF8 *
"""

=================================================================================================

"""


def UART(id):
   """
   构造一个具有给定id的UART对象。

   :param id: 设备索引号，每个硬件设备支持的通道数目受硬件限制，具体设备数目请参考硬件手册。HaaS硬件默认提供4个设备。
   :returns: UART 类句柄
   :raises ValueError: EINVAL
   """
   pass


def init(baudrate=115200, bits=8, parity=None, stop=1):
   """
   用给定的参数初始化UART总线:

   :param baudrate: 波特率
   :param bits: 每个字符的位数，可选数值为5，6，7，8或9。默认是8bit
   :param parity: 是奇偶校验，None，0(偶数) 或 1(奇数)。
   :param stop: 停止位的数目，1 或 2

   :returns: None
   """
   pass


def deinit():
   """
   关闭UART总线。

   :param 空:
   :returns: None
   """
   pass


def read(nbytes):
   """
   读取字符。若指定 nbytes，则最多读取该数量的字节。否则可读取尽可能多的数据。

   :param value: None 或者 nbytes
   :returns: 一个包括读入字节的字节对象。超时则返回 None
   """
   pass


def readinto(buf, nbytes):
   """
   将字节读取入 buf。若指定 nbytes ，则最多读取该数量的字节。否则，最多读取 len(buf) 数量的字节。

   :param buf: 读取数据的缓存
   :returns: 读取并存入 buf 的字节数；若超时则返回 None 。
   """
   pass


def readline():
   """
   读取一行，并以一个换行符结束。

   :param : None
   :returns: 读取的行；若超时，则返回 None 。

   """
   pass


def write(buf):
   """
   将字节缓冲区写入总线。

   :param buf: 待写入数据的缓存
   :returns: 写入的字节数；若超时，则返回 None。
   """
   pass


def sendbreak(buf, nbytes):
   """
   在总线上发送一个中断状态。这使得总线在一段时间内保持低状态，其持续时间比字符的正常传输所需时间长。(HaaS 设备暂不支持该接口)
   """
   pass

