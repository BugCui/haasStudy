# * coding: UTF8 *
"""

=================================================================================================

"""

def uploadFile(key,secret,endPoint,bucketName,filePath):
   """
   上传资源文件

   :param key: "Your-Access-Key"
   :param secret: "Your-Access-Secret"
   :param endPoint: "Your-OSS-Endpoint"
   :param bucketName: "Your-OSS-Bucket"
   :param filePath: "文件路径"
   :returns: !0: 传成功后对应的url，0: 失败
   :raises OSError: EINVAL
   """
   pass

def uploadContent(key,secret,endPoint,bucketName,fileContent):
   """
   上传资源文件内容

   :param key: "Your-Access-Key"
   :param secret: "Your-Access-Secret"
   :param endPoint: "Your-OSS-Endpoint"
   :param bucketName: "Your-OSS-Bucket"
   :param fileContent: "文件内容"
   :returns: !=0: 传成功后对应的url，0: 失败
   :raises OSError: EINVAL
   """
   pass

