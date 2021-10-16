# * coding: UTF8 *
"""

=================================================================================================

"""

def Pin(id, mode=-1, pull=-1, *, value):
   """
   访问与给定 id 相关联的外围引脚（GPIO引脚）。

   :param id(int): 必选参数，GPIO管脚索引号，具体可用数值请参考硬件手册。

   :param mode(int): 必选参数，指定引脚模式，可选值为下列之一：

      - Pin.IN - 引脚配置为输入。若将之视为输出，则引脚会处于高阻抗状态。
      - Pin.OUT - 引脚配置为（常规）输出。
      - Pin.OPEN_DRAIN - 引脚配置为开漏输出。

   :param pull(int): 可选参数，若引脚与一个（弱）电阻相连，可选值为下列之一：

      - None - 无上拉或下拉电阻。
      - Pin.PULL_UP - 启用上拉电阻。
      - Pin.PULL_DOWN - 启用下拉电阻。

   :returns: Pin 类句柄
   :raises ValueError: EINVAL
   """
   pass


def init(mode=-1, pull=-1, *, value):
   """
   使用给定参数将引脚重新初始化。只有指定参数将被设置，其余的外围引脚状态将保持不变。更多参数细节，请参见构造函数文件。

   :param 空:
   :returns: None
   """
   pass


def value(x):
   """
   该方法允许设置并获取引脚值，这取决于是否提供了参数 x。

   如果没有提供参加，则该方法获取引脚的数字逻辑电平，分别返回0或1对应的低电压信号和高电压信号。该方法的行为取决于引脚的模式:

      - Pin.IN - 该方法返回目前在引脚上出现的实际输入值。
      - Pin.OUT - 该方法的行为和返回值未定义。
      - Pin.OPEN_DRAIN - 若该引脚在“0”状态下，则该方法的行为和返回值未定义。否则，若该引脚在“1”状态下，该方法返回目前在引脚上出现的实际输入值。

   如果提供了参数值，则该方法设置引脚的数字逻辑电平。参数 x 可为任何可以转换成布尔值的参数。 若转换为 True ，则该引脚设置为状态“1”，否则引脚为状态“0”。
   该方法的行为取决于引脚的模式：

      - Pin.IN - 该值储存在引脚的输出缓冲区中。引脚状态不变，始终为高阻抗状态。当它更改为 Pin.OUT 或 Pin.OPEN_DRAIN 模式时，该储存值将在引脚上激活。
      - Pin.OUT - 输出缓冲区立即设置为给定值。
      - Pin.OPEN_DRAIN - 若该值为“0”，引脚则被设置为低电压状态。否则引脚设置为高阻抗状态。


   :param x: 输出值 或 None  
   :returns: None(提供了参数) 或 int 值(未提供参数）
   """
   pass


def off():
   """
   向管脚写入0数值（低电平）

   :param 空:
   :returns: None
   """
   pass

def on():
   """
   向管脚写入1数值（搞电平）

   :param 空:
   :returns: None
   """
   pass


def enable():
   """
   允许IRQ中断

   :param 空:
   :returns: None
   """
   pass


def disable():
   """
   禁止IRQ中断

   :param 空:
   :returns: None
   """
   pass


def irq(handler, trigger, wake=None):
   """
   配置一个中断处理程序，当引脚的触发器源处于激活状态时，调用该程序。


   若引脚模式为 Pin.IN， 则触发器源为引脚上的外部值。 若引脚模式为 Pin.OUT，则触发器源为引脚上的输出缓冲区。 


   若引脚模式为 Pin.OPEN_DRAIN，

      - 状态为“0”时，触发器源为输出缓冲区；
      - 状态为“1”时，触发器源为外部引脚值。

   :param handler: 是中断触发时所调用的可选函数
   :param trigger: 配置可产生中断的事件。可选值为:

      - Pin.IRQ_FALLING 下降沿上的中断
      - Pin.IRQ_RISING 上升沿上的中断
      - Pin.IRQ_LOW_LEVEL 低电平上的中断
      - Pin.IRQ_HIGH_LEVEL 高电平上的中断
      这些值可在多个事件中同时进行“或”运算。
   :param wake: 选择电源模式，在该模式下中断可唤醒系统。（HaaS硬件不支持该参数）
      可选值为：

      - machine.IDLE
      - machine.SLEEP
      - machine.DEEPSLEEP
      这些值可同时进行“或”运算，以使引脚在多种电源模式下生成中断。

   :returns: None
   """
   pass



