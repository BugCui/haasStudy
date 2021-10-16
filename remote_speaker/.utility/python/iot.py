# -*- coding: UTF-8 -*-
"""



阿里云物联网平台提供安全可靠的设备连接通信能力，支持设备数据采集上云，规则引擎流转数据和云端数据下发设备端。此外，也提供方便快捷的设备管理能力，支持物模型定义，数据结构化存储，和远程调试、监控、运维。 基于iot模块可以简单快速的使用阿里云物联网平台能力。

iot模块的主要实现是一个Device 类，通过它的构造函数获取device实例，就可以轻松设置相关回调函数和调用相关方法。阿里云物联网平台中涉及三个基本概念如下:

- 属性(prop)
    云/端双向通道

- 事件(event)
    设备端到云端的单向通道

- 服务(service)
    云端到设备端的单向通道

详细使用示例请参考主页”参考案例”中的云端连接/控制部分


"""

class Device(object):
    """

    初始化物联网平台Device类，获取device实例

    :param data(dict): data字典的key信息如下

        .. list-table::

            * - 属性
              - 类型
              - 是否必填
              - 说明
            * - deviceName
              - 字符串
              - Y
              - 物联网平台上注册的设备名称
            * - deviceSecret
              - 字符串
              - Y
              - 物联网平台上注册的deviceSecret
            * - productKey
              - 字符串
              - Y
              - 物联网平台上注册的productKey      
            * - productSecret
              - 字符串
              - 可选
              - 物联网平台上注册的productSecret
            * - region
              - 字符串
              - 可选
              - 默认值是'cn-shanghai'    

        使用示例::

            import iot

            productKey = "a1uTFk4xjko"
            productSecret = "xxxxxxx"
            deviceName  =    "mpy_001"
            deviceSecret  =   "xxxxxxxxxxxxxxx"
            key_info = {
                'region' : 'cn-shanghai' ,
                'productKey': productKey ,
                'deviceName': deviceName ,
                'deviceSecret': deviceSecret ,
                'productSecret': productSecret
            }
            device = iot.Device(key_info) 



    """

    def __init__(self,data):

        def __str_is_empty(value):
            if value is None or value == "":
                return True
            else:
                return False

        if not isinstance(data,dict):
            raise ValueError("Class Device init param must be dict")

        if not 'productKey' in data:
            raise ValueError('Device init : param must have key "productKey"')
        elif __str_is_empty(data['productKey']):
            raise ValueError("productKey wrong")

        if not 'deviceName' in data:
            raise ValueError('Device init : param must have key "deviceName"')
        elif __str_is_empty(data['deviceName']):
            raise ValueError("deviceName wrong")

        if not 'deviceSecret' in data:
            raise ValueError('Device init : param must have key "deviceSecret"')
        elif __str_is_empty(data['deviceSecret']):
            raise ValueError("deviceSecret wrong")

        if 'productSecret' in data:
            self.productSecret = data['productSecret']
        else:
            self.productSecret = ""

        if 'region' in data:
            self.region = data['region']
        else:
            self.region = "cn-shanghai"

        self.data = data

        # ret = _lk.init(region,data['productKey'],data['deviceName'],data['deviceSecret'],productSecret)
        # print("init return :")
        # print(ret)
        # _lk.register_dyn_dev()

        self._callback = {}



    # def publish(self):
    #     pass

    # def subscribe(self):
    #     pass

    # def unsubscribe(self):
    #     pass



    def on(self,event,callback):

        """
        通过这个函数，可以设置物联网平台各种事件的处理函数，函数接收两个参数分别是事件名称和事件处理函数

        :param event(str)): 需要注册的事件名称，类型是字符串

            .. list-table::

                * - 事件名称
                  - 事件说明
                * - connect
                  - 当iot设备连接到物联网平台的时候触发'connect' 事件
                * - disconnect
                  - 当连接断开时，触发'disconnect'事件
                * - props
                  - 当iot云端下发属性设置时，触发'props'事件
                * - service
                  - 当iot云端调用设备service时，触发'service'事件
                * - error
                  - 当设备跟iot平台通信过程中遇到错误时，触发'error'事件

        :param callback: 回调函数

        使用示例::

            def on_connect():
                print('linkkit is connected')
            
            device.on('connect',on_connect)

            def on_disconnect():
                print('linkkit is disconnected')

            device.on('disconnect',on_disconnect)

            def on_props(request):
                print('clound req data is %s' %(request))

            device.on('props',on_props)


            def on_service(id,request):
                print('clound req id  is %d , req is %s' %(id,request))

            device.on('service',on_service)


            def on_error(err):
                print('err msg is %s '%(err))

            device.on('error',on_error)


        """

        # if not callable(callback):
        #     raise ValueError("the 2nd param of function on must be function")

        # if (event == 'connect'):
        #     _lk.register_call_back(_lk.ON_CONNECT,callback)
        # elif (event == 'disconnect'):
        #     _lk.register_call_back(_lk.ON_DISCONNECT,callback)
        # elif (event == 'close'):
        #     _lk.register_call_back(_lk.ON_CLOSE,callback)
        # elif (event == 'error'):
        #     _lk.register_call_back(_lk.ON_ERROR,callback)
        # elif (event == 'props'):
        #     _lk.register_call_back(_lk.ON_PROPS,callback)
        # elif (event == 'service'):
        #     _lk.register_call_back(_lk.ON_SERVICE,callback)
        self._callback[event] = callback

    def connect(self):
        '''
        连接物联网平台连接函数，该函数是异步调用
        '''

        for key in self._callback:
            event = key
            callback = self._callback[key]
            print(event)
                    # if not callable(callback):
        #     raise ValueError("the 2nd param of function on must be function")

            if (event == 'connect'):
                _lk.register_call_back(_lk.ON_CONNECT,callback)
            elif (event == 'disconnect'):
                _lk.register_call_back(_lk.ON_DISCONNECT,callback)
            elif (event == 'close'):
                _lk.register_call_back(_lk.ON_CLOSE,callback)
            elif (event == 'error'):
                _lk.register_call_back(_lk.ON_ERROR,callback)
            elif (event == 'props'):
                _lk.register_call_back(_lk.ON_PROPS,callback)
            elif (event == 'service'):
                _lk.register_call_back(_lk.ON_SERVICE,callback)


        ret = _lk.init(self.region,self.data['productKey'],self.data['deviceName'],self.data['deviceSecret'],self.productSecret)
        _lk.register_dyn_dev()

        _lk.connect()

    def postProps(self,data):
        """
        上报设备属性


        :param data(dict): 字典的key信息如下

            .. list-table::

                  * - 属性
                    - 类型
                    - 是否必填
                    - 说明
                  * - params
                    - 字典
                    - Y
                    - 属性的值对应的是物联网平台的json数据                    

        使用示例::

            data = {
                'params': {
                'test_prop' : 100
                }
            }
            device.postProps(data)

        """
        if not isinstance(data, dict):
            raise ValueError("postProps func param must be dict")

        if not 'params' in data:
            raise ValueError('data must have key: "params"')
        return _lk.post_property(ujson.dumps(data['params']))



    def postEvent(self,data):
        """
        上报设备的事件

        :param data(dict): 字典的key信息如下

            .. list-table::

                  * - 属性
                    - 类型
                    - 是否必填
                    - 说明
                  * - params
                    - 字典
                    - Y
                    - 属性的值对应的是物联网平台的json数据       
                  * - id
                    - 字符串
                    - Y
                    - 事件名称，请参考物模型上定义的事件id                      

        使用示例::

            data = {
                'id': 'EventTest' ,
                'params': {
                'test_event' : 100
                }
            }
            device.postEvent(data)


        """
        if isinstance(data, dict):
            if not 'id' in data:
                raise ValueError('data must have key:  "id"')
            if not 'params' in data:
                raise ValueError('data must have key: "params"')

        else:
            raise ValueError("postEvent func param must be dict")
        return _lk.post_event(data['id'],ujson.dumps(data['params']))


    def close(self):
        '''
        关闭物联网设备节点，断开连接
        '''
        return _lk.close()

    # def do_yield(self,time):
    #     """
    #     激活物联网平台接收云端消息，并设置接收超时时间为:timeout, 单位是 ms.为了保证云端消息被接收到，执行了异步命令以后，需要循环执行这个方法，直到拿云端的返回
    #     """
    #     _lk.do_yield(time)
    #     utime.sleep_ms(time)


    # def __register_callback(self):
    #     _lk.register_call_back(1,self.__on_connect)
    #     _lk.register_call_back(3,self.__on_disconnect)
    #     _lk.register_call_back(5,self.__on_service_request)
    #     _lk.register_call_back(7,self.__on_prop_set)
    #     _lk.register_call_back(9,self.__on_thing_prop_post)
    #     _lk.register_call_back(10,self.__on_thing_event_post)


# class GateWay(object):

#     def addTopo(self):
#         pass

#     def getTopo(self):
#         pass

#     def removeTopo(self):
#         pass

#     def login(self):
#         pass

#     def logout(self):
#         pass

#     def regiestSubDevice(self):
#         pass

# def register():
    # pass









