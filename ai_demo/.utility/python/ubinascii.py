# * coding: UTF8 *

"""
该模块实现相应CPython模块的子集，如下所示。

该模块实现二进制数据和ASCII格式的各种编码之间的转换（双向）。

|

- 使用示例
      >>> import ubinascii
      >>>
      >>> c = ubinascii.hexlify(s)
      >>> c
      b'68656c6c6f'
      >>> 
      >>> ubinascii.unhexlify(c)
      b'hello'
      >>> 


函数
------------------------------   

"""



def hexlify(data):
   """
   将二进制数据转换为十六进制表示。返回字节字符串。
   """
   pass


def unhexlify(data):

   """
   将十六进制数据转换为二进制表示。返回字节字符串。
   """

def a2b_base64(data):

   """
   将Base64编码数据转换为二进制表示。返回字节字符串。
   """

def b2a_base64(data):

   """
   将二进制数据转换为Base64编码数据。返回字节字符串。


   """
