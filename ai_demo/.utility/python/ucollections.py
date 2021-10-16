# * coding: UTF8 *
"""
该模块实现相应CPython模块的子集,主要提供命名元组功能

|

- 使用示例
      >>> import ucollections
      >>>
      >>> mytuple = ucollections.namedtuple('mytuple', ('id', 'name'))
      >>> t1 = mytuple(1, 'foo')
      >>> t2 = mytuple(3, 'bar')
      >>>
      >>> print(t1.id)
      1
      >>> print(t1.name)
      foo
      >>> print(t2.id)
      3
      >>> print(t2.name)
      bar
      >>>



函数
------------------------------   

"""





def namedtuple(name,fields):
    """

    用以创建具有特定名称和字段集的命名元组函数。命名元组为元组的子类， 它可以通过数值索引或具有符号字段名的属性访问语法来访问其字段，字段是指定字段名的字符串序列。 

    """
    pass

# def OrderedDict(dictlist):
#     """
#     ``dict`` 类型的子类，该子类记住并保存所添加键的顺序。当有序字典重复时，键/项将按照其添加的顺序返回

#     使用示例::

#         from ucollections import OrderedDict
#         # 将有序字典从序列对（键、值）中初始化
#         d = OrderedDict([("z", 1), ("a", 2)])
#         # 可添加更多项
#         d["w"] = 5
#         d["b"] = 3
#         for k, v in d.items():
#             print(k, v)

#     Output::

#         z 1
#         a 2
#         w 5
#         b 3
#     """
#     pass









