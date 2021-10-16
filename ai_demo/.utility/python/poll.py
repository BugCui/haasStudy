# * coding: UTF8 *
"""
poll类，调用uselect.poll()后返回的示例

| 
"""


def register(obj, eventmask):
    """
    在轮询对象中注册 ``stream`` 目标用来轮询。
    eventmask 是可选的位掩码，用于指定要检查的事件类型, 默认值是 uselect.POLLIN | uselect.POLLOUT。

    * uselect.POLLIN - 可供读取的数据
    * uselect.POLLOUT - 更多可供写入的数据

    .. admonition:: 注意
        :class: note

        诸如uselect.POLLHUP和uselect.POLLERR之类的标志不能作为输入事件掩码使用(这些是未经请求的事件，无论是否要求，它们都会从poll() 返回), 此语义是根据POSIX定义的。


    可以为同一obj多次调用此函数，连续调用会将obj的事件掩码更新为事件掩码的值。

    """
    pass


def unregister(obj):
    """
    从轮询中注销obj
    """
    pass


def modify(obj, eventmask):
    """
    修改obj的事件掩码。如果未注册obj，则会引发OSError并出现ENOENT错误。
    """
    pass


def poll(timeout):
    """
    等待至少一个已注册的对象准备就绪或处于异常状态，并带有以毫秒为单位的可选超时（如果未指定timeout参数或指定为-1，则持续等待）。
    

    返回（obj，event，…）元组的列表, 元组中可能还有其他元素，具体取决于平台和版本，因此不要假定其大小为2。
    

    event元素指定流中发生了哪些事件，并且是上述uselect.POLLIN / uselect.POLLOUT 常量的组合。
    

    .. admonition:: 注意
        :class: note

        标记uselect.POLLHUP和uselect.POLLERR可以在任何时候返回（即使未要求), 并且必须相应地对其进行操作（相应的流已从poll中注销，并且可能已关闭),
        因为否则将进一步调用poll() 可能会立即返回，并再次为此流设置这些标志。


    如果超时，则返回一个空列表。
    """
    pass


def ipoll(timeout):
    """
    与poll.poll（）类似，但是返回一个迭代器，该迭代器生成被调用方拥有的元组。此功能提供了一种高效，无需分配的方式来轮询流。


    如果标志为1，则采用事件的一次性行为：发生事件的流将自动重置其事件掩码（相当于poll.modify（obj，0)),
    因此不会为该流添加新事件进行处理，直到使用poll.modify（）设置了新的蒙版为止。
    

    此行为对于异步I/O调度程序很有用。
    """
    pass
