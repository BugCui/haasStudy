# * coding: UTF8 *
"""
基于TLS的套接字创建

"""

def wrap_socket(sock, server_side=False, keyfile=None, certfile=None, cert_reqs=CERT_NONE, ca_certs=None, do_handshake=True):
    """
    接受一个 stream 类型的 sock(通常是SOCK_STREAM类型的usocket.socket实例)，并返回ssl.SSLSocket的实例，该实例将基础流包装在SSL上下文。
    返回的对象具有通常的stream接口方法，例如 read（），write（）等。


    在MicroPython中，返回的对象不会公开套接字接口和方法，例如recv() ，send() 。特别是服务器端SSL套接字应使用从传回的普通套接字创建
    ~usocket.socket.accept()在非SSL侦听服务器套接字上。

    do_handshake: 确定握手是否作为wrap_socket的一部分完成或者是否将其推迟作为初始读取或写入的一部分（CPython中没有do_handshake方法）。
    对于阻塞式套接字，标准行为是立即进行握手。对于非阻塞套接字（即，传递给wrap_socket的sock处于非阻塞模式时），
    通常应该推迟握手，因为否则wrap_socket会阻塞直到完成。
    """
    pass

