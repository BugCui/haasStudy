#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File       :    main.py
@Description:    播报音箱
@Date       :    2021年09月28日
@Author     :    ethan.lcz
@version    :    1.0.3
'''
import iot
import http
import ujson as json
from speech_utils import *
import time
import netmgr as nm

# 语音播放相关的音频资源文件定义
resDir = "/data/pyamp/resource/"
tonepathConnected = "fs:" + resDir + "connected.wav"
tonepathPowerOn = "fs:" + resDir + "poweron.wav"

# 物联网平台相关的key和serect定义
productKey     = "xx"
deviceName     = "xx"
deviceSecret   = "xx"

on_request = False
on_play = False
iot_connected = False

# 等待Wi-Fi成功连接到路由器
def get_wifi_status():
   nm.init()
   wifi_connected = nm.getStatus()

   while True :
      if wifi_connected == 5:
         break
      else:
         wifi_connected = nm.getStatus()
         time.sleep(0.5)
   time.sleep(5)
   print("Wi-Fi connected")
   print('DeviceIP:' + nm.getInfo()['IP'])

# 物联网平台连接成功的回调函数
def on_connect():
    global iot_connected
    print ("on_connect called")
    iot_connected = True

# 设置service 事件接收函数（本案例是千里传音）
def on_service(data):
   global on_request, on_play
   import json
   print('****** on service ********')
   print(data)
   print(data['id'])
   print(data['param'])
   serviceid = data['id']
   data = json.loads(data['param'])

   if serviceid == "SpeechPost":
      on_request = data
   elif serviceid == "SpeechBroadcast":
      on_play = data
   else:
      pass

# 连接物联网平台
def do_connect_lk(productKey, deviceName, deviceSecret):
    global device, iot_connected, on_request, on_play
    key_info = {
        'region': 'cn-shanghai',
        'productKey': "*",
        'deviceName': "*",
        'deviceSecret': "*",
        'productSecret': "*"
    }
    # 将三元组信息设置到iot组件中
    device = iot.Device(key_info)

    # 设定连接到物联网平台的回调函数，如果连接物联网平台成功，则调用on_connect函数
    device.on('connect', on_connect)
   # 设定连接到物联网平台的回调函数，如果连接物联网平台下发控制服务请求指令，则调用on_service函数
    device.on('service', on_service)

    print ("set on_connect and on_service callback, start connect")

    # 启动连接阿里云物联网平台过程
    device.connect()
    # 等待设备成功连接到物联网平台
    while(True):
        if iot_connected:
            print("物联网平台连接成功")
            play(tonepathConnected)
            break
        else:
            print("sleep for 1 s")
            time.sleep(1)

   # 触发linkit sdk持续处理server端信息
    while(True):
        time.sleep(0.2)
        if  on_request:
            download_resource_file(on_request, resDir)
            on_request = False
        elif on_play:
            play_voice(on_play,resDir)
            on_play = False
    # 断开连接
    device.close()

if __name__ == '__main__':
   # 运行此demo前需要按照”HaaS EDU K1快速上手“的文章（https://g.alicdn.com/HaaSAI/PythonDoc/quickstart/quickstart_haasedu.html）确认HaaS EDU K1固件已经烧录此文章中的固件并且确认文章中的”HaaS EDU K1跑马灯“案例可以运行成功
   # 运行此demo之前务必保证Wi-Fi连接成功过，并且此Wi-Fi路由器/热点在设备可连接范围内，Python脚本启动之后会等待系统自动重连Wi-Fi成功后才会进行连接物联网平台的操作
   print("remote speaker demo version - 1.0.3")
   init_audio()
   play(tonepathPowerOn)
   get_wifi_status()
   do_connect_lk(productKey, deviceName, deviceSecret)