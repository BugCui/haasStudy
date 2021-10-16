# -*- coding: UTF-8 -*-
"""
随机数生成器函数接口
"""

def getrandbits(n):
    """
    返回一个具有 n 个随机位的整数，其中 n 可能介于 1-32（含）之间。
    """
    pass

def seed(n):
    """
    用已知整数 n 初始化随机数生成器。
    """
    pass


def randint(a, b):
    """
    返回一个随机整数 N，使得 a <= N <= b。
    """
    pass

def randrange(stop):
    """
    返回一个介于零到（但不包括）停止数之间的随机选择的整数。
    """
    pass

def randrange(start, stop):
    """
    从范围（开始，停止）中返回一个随机选择的整数。
    """
    pass

def randrange(start, stop, step):
    """
    从范围（开始，停止，步骤）中返回一个随机选择的元素。
    """
    pass


def choice(seq):
    """
    从非空序列 seq 中返回一个随机元素。如果 seq 为空，则引发 IndexError。
    """
    pass


def random():
    """
    返回 [0.0, 1.0) 范围内的下一个随机浮点数
    """
    pass


def uniform(a,b):
    """
    返回一个随机浮点数 N, 使得
      - a <= b时： a <= N <= b，
      - b < a 时： b <= N <= a。
    """
    pass
