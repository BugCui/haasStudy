# -*- coding: UTF-8 -*-
"""

ModBus工业协议标准接口
======================================

| 

"""


def PARITY():
    """
    奇偶校验枚举值

        * PARITY_NONE = 0
        * PARITY_ODD = 1
        * PARITY_EVEN = 2
    """
    pass


def STATUS():
    """
    读写操作状态码枚举值

        * MB_SUCCESS = 0
        * MB_MUTEX_ERROR = 1
        * MB_INVALID_SLAVE_ADDR = 2
        * MB_INVALID_PARAM = 3
        * MB_RESPOND_EXCEPTION = 4
        * MB_RESPOND_LENGTH_ERR = 5
        * MB_RESPOND_FRAME_ERR = 6
        * MB_RESPOND_TIMEOUT = 7
        * MB_CANNOT_GET_HANDLER = 8
        * MB_SLAVE_NO_RESPOND = 9
        * MB_FRAME_SEND_ERR = 10
        * MB_SERIAL_INIT_FAILED = 11
        * MB_SERIAL_UNINIT_FAILED = 12
        * MB_FUNCTION_CODE_NOT_SUPPORT = 13
    """
    pass

def init(port, baud_rate, parity, timeout):
    """
    初始化modbus协议

    :param port(int): 必选参数，RS485串口端口号
    :param baud_rate(int): 可选参数，波特率，默认值为9600
    :param parity(int): 可选参数，奇偶校验信息，默认值为0。可选值参考奇偶校验信息（PARITY）
    :param timeout(int): 可选参数，相应等待超时，单位是毫秒（ms），-1表示永久等待。默认值为200
    :returns: 0: 成功，其他: 失败，返回结果具体含义参考 STATUS 信息

    :raises OSError: EBUSY 或 EINVAL
    """
    pass

def deinit():
    """
    释放modbus协议

    :returns:  0: 成功，其他: 失败，返回结果具体含义参考 STATUS 信息
    :raises OSError: EBADF
    """
    pass


def writeHoldingRegister(slave_addr, register_addr, register_value, timeout):
    """
    向从机写单个保持寄存器 

    :param slave_addr(int): 请求的从机地址，0代表广播
    :param register_addr(int): 写寄存器的地址
    :param register_value(int): 写寄存器的数据
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。
    :returns: tuple，4元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * resp_addr: 响应地址
      * resp_value: 响应数据
      * exception_code: 响应异常代码

    :raises RuntimeError: EINVAL
    """
    pass


def writeMultipleHoldingRegisters(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    向从机多个保持寄存器中写入数据。

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待写寄存器的起始地址
    :param reg_quantity(int): 待写寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 写寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。
    :returns: tuple，4元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败。具体数值参考 STATUS
      * resp_addr: 响应地址
      * resp_quantity: 真实完成寄存器操作的数量
      * exception_code: 异常代码

    :raises ValueError: EINVAL
    """
    pass


def writeCoil(slave_addr, coil_addr, coil_value, timeout):
    """
    向从机某个线圈中写入数据

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param coil_addr(int): 写线圈的地址
    :param coil_value(int): 写线圈的数据
    :param timeout(int): 请求超时时间，单位是毫秒（ms）。-1表示永久等待。
    :returns: tuple，4元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * resp_addr: 响应地址
      * resp_value: 响应数据
      * exception_code: 异常代码

    :raises OSError: EINVAL
    """
    pass


def writeMultipleCoils(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    向从机多个线圈中写入数据。

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待写寄存器的起始地址
    :param reg_quantity(int): 待写寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 写寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。

    :returns: tuple，4元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败。具体数值参考 STATUS
      * resp_addr: 响应地址
      * resp_quantity: 真实完成寄存器操作的数量
      * exception_code: 异常代码

    :raises ValueError: EINVAL
    """
    pass


def readHoldingRegisters(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    读取多个保持寄存器中的数据

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待读寄存器的起始地址
    :param reg_quantity(int): 待读寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 读寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。

    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * respond_count: 读取到数据的字节数，该数值不大于data的长度

    :raises OSError: EINVAL
    """
    pass


def readInputRegisters(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    读取多个输入寄存器中的数据

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待读寄存器的起始地址
    :param reg_quantity(int): 待读寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 读寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。

    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * respond_count: 读取到数据的字节数，该数值不大于data的长度

    :raises OSError: EINVAL
    """
    pass


def readDiscreteInputs(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    读取多个离散输入中的数据

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待读寄存器的起始地址
    :param reg_quantity(int): 待读寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 读寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。

    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * respond_count: 读取到数据的字节数，该数值不大于data的长度

    :raises OSError: EINVAL
    """
    pass


def readCoils(slave_addr, start_addr, reg_quantity, data, timeout):
    """
    读取多个线圈中的数据

    :param slave_addr(int): 请求的从机地址，0代表广播。
    :param start_addr(int): 待读寄存器的起始地址
    :param reg_quantity(int): 待读寄存器的数量，表示操作多少个寄存器
    :param data(bytearray): 读寄存器的数据，注意每个寄存器包含高低两个字节
    :param timeout(int): 请求超时时间，单位是毫秒（ms），-1表示永久等待。
    
    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * respond_count: 读取到数据的字节数，该数值不大于data的长度

    :raises OSError: EINVAL
    """
    pass

def recv():
    """
    接收主机发送的请求命令，轮训间隔由 init 函数的 timeout参数决定

    :param 空:
    
    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * bytes: 接收到的数据，包含CRC校验数据

    :raises OSError: EINVAL
    """
    pass


def send(slave_addr, data, timeout):
    """
    发送响应数据给主机

    :param slave_addr(int): 响应请求的从机地址
    :param data(bytearray): 响应数据，格式为： fucntion + resp data
    :param timeout(int): 发送超时时间，单位是毫秒（ms），-1表示永久等待。
    
    :returns: tuple，2元组中的条目格式为:

      * status: 请求状态，0表示成功，其他表示失败
      * length: 发送的响应帧的长度，包含CRC校验长度

    :raises OSError: EINVAL
    """
    pass
    