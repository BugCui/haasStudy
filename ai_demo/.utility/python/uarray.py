# * coding: UTF8 *
"""
该模块实现相应CPython模块的子集，如下所示

|

支持格式编码： ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` （后两种依赖于浮点支持）

|

- 使用示例
      >>> import uarray
      >>>
      >>> tt = uarray.array('i', [1, 2, 3])
      >>> tt
      array('i', [1, 2, 3])
      >>> 
      >>> tt.append(5)
      >>> tt
      array('i', [1, 2, 3, 5])
      >>> 

类

"""

class array(object):

    """
    使用给定类型的元素创建数组。数组的初始内容由 iterable 给定。若未给定内容，则创建一个空数组
    """

    def __init__(self,typecode,iterable=None):
        pass

    def append(self,val):
        """
        将新元素添加到数组末尾，并不断增加
        """
        pass

    def extend(self,iterable):

        """
        将包含在迭代中的新元素添加到数组末尾，并不断增加
        """
        pass