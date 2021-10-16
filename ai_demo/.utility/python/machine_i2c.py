# * coding: UTF8 *
"""

=================================================================================================

"""

def I2C(id, scl, sda, freq, timeout, mode, addr, addrsize):
   """
   创建 I2C 类对象

   :param id(int): 必选参数， 设备索引号，每个硬件设备支持的通道数目受硬件限制，具体通道数目请参考硬件手册。HaaS硬件默认提供两个通道。
   :param scl(Pin): 可选参数， 表示 scl 使用的硬件管脚信息。
   :param sda(Pin): 可选参数， 表示 sda 使用的硬件管脚信息。
   :param freq(int): 可选参数， I2C工作频率，默认为400KHz。
   :param timeout(int): 可选参数， 超时等待参数，单位是毫秒，默认为10ms。
   :param mode(int): 可选参数， 工作模式，1 表示主模式， 2 表示从模式。
   :param addr(int): 必选参数， I2C 设备地址。
   :param addrsize(int): 可选参数， I2C 地址模式， 7表示7bit模式， 10表示10bit模式。 默认为7bit模式
   :returns: I2C 类句柄
   :raises ValueError: EINVAL
   """
   pass


def readinto(buf, nack):
   """
   从I2C设备读数据

   :param buf(bytearray): 必选参数，读取数据的存放空间。
   :param nack(bool): 必选参数，是否需要在读取结束后发送nack信号。
   :returns: None
   """
   pass


def write(buf):
   """
   向I2C设备写数据

   :param buf(bytearray): 必选参数，待写出的数据。
   :returns(int): 成功写出的字节数据
   """
   pass


def readfrom(addr, size, stop=True):
   """
   从addr指定的从属设备中读取nbytes。使用读取的数据返回一个字节对象。

   :param addr(int): 必选参数，I2C 设备地址。
   :param size(int): 必选参数，需要读取的数据字节数。
   :param stop(bool): 可选参数，是否发送停止位，默认发送停止位。
   :returns (bytearray): 读取到的有效数据
   """
   pass


def readfrom_into(addr, buf, stop=True):
   """
   从addr指定的从属设备中读取到缓冲区中。读取的字节数量即为缓冲区的长度。

   :param addr(int): 必选参数，I2C 设备地址。
   :param buf(bytearray): 必选参数，读取后数据存放空间。
   :param stop(int): 可选参数，是否发送停止位，默认发送停止位。
   :returns: None
   """
   pass


def writeto(addr, buf, stop=True):
   """
   将字节从缓冲区中读取到addr指定的从属设备中。
   
   
   停止参数显示是否应在传输结束时发送一个停止位。若为False，则传输应在稍后继续进行。

   :param addr(int): 必选参数，I2C 设备地址。
   :param buf(bytearray): 必选参数，待写数据。
   :param stop(int): 可选参数，是否发送停止位，默认发送停止位。
   :returns: None
   """
   pass


def writevto(addr, vector, stop=True):
   """
      将 vector 中包含的字节写到 addr 指定的从设备中。 vector 应该是具有缓冲协议的元组或对象列表。 


      发送一次 addr ，然后按顺序写出 vector 中每个对象的字节。 


      vector 中的对象的长度可能为零字节，在这种情况下，它们对输出没有帮助。


      如果从 vector 中的一个对象写入一个字节后接收到的是NACK，则不发送任何剩余的字节和对象。 


      如果 stop 为 true，则即使收到一个NACK，也会在传输结束时生成STOP条件。 该函数返回已接收的ACK数。


   :param addr(int): 必选参数，I2C 设备地址。
   :param vector(list): 待写数据队列，数据格式为bytearray。
   :param stop(int): 可选参数，是否发送停止位，默认发送停止位。
   :returns: 空
   """
   pass


def readfrom_mem(addr, memaddr, nbytes, addrsize=8):
   """
   从memaddr指定的内存地址开始，从 addr 指定的从属设备中将nbytes读取到缓冲区中。


   addrsize参数指定以位为单位的地址大小（在HaaS上，该参数未被识别，地址大小通常为8位）。


   使用读取的数据返回一个字节对象。

   :param addr(int): 必选参数，I2C 设备地址。
   :param memaddr(int): 必选参数，读取的内存起始地址。
   :param nbytes(int): 必选参数，待读取的数据长度。
   :param addrsize(int): 可选参数，地址位宽大小，默认为8。
   :returns (bytearray): 读取到的数据
   """
   pass


def readfrom_mem_into(addr, memaddr, buf, addrsize=8):
   """
   从memaddr指定的内存地址开始，从addr 指定的从属设备中将nbytes读取到缓冲区中。读取的字节数量即为缓冲区的长度。


   addrsize参数指定以位为单位的地址大小（在HaaS上，该参数未被识别，地址大小通常为8位）

   :param addr(int): 必选参数，I2C 设备地址。
   :param memaddr(int): 必选参数，读取的内存起始地址。
   :param buf(bytearray): 必选参数，读取到的数据存放空间。
   :param addrsize(int): 可选参数，地址位宽大小，默认为8。
   :returns: None
   """
   pass


def writeto_mem(addr, memaddr, buf, addrsize=8):
   """
   从memaddr指定的内存地址开始，将缓冲区写到addr 指定的从属设备中。


   addrsize参数指定以位为单位的地址大小（在HaaS上，该参数未被识别，地址大小通常为8位）。

   :param addr(int): 必选参数，I2C 设备地址。
   :param memaddr(int): 必选参数，待写入内存的起始地址。
   :param buf(bytearray): 必选参数，待写入数据的存放空间。
   :param addrsize(int): 可选参数，地址位宽大小，默认为8。
   :returns: None
   """
   pass
