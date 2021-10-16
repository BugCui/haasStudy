# * coding: UTF8 *
"""
访问和控制MicroPython内部构件
"""

def const(expr):
   """
   用于表示表达式为常量，这样编译就可以将其优化。
   该函数应按照下述说明使用::

      from micropython import const

      CONST_X = const(123)
      CONST_Y = const(2 * CONST_X + 1)

   以此方式声明的常量仍可作为全局变量从其声明的模块外部访问。
   另一方面，若某常量以下划线开始，则会被隐藏，则该常量无法作为全局变量访问，且在执行时不会占据任何内存。

   const 函数是由 MicroPython 解析器直接识别的，并作为 `micropython – 访问和控制MicroPython内部构件` 模块的一部分提供，
   因此可通过以上模式编写在 CPython 和 MicroPython 下运行的脚本。

   """
   pass

def opt_level(level):
   """
   若level给定，则该函数为后续脚本编译设置优化级别，并返回 None 。若未给定level则返回当前的优化级别
   """
   pass

def alloc_emergency_exception_buf(size):
   """
   为紧急异常缓冲区（适宜大小为100字节）分配RAM的 size 字节。


   当正常的RAM分配失败时（如在中断处理程序中），缓冲区用来创建异常，因此在此情况下提供有用的回溯信息。
   使用该函数的较好方法为将其置于主脚本的开始，然后紧急异常缓冲区将会为其后所有代码激活。
   """
   pass

def mem_info(verbose):
   """
   打印关于当前占用内存的信息。若给定 *verbose* 参数，则打印附加信息。


   所打印的信息与实现相关，但当前包含存储栈和堆的使用量。
   在详细模式下会打印整个堆，并标明指示哪些已占用，哪些尚可用。
   """
   pass

def qstr_info(verbose):
   """
   打印关于当前interned字符串的信息。若给定 verbose 参数，则打印附加信息。


   所打印的信息与实现相关，但当前包含interned字符串和RAM使用量。
   在详细模式下会打印所有RAM-interned字符串的名称。
   """
   pass

def stack_use():
   """
   返回一个代表使用中的当前堆数量。
   
   
   该数值的绝对值并没有什么用处，但是这一数值应用于计算在不同点上堆使用的不同。
   """
   pass

def heap_lock():
   """
   锁定堆。锁定后无法进行内存分配，若试图执行任何堆分配，会引发 MemoryError。
   """
   pass

def heap_unlock(x):
   """
   解锁堆。heap_lock/heap_unlock 这两个函数可嵌套。
   heap_lock() 可在一行中调用多次，锁定深度将会增加，且 heap_unlock() 必须调用同样次数，以使堆重新可用。
   """
   pass

def kbd_intr(chr):
   """
   设置会引发 KeyboardInterrupt 异常的字符。


   在脚本执行中，其默认值为3，与Ctrl-C相对应。传递-1给此函数将禁用的捕捉，传递3将恢复。
   该函数可用于在传入的字符流中捕捉ctrl-c（该字符流常用于REPL），以防止该流被用于其他目的。
   """
   pass

def schedule(func, arg):
   """
   将执行的函数调度为 “非常快速”。
   该函数传递arg值作为其唯一参数。“非常快速” 意味着运行时间将尽其所能尽早执行该函数，假定运行尽可能高效，以下条件依然有效：

   - 预定函数不会抢占另一预定函数。
   - 预定函数总在 “操作码之间” 执行，也就意味着所有基本Python操作（例如添加一个列表）都确保为极小的。
   - 给定端口可能会定义“临界区”，预定函数不会在该区域中执行。函数可能在临界区内预定，但函数只在退出该区域后才会执行。
     临界区一个例子即抢占中断处理程序（一个IRQ）。
   
   该函数可用来从抢占IRQ中预定回调。这样的IRQ对IRQ（例如，堆可能被锁定）中运行的代码进行了限制，并预定一个稍后会回调的函数能够接触这些限制。

   有一个用来存放预定函数的堆栈，若堆栈已满，则 schedule 会引发 RuntimeError。

   示例调度如下::

      def callback(arg):
      global done
      try:
         for i in range(100):
               micropython.schedule(lambda x: x, None)
      except RuntimeError:
         print("RuntimeError")
      done = True


      done = False
      micropython.schedule(callback, None)
      while not done:
         pass
   """
   pass
  