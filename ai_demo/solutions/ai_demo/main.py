# 智能物体识别

from minicv import ML

print("-------------------Welcome HaasAI MicroPython--------------------")
print("-----ml ucloud ObjectDet demo start-----")
OSS_ACCESS_KEY = "*"
OSS_ACCESS_SECRET = "*"
OSS_ENDPOINT = "*"
OSS_BUCKET = "*"
ml = ML()
ml.open(ml.ML_ENGINE_CLOUD)
ml.config(OSS_ACCESS_KEY, OSS_ACCESS_SECRET, OSS_ENDPOINT, OSS_BUCKET,"NULL")
ml.setInputData("/data/pyamp/resource/test2.jpeg")
ml.loadNet("ObjectDet")
ml.predict()
responses_value = bytearray(10)
ml.getPredictResponses(responses_value)
# print(responses_value)
ml.unLoadNet()
ml.close()
print("-----ml ucloud ObjectDet demo end-----")

