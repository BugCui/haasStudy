# * coding: UTF8 *
"""
使用外部储存（磁盘文件）实现简单的键值数据库
"""

def open(stream, flags=0, cachesize=0, pagesize=0, minkeypage=0):
   """
   从随机存取的 ``stream``（类似一个打开的文件）中打开一个数据库。
   所有其他的参数都是可选的，且都只为关键字，并允许对数据库操作的高级参数进行调整（大多数用户并不会需要这个）。

   :param flag: 当前未使用的
   :param cachesize: 以字节计的建议最大内存缓存大小。对于一个由充足内存的板而言，使用更大值或许可以提高性能。该值只是推荐值，若该值设置过低，则模块可能会占用更多内存。
   :param pagesize: B树中用于节点的页面大小。可接受范围为512-65536。若为0，则会使用基础I/O块的大小（内存使用和性能之间的最佳协调）。
   :param minkeypage:  每个页面存储的键的最小数量。默认值为0等于2。

   :returns: 返回一个B树对象，该对象实现一个字典协议（方法集）和下下面的一些附加方法。
   """
   pass

def close():
   """
   关闭数据库。处理结束时关闭数据库是强制性的，因为某些未写入的数据可能仍留在缓存中。
   注意：这并不会关闭随数据库打开的基础流，基础流应单独关闭（这也是强制性的，以确保从缓冲区中刷新的数据进入底层储存）。

   :param 空:
   :returns 空: 
   """
   pass

def flush():
   """
   将缓存中的任何数据刷新到底层流。

   :param 空:
   :returns: 空
   """
   pass

def __getitem__(key):
   """
   标准字典方法，查询一个键值对。

   :param key: 查询的键
   :returns: 查询键对应的值
   """
   pass

def get(key, default=None):
   """
   标准字典方法，获取一个键值对。

   :param key: 查询的键
   :param default: 字典键不存在的时候返回的默认值
   :returns: 查询键对应的值，缺失情况下返回 default 定义的值
   """
   pass

def __setitem__(key, val):
   """
   标准字典方法，设置一个键值对。

   :param key: 设置的键
   :param val: 设置的键对应的值
   :returns: 空
   """
   pass

def __delitem__(key):
   """
   标准字典方法，删除一个键值对。

   :param key: 待删除的键
   :returns: 空
   """
   pass

def __contains__(key):
   """
   标准字典方法。

   :param 空:
   :returns: 空
   """
   pass

def __iter__():
   """
   B树对象可被直接迭代（与字典相似）以按顺序访问所有键。
   """
   pass

def keys(start_key, end_key, flags):
   """
    """
   pass

def values(start_key, end_key, flags):
   """
   """
   pass 

def items(start_key, end_key, flags):
   """
   ``keys``, ``values``, ``items``这些方法类似于标准字典方法，但也可使用可选参数来迭代一个键子范围，而不是整个数据库。 
   
   注意：这三种方法中， *start_key* 和 *end_key* 参数都代表键值。
   
   例如，`values()` 方法将迭代与给定键范围对应的值。 
   无 *start_key* 值即意为 “从首个键”，无 *end_key* 值或其值为None则意为 “直到数据库结束” 。 
   默认情况下，范围包括 *start_key* ，而不包括 *end_key* ，您可以通过传递 `btree.INCL` 的标记来将 *end_key* 包括在迭代中。 
   您可以通过传递 `btree.DESC` 的标记来按照下行键方向进行迭代。标记值可同为ORed。
   """
   pass

 