# * coding: UTF8 *

"""
该模块实现相应 CPython 模块的子集，如下所示。

堆队列即为以一定方式储存其所有项的列表。

|

- 使用示例
      >>> import uheapq
      >>>
      >>> li = list([15])
      >>> li.append(2)
      >>> li.append(50)
      >>> li.append(34)
      >>> li.append(37)
      >>> li.append(55)
      >>>
      >>> li
      [15, 2, 50, 34, 37, 55]
      >>>
      >>> uheapq.heapify(li)
      >>> print(li)
      [2, 15, 50, 34, 37, 55]
      >>> 
      >>> uheapq.heappush(li, 105)
      >>> print(li)
      [2, 15, 50, 34, 37, 55, 105]
      >>> 
      >>> uheapq.heappop(li)
      2
      >>> print(li)
      [15, 34, 50, 105, 37, 55]
      >>> 



函数
------------------------------   

"""



def heappush(heap, item):
   """
   将item载入heap中
   """
   pass

def heappop(heap):
   """
   从 heap 中提取首项，并返回,若堆为空，则引发Index错误
   """
   pass

def heapify(x):

   """
   将列表 x 转换为一个堆
   """
   pass