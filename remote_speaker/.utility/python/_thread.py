# -*- coding: UTF-8 -*-
"""

该模块提供了操作多个线程（也被称为 轻量级进程 或 任务）的底层原语 —— 多个控制线程共享全局数据空间。

为了处理同步问题，也提供了简单的锁机制（也称为 互斥锁 或 二进制信号）。

当发生特定于线程的错误时，RuntimeError将引发异常。

使用示例::

import _thread
import time

def th_func(delay, id):
    while True:
        time.sleep(delay)
        print('Running thread %d' % id)

for i in range(2):
    _thread.start_new_thread(th_func, (i + 1, i))

"""


def start_new_thread(function, args, kwargs):
   """
   开启一个新线程并返回其标识

   :param function: 回调函数
   :param args: 初始化参数个数
   :param kwargs: 初始化参数列表
   :returns: 空
   :raises OSError: EINVAL
   """
   pass


def exit():
   """
   抛出 SystemExit 异常

   :param 空:
   :returns: 空
   :raises OSError: SystemExit
   """
   pass


def allocate_lock():
   """
   返回一个新的锁对象

   :param 空:
   :returns: 获取的锁对象
   :raises OSError: 空
   """
   pass


def get_ident():
   """
   返回当前线程的 “线程描述符”

   :param 空:
   :returns: int
   :raises OSError: EINVAL
   """
   pass


def stack_size():
   """
   返回新建线程时使用的堆栈大小

   :param 空:
   :returns: 堆栈大小
   :raises OSError: EINVAL
   """
   pass
