# 🧰 haasStudy「HaaS 开发板学习」


> Haas 是阿里巴巴基于AliOS 操作系统推出的一款板子，类似于树莓派，只不过是运行AliOS操作系统。

📀 [关于AliOS](https://www.aliyun.com/product/aliosthings?spm=a2cpu.b16145223.0.0.595660b1oZ8mUX)

📱 [关于Haas](https://haas.iot.aliyun.com)

<br>

1. remote_speaker「语音播报音响」

    bilibili 入口地址: [支付到账十亿元](https://www.bilibili.com/video/BV17q4y157AY?share_source=copy_web)

2. ai_demo「AI图片识别」
    
    ① 目标检测

    输入图片：<a href="https://github.com/BugCui/haasStudy/blob/main/ai_demo/solutions/ai_demo/resource/test2.jpeg"> test2.jpeg </a>

    输出识别内容：laptop
    ```
    -------------------Welcome HaasAI MicroPython--------------------
    -----ml ucloud ObjectDet demo start-----
    ......

    objectdet describeInstances returned:
    error code: 
    object num:1
    object height:800
    object width:800
    object score:0.616
    object type:laptop # 识别出的物体类型
    object boxes.x:38
    object boxes.y:70
    object boxes.w:714
    object boxes.h:734
    [  62.101]<E>HAAS_ML_CLOUD type: laptop, Score: 0.6, x: 38, y: 70, w: 714, h: 734

    -----ml ucloud ObjectDet demo end-----
    ```

    ② 表情识别

    输入图片：

    输出识别表情：happiness

    ```
    -------------------Welcome HaasAI MicroPython--------------
    -----ml ucloud RecognizeExpression demo start-----

    expression:happiness # 识别表情
    face probablility:0.999283
    x:872453104
    y:872453320
    w:4
    h:872453248
    expression:happiness
    [ 101.791]<E>HAAS_ML_CLOUD Recognize expression result:

    [ 101.791]<E>HAAS_ML_CLOUD type: happiness, probability: 1.0

    bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    -----ml ucloud RecognizeExpression demo end-----

    ```