# 🧰 haasStudy「HaaS 开发板学习」


> Haas 是阿里巴巴基于AliOS 操作系统推出的一款板子，类似于树莓派，只不过是运行AliOS操作系统。

📀 [关于AliOS](https://www.aliyun.com/product/aliosthings?spm=a2cpu.b16145223.0.0.595660b1oZ8mUX)

📱 [关于Haas](https://haas.iot.aliyun.com)

📄 [官网教程](https://g.alicdn.com/HaaSAI/PythonDoc/demos/index.html#ii-ai)

<br>

1. remote_speaker「语音播报音响」

    bilibili 入口地址: [支付到账十亿元](https://www.bilibili.com/video/BV17q4y157AY?share_source=copy_web)

2. ai_demo「AI图片识别」
    
    ① 目标检测

    输入图片：<a href="https://github.com/BugCui/haasStudy/blob/main/ai_demo/solutions/ai_demo/resource/test2.jpeg"> test2.jpeg </a>

    识别结果：laptop
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

    输入图片：<a href="https://github.com/BugCui/haasStudy/blob/main/ai_demo/solutions/ai_demo/resource/expression.png">expression.png</a>

    识别结果：happiness

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

    ③ 文字识别

    输入图片：<a href="https://github.com/BugCui/haasStudy/blob/main/ai_demo/solutions/ai_demo/resource/font.png">font.png</a>

    识别结果：也 行。（aha，是姿势不对么~）

    ```
    -------------------Welcome HaasAI MicroPython--------------------
    -----ml ucloud RecognizeCharacter demo start-----
  
    results size: 3
    0text: 也
    0probability: 0.9
    0text left: 492
    0text angle: 0
    0text top: 213
    0text height: 84
    0text: width:119
    [ 216.423]<E>HAAS_ML_CLOUD text: 也

    [ 216.423]<E>HAAS_ML_CLOUD probability: 0.9

    [ 216.423]<E>HAAS_ML_CLOUD text area: left: 213, top: 492, weight: 119, height: 84

    1text: 00
    1probability: 0.91
    1text left: 208
    1text angle: 0
    1text top: 397
    1text height: 22
    1text: width:25
    [ 216.424]<E>HAAS_ML_CLOUD text: 00

    [ 216.424]<E>HAAS_ML_CLOUD probability: 0.9

    [ 216.424]<E>HAAS_ML_CLOUD text area: left: 397, top: 208, weight: 25, height: 22

    2text: /行
    2probability: 0.7
    2text left: 251
    2text angle: -3
    2text top: 164
    2text height: 297
    2text: width:652
    [ 216.425]<E>HAAS_ML_CLOUD text: /行

    [ 216.425]<E>HAAS_ML_CLOUD probability: 0.7

    [ 216.425]<E>HAAS_ML_CLOUD text area: left: 164, top: 251, weight: 652, height: 297

    bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\
    ```
