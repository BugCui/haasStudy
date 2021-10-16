# -*- coding: UTF-8 -*-
"""

"""


def setlogfilesize(filesize):
    """
    设置记录到文件系统的日志文件大小

    :param filesize(int): 日志文件大小
    :returns: 0: 成功，其他: 失败

    """

    pass

def setlogfilepath(filepath):
    """
    设置记录到文件系统的日志文件路径

    :param filepath(str): 日志文件路径
    :returns: 0: 成功，其他: 失败

    """
    pass


def fsloglevel(level):
    """
    设置记录到文件系统的日志等级

    :param level(int): 日志等级值
    :returns: 0: 成功，其他: 失败

    """
    pass


def cloudloglevel(level):
    """
    设置上传到云端的日志等级
    
    `云端日志查看方法 <https://help.aliyun.com/document_detail/164456.html?spm=a2c4g.11186623.6.620.57fb52bfgHDgz6>`_
    
    :param level(int): 日志等级值
    :returns: 0: 成功，其他: 失败

    """
    pass

def stdloglevel(level):
    """
    设置本地终端日志输出等级值

    :param level(int): 日志等级值
    :returns: 0: 成功，其他: 失败

    """
    pass

def info(tag, log_str):
    """
    信息级别记录日志

    :param tag(str): 需要记录的日志tag
    :param log_str(str): 需要记录的log
    :returns: 0: 成功，其他: 失败

    """
    pass


def fatal(tag, log_str):
    """
    信息级别记录日志

    :param tag(str): 需要记录的日志tag
    :param log_str(str): 需要记录的log
    :returns: 0: 成功，其他: 失败

    """
    pass

def warn(tag, log_str):
    """
    信息级别记录日志

    :param tag(str): 需要记录的日志tag
    :param log_str(str): 需要记录的log
    :returns: 0: 成功，其他: 失败

    """
    pass

def error(tag, log_str):
    """
    信息级别记录日志

    :param log_str(str): 需要记录的log
    :returns: 0: 成功，其他: 失败

    """
    pass

def debug(tag, log_str):
    """
    debug级别记录日志

    :param tag(str): 需要记录的日志tag
    :param log_str(str): 需要记录的log
    :returns: 0: 成功，其他: 失败

    """
    pass