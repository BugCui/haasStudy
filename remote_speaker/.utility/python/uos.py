# -*- coding: UTF-8 -*-
"""

提供操作系统相关的功能函数 和 文件操作功能函数

=================================================================================================

"""

def uname():
    """
    返回一个元组（可能是一个命名了的元组），其中包含有关底层机器和/或其操作系统的信息。
    
    
    元组按以下顺序有五个字段，每个字段都是一个字符串：

        * sysname – 底层系统的名称
        * nodename – 节点名（/板子名称）（可以与sysname相同）
        * release – 底层系统的版本
        * version – MicroPython版本和构建日期
        * machine – 底层硬件的标识符（例如，板卡信息，CPU信息）

    :raises OSError: ENOENT
    """
    pass

def urandom(n):
    """
    返回一个字节(bytes)对象，该对象包含n个字节。使用该函数的时候建议n为4的整数倍，这样生成的字节组合起来就是一个32bit随机数，否则生成的随机数会被截取。

        下面的示例示例展示了生成一个32bit的随机数：
            >>> a = binascii.hexlify(uos.urandom(4))
            >>> a
            b'e9508139'
            >>> a[0:8]
            b'e9508139' 

        下面的示例示例展示了生成两个32bit的随机数，可以按字节数取出相应的随机数：
            >>> c = binascii.hexlify(uos.urandom(8))
            >>> c
            b'57165237db2f9a4d'
            >>> c[0:8]
            b'57165237'
            >>> c[9:16]
            b'b2f9a4d'

    :param n(int): 待生成的随机字节的数目
    :raises OSError: ENOENT
    """
    pass


def chdir(path):
    """
    切换到 path 指定的目录。

    :param path(str): 待切换的目的路径
    :raises OSError: ENOENT
    """
    pass

def getcwd():
    """
    获取当前目录。

    :param 空:
    :returns(str): 当前目录
    :raises OSError: ENOENT
    """
    pass

def ilistdir(dir):
    """
    该函数返回一个迭代器，该迭代器将生成与它所列出目录中的条目相对应的3元组。无参数情况下，列出当前目录，否则列出由 dir 指定的目录。

    3元组的形式包括 （名称、类型、索引节点） :

        * name 为一个字符串（若dir为一个字节对象，则名称为字节）且为条目的名称；
        * type 为一个指定条目类型的整数，其中目录为0x4000，常规文件为0x8000；
        * inode 为一个与文件的索引节点相对应的整数，而对于没有这种概念的文件系统来说，可能为0。
    :param dir(str): 待列出待切换的目的路径
    :raises OSError: ENOENT
    """
    pass


def listdir(dir):
    """
    若无参数，则列出当前目录；否则将列出给定目录。
    """
    pass


def mkdir(path):
    """
    创建一个指定path的新目录。
    """
    pass

def remove(path):
    """
    删除一个指定path的文件。
    """
    pass

def rmdir(path):
    """
    删除一个指定path的目录。
    """
    pass


def rename(old_path, new_path):
    """
    重命名文件。
    """
    pass

def stat(path):
    """
    获取文件或目录的状态。
    """
    pass

def statvfs(path):
    """
    获取文件系统的状态。按照以下顺序返回一个具有文件系统信息的元组:

        * f_bsize – 文件系统块大小
        * f_frsize – 碎片大小
        * f_blocks – f_frsize单元中fs的大小
        * f_bfree – 空闲块的数量
        * f_bavail – 非特权用户的免费块数
        * f_files – 索引节点的数量
        * f_ffree – 空闲索引节点的数量
        * f_favail – 非特权用户的免费空闲索引节点的数量
        * f_flag – 挂载标志
        * f_namemax – 最大文件名长度

    受 aos3.3 系统能力所限，目前 f_frsize f_flags 参数返回0。

    """
    pass


def sync():
    """
    同步所有文件系统。
    """
    pass

"""

================================================================

"""

def open(path, mode):
    """
    打开文件，具体使用方式参考Linux C下的fopen函数。

    :param path(str): 待打开的文件路径及文件名;
    :param mode(str): 待打开的文件长度操作形态;
    :returns: 若文件打开成功，返回值为文件流指针。若文件打开失败, 则返回Null。
    :raises OSError: ENOENT
    """
    pass

def read(buf, size, nmemb, stream):
    """
    从文件流读取数据，具体使用方式参考Linux C下的fread函数。

    :param buf(bytearray): 数据空间，用来存放读取进来的数据;
    :param size(int): 待读取的每个数据项占据的字节数;
    :param nmemb(int): 待读取的数据项数目，读取的总字符数以参数size*nmemb来决定;
    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    :returns: 实际读取到的总字符数目。
    :raises OSError: EINVAL
    """
    pass

def write(buf, size, nmemb, stream):
    """
    从文件流写入数据，具体使用方式参考Linux C下的fwrite函数。

    :param buf(bytearray): 数据空间，用来存放待写入的数据;
    :param size(int): 待写入的每个数据项占据的字节数;
    :param nmemb(int): 待写入的数据项数目，写入的总字符数以参数size*nmemb来决定;
    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    :returns: 实际写入到的总字符数目。
    :raises OSError: EINVAL
    """
    pass

def close(stream):
    """
    关闭文件，具体使用方式参考Linux C下的fclose函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    :returns: 0: 成功，其他: 失败
    :raises OSError: EINVAL
    """
    pass

def seek(buf, size, nmemb, stream):
    """
    移动文件流的读写位置，具体使用方式参考Linux C下的fseek函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    :param offset(int): 相对 whence 的偏移量，以字节为单位;
    :param whence(int): 开始添加偏移 offset 的位置，它一般指定为: SEEK_SET, SEEK_CUR和SEEK_END;
    
    :returns: 0: 成功，其他: 失败
    :raises OSError: EINVAL
    """
    pass

def tell(stream):
    """
    获取给定流stream的当前文件位置，具体使用方式参考Linux C下的ftell函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    
    :returns: 若获取成功则返回位置标识符的当前值；若获取失败则返回-1L。
    :raises OSError: EINVAL
    """
    pass

def rewind(stream):
    """
    设置文件位置为给定流stream的文件的开头，具体使用方式参考Linux C下的rewind函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    
    :returns: 空
    :raises OSError: EINVAL
    """
    pass

def getpos(stream):
    """
    获取流 stream 的当前文件位置，具体使用方式参考Linux C下的fgetpos函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    
    :returns: 如果成功则返回当前文件位置，如果失败则返回-1。
    :raises OSError: EINVAL
    """
    pass

def setpos(stream, pos):
    """
    设置给定流 stream 的文件位置为给定的位置，具体使用方式参考Linux C下的fsetpos函数。

    :param stream(nil): 通过open函数获取到的已打开的文件指针;
    :param pos(int): 需要设置的文件位置;
    :returns: 0: 成功，其他: 失败
    :raises OSError: EINVAL
    """
    pass