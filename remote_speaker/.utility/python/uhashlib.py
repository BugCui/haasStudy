# * coding: UTF8 *
"""
该模块实现二进制数据的散列算法。目前实现了SHA256算法。SHA256是深思熟虑之选，这是一种现代的加密安全算法。


这意味着单个算法既可覆盖任何散列算法的用例，也可覆盖与安全相关的使用，从而省略了诸如MD5或SHA1之类的遗留算法以节省时间。

| 

* SHA256 - 最新一代，现代散列算法（SHA2串联）。适用于包含在MicroPython核心中的加密安全，且除有特定代码大小限制外，建议所有板都提供该算法。
* SHA1 - 上一代算法。不推荐作新用法，但是SHA1属于网络标准与现有应用程序的一部分，因此针对网络连通性和可互通性的板子将尝试实现这一算法。
* MD5 - 遗留算法，并未实现加密安全等相关功能。只有选定的针对遗留应用程序的可使用性的板才提供这一算法。

|

使用示例
      >>> import uhashlib, ubinascii
      >>> x = uhashlib.sha256()
      >>> x.update(b"haas")
      >>> ubinascii.hexlify(x.digest())
      b'984f7b4489f974f98c2929585947bb95b5ef997b8d6b354115d8163b9e489208'

类
------------------------------   
"""

class sha256(object):

   """
   创建一个hasher对象，并选择性地将数据输入其中
   """

   def __init__(self,data):
      pass

   def update(self,data):

      """
      将更多二进制数据输入hash
      """
      pass

   def digest(self):

      """
      返回用于所有通过散列传递的所有数据的散列。调用该方法后，其他数据无法再输入到散列中。
      """
      pass

   def hexdigest(self):
  
      """
      该方法尚未实现。请使用 ``ubinascii.hexlify(hash.digest())`` 以达到相似效果。
      """
      pass


class sha1(object):

   """
   创建一个SHA1 hasher对象，并视需要将 `data` 输入其中
   """

   def __init__(self, data):
      pass

   def update(self, data):
      """
      将更多二进制数据输入hash
      """
      pass

   def digest(self):
      """
      返回用于所有通过散列传递的所有数据的散列。调用该方法后，其他数据无法再输入到散列中。
      """
      pass

   def hexdigest(self):
    
      """
      该方法尚未实现。请使用 ``ubinascii.hexlify(hash.digest())`` 以达到相似效果。
      """
      pass

class md5(object):
  
   """
   创建一个MD5 hasher对象，并视需要将 `data` 输入其中
   """

   def __init__(self,data):
      pass

   def update(self,data):

      """
      将更多二进制数据输入hash
      """
      pass

   def digest(self):

      """
      返回用于所有通过散列传递的所有数据的散列。调用该方法后，其他数据无法再输入到散列中。
      """
      pass
      
   def hexdigest(self):
    
      """
      该方法尚未实现。请使用 ``ubinascii.hexlify(hash.digest())`` 以达到相似效果。
      """
      pass
