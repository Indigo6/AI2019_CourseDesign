# -*- coding: utf-8 -*-
from aip import AipFace
import base64

class FaceScan:
    def __init__(self):
        self.imageType = "BASE64"
        """ 你的 APPID AK SK """
        self.APP_ID = '16361765'
        self.API_KEY = '08eNIM7h4mcc9tPzOZaOrkR1'
        self.SECRET_KEY = 'gErwZbxYktnzwQnLVvQKT1oWLffem4EA'
        #    imagePath = 'zipai.jpg'#should be a variable

    def getAttrOfPic(self,imagePath):
        with open(imagePath, 'rb') as fp:
            image = base64.b64encode(fp.read())
        # print(type(image))
        self.client = AipFace(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        self.options = {}
        # self.options["face_field"] = "age,faceshape,beauty,landmark"
        self.options["face_field"] = "age,faceshape,beauty,landmark,gender"
        # 调用ai客户端的detect方法，这个方法返回的结果就是对人脸检测后的数据
        self.result = self.client.detect(image, self.imageType, self.options)
        #print result
        # 解析返回数据中的位置参数，获取到人脸的矩形信息
        self.beauty  = self.result['result']['face_list'][0]['beauty']
        self.shape = self.result['result']['face_list'][0]['face_shape']
        self.faceShape = self.shape['type']
        self.probability = self.shape['probability']
        self.gender = self.result['result']['face_list'][0]['gender']
        self.landMark = self.result['result']['face_list'][0]['landmark72']
        self.location = self.result['result']['face_list'][0]['location']
    def getShape(self):
        return self.faceShape
    def getLandMark(self):
        return self.landMark