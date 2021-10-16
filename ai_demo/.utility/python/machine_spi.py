# * coding: UTF8 *
"""

=================================================================================================

"""

def SPI(id):
   """
   创建一个具有给定id的SPI对象。 id 的值取决于特定端口及其硬件, 不同设备支持的SPI端口号数目不同，请参考具体电路手册获取。


   若无额外参数，创建SPI对象但未进行初始化（该对象有来自总线最后一次初始化的设置，若存在的话）。 

   
   若给定额外参数，则初始化总线。初始化参数，请参见 init 函数。

      .. admonition:: 提前注意事项
         :class: important

         建议在创建SPI对象的同时进行初始化。

   """
   pass


def init(baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0):
   """
   使用给定参数初始化SPI总线：

   :param baudrate: SCK的时钟频率。
   :param polarity: 可为0或1，并为闲置时钟线所在的层级
   :param phase: 可为0或1，分别对应第一和第二时钟脉冲边缘的采样数据。
   :param bits: 为每次传输的位宽。所有硬件都支持的位宽为8位。
   :param firstbit: 每次SPI传输先传输最高位还是最低位： 0为最高位，1为最低位
   :param mode: SPI工作模式：0为从模式， 1为主模式

   :returns: None
   :raises ValueError: EINVAL
   """
   pass


def deinit():
   """
   关闭SPI总线。

   :param 空:
   :returns: None
   """
   pass


def read(nbytes, write=0x00):
   """
   当持续写入由 write 给定的单个字节时，读取由 nbytes 指定的字节数。用读取的数据返回一个 bytes 对象。

   :param 空:
   :returns: ADC数值。
   """
   pass


def readinto(buf, write=0x00):
   """
   当持续写入由 write 给定的单个字节时，读取入由 buf 指定的缓冲区。返回 None 。

   :param value: 衰减数值
   :returns: 空
   """
   pass


def write(buf):
   """
   写入buf内包含的字节。

   :param buf: 待写出数据的缓存
   :returns: 真实写出的数据字节数
   """
   pass


def write_readinto(write_buf, read_buf):
   """
   读取入 read_buf 时，从 write_buf 中写入字节。缓冲区可为相同或不同的，但须有相同长度。

   :param write_buf: 待写出数据缓存
   :param read_buf: 待读入数据缓存
   :returns: 真实写出的字节数
   """
   pass

