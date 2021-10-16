# * coding: UTF8 *
"""

该模块实现socket示例创建

函数
-----------------------------------------------------------
"""

def AF():
    """
    家庭类型。

        * AF_INET = 2
        * AF_INET6 = 10
    """
    pass

def SOCK():
    """
    socket类型。

        * SOCK_STREAM = 1
        * SOCK_DGRAM = 2
        * SOCK_RAW = 3
    """
    pass


def IP():
    """
    IP 协议数。

        * IPPROTO_IP = 0
        * IPPROTO_TCP = 6
        * IPPROTO_UDP = 17
    """
    pass


def OTHER():
    """
        * 套接字级别: SOL_SOCKET = 0xFFF
        * 允许本地地址复用: SO_REUSEADDR = 0x0004
        * 加入某个广播组: IP_ADD_MEMBERSHIP = 3
    """
    pass

def socket(af, type, proto):
   """
   使用给定的地址群、类型和协议号创建一个新的socket对象。

   :param af:
   :param type:
   :param proto:
   :returns: 0: 成功，其他: 失败
   """
   pass


def getaddrinfo(host, port):
    """
    将参数翻译为一个5元组序列，该序列包含创建一个与设备连接的socket所需的全部必要参数。该5元组列表有以下结构:

    .. code-block:: sh

        (family, type, proto, canonname, sockaddr)

    下列示例演示了如何连接到给定的url:

    .. code-block:: sh

        s = socket.socket()
        s.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])

    .. admonition:: 与CPython区别
        :class: attention

        该函数发生错误时，会引发一个 socket.gaierror 异常（ OSError 子类）。
        MicroPython并不具有 socket.gaierror ，会直接引发OSError。 
        注意： getaddrinfo() 的错误数量组成一个单独的名称空间，可能与 uerrno – 系统错误代码 – 系统错误代码模块中的错误数量不匹配。 
        为区分 getaddrinfo() 错误，该错误使用负数标记，标准系统错误为正数（错误数可通过使用异常对象的 e.args[0] 特性访问）。暂时使用负数，未来可能改变。


    :param host: 待访问的主机名称
    :param port: 待访问的端口号
    :returns: 0: 成功，其他: 失败
    :raises OSError: socket.gaierror
    """
    pass
