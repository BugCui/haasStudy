# * coding: UTF8 *
"""
加密/解密模块

常量
-----------

.. data:: MODE_ECB
.. data:: MODE_CBC
.. data:: MODE_CTR

"""

def aes(key, mode, IV):
   """
    初始化一个密码对象 (cipher) 用于加密/解密操作。注意：初始化后， cipher 对象只能用于加密或解密。
    不允许创建一个密码对象(cipher) 同时用于加密()、解密()操作::

        crypto = aes(b"1234" * 4, 1)
        enc = bytearray(32)
        crypto.encrypt(bytes(range(32)), enc)
        print(enc)

        crypto = aes(b"1234" * 4, 1)
        dec = bytearray(32)
        crypto.decrypt(enc, dec)
        print(dec)


   :param key: 加密/解密 秘钥。(bytes格式)
   :param mode: 加密/解密模式：
        * ``1`` (or ``ucryptolib.MODE_ECB``) 表示 电子密码本 (Electronic Code Book).
        * ``2`` (or ``ucryptolib.MODE_CBC``) 表示 密码块链接 （Cipher Block Chaining）.
        * ``6`` (or ``ucryptolib.MODE_CTR``) 表示 计数器模式 (Counter mode).
   :param IV: 是CBC模式的初始化向量。在计数器模式下，IV 为计数器的初始值

   :returns: 密码对象 cipher
   """
   pass

def encrypt(in_buf, out_buf):
   """
    加密 *in_buf*。


    如果没有给出 *out_buf*，则返回结果为新分配的 `bytes` 对象。否则，结果被写入 可变的缓冲 *out_buf*。
    *in_buf* 和 *out_buf* 也可以使用相同的可变缓冲区。


   :param in_buf: 待加密数据。
   :param out_buf: 加密后输出数据，该参数可以不指定，未指定则在返回参数中携带加密数据。

   :returns: 空 或者 加密后数据

   """
   pass

def dencrypt(in_buf, out_buf):
   """
    解密 *in_buf*。

   :param in_buf: 待解密数据。
   :param out_buf: 解密后输出数据，该参数可以不指定，未指定则在返回参数中携带解密数据。

   :returns: 空 或者 解密后数据

   """
   pass