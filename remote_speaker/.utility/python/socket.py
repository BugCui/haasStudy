# * coding: UTF8 *
"""

该模块实现socket相关操作

函数
-----------------------------------------------------------
"""

def close():
   """
    标记关闭的socket。一旦发生这种情况，所有将对socket对象进行的操作都将失败。远程端将无法再接收到任何数据（队列数据刷新后）。

    Socket在垃圾回收时自动关闭，但是建议您明确地关闭它们，或在使用时附加声明语句。

   :param af:
   :param type:
   :param proto:
   :returns: 0: 成功，其他: 失败
   """
   pass


def bind(address):
    """
    将socket绑定到地址。socket不能为已绑定的。
    """
    pass


def listen(backlog):
    """
    启用一个服务器以接受连接。若指定积压工作，则其不得小于0（若数值小于0，则需设置为0）；
    指定系统在拒绝新连接之所允许的未接受的连接的数量。若未指定，则选择一个默认的合理值。
    """
    pass

def accept():
    """
    接受连接。Socket须绑定到一个地址并监听连接。返回值是两个数值（conn, address），
    其中conn为一个新的socket对象，可用来发送和接收连接上的数据，而address是绑定到连接另一端的socket的地址。
    """
    pass


def connect(address):
    """
    连接到地址上的远程socket。
    """
    pass


def send(bytes):
    """
    将数据发送到socket。Socket须连接到一个远程socket。
    """
    pass


def sendall(bytes):
    """
    将数据发送到socket。Socket须连接到一个远程socket。

    将所有数据发送到套接字。套接字须连接到一个远程套接字。与 send() 不同，该方法会通过连续发送尽量发送所有数据。

    该方法在非阻塞套接字上的行为尚未定义。因此在MicroPython中，推荐使用 write() 方法，该方法对阻塞套接字实行相同的“无短写”方法，并将返回在非阻塞套接字上发送的字节的数量。
    """
    pass


def recv(bufsize):
    """
    从socket上接收数据。返回值是一个表示接收到的数据的字节对象。要接收到的数据最大数量由缓冲区大小指定。
    """
    pass


def sendto(bytes, address):
    """
    将数据发送到socket。Socket不应连接到远程socket，因为目的地socket由 address 指定。
    """
    pass


def recvfrom(bufsize):
    """
    从socket上接收数据。返回值是两个数值（bytes, address），其中bytes是一个表示接收到的数据的字节对象，address是发送数据的socket地址。
    """
    pass


def setsockopt(level, optname, value):
    """
    设置给定的socket选项的值。在socket模块(SO_* etc.)中定义了所需的符号常量。该值可为一个整数，也可为一个表示缓冲区的bytes类对象。
    """
    pass


def settimeout(value):
    """
    设置阻塞socket操作的超时时间。值参数可以是一个表示秒或None的非负浮点数。


    若给定一个非零值，且在操作完成前超时时间已过期，则后续的socket操作将会引发异常。


    若给定0值，则socket采用非阻塞模式。若给定None，则socket给定阻塞模式。

    .. admonition:: 与CPython区别
        :class: attention

        CPython在超时时引发 socket.timeout 异常，即一个 OSError 的子类。MicroPython则直接引发OSError。 
        若您使用 except OSError: 来匹配异常，您的代码将在MicroPython和CPython中同时运行。

    """
    pass


def setblocking(falg):
    """
    设置socket的阻塞或非阻塞模式：若标记为false，则将该socket设置为非阻塞模式，而非阻塞模式。

    该方法为某些settimeout()调用的简写:

        * ``sock.setblocking(True)`` is equivalent to ``sock.settimeout(None)``
        * ``sock.setblocking(False)`` is equivalent to ``sock.settimeout(0)``
    """
    pass


def read(size):
    """
    从socket中读取size字节。返回一个字节对象。若未给定 size ，则按照类似 socket.readall() 的模式运行，见下。
    """
    pass


def readinto(buf, nbytes):
    """
    将字节读取入缓冲区。若指定 nbytes ，则最多读取该数量的字节。否则，最多读取 len(buf) 数量的字节。正如 read() ，该方法遵循“无短读”方法。

    :returns: 读取并存入缓冲区的字节数量。
    """
    pass


def readline():
    """
    读取一行，以换行符结尾。

    :returns: 读取的行。
    """
    pass


def write(buf):
    """
    将字节缓冲区写入socket。

    :returns: 写入的字节数量。
    """
    pass
