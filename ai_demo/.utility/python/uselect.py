# * coding: UTF8 *
"""
该模块提供的功能可以有效地等待多个 **streams** (选择准备进行操作的流) 上的事件。

| 
"""

def poll():
    """
        创建一个轮询的实例
    """
    pass


def select(rlist, wlist, xlist, timeout):
    """
        等待一组对象上的活动。该函数效率不高，推荐使用poll函数。

        :param rlist: 读列表
        :param wlist: 写列表
        :param xlist: 执行列表
        :param timeout: 超时时间，单位为ms
        :returns: 空
    """
    
    pass

