__author__ = 'cnzhao'
from glacier.message.msgHead_pb2 import MessageHead
from glacier.message.msgDefine_pb2 import *

head = MessageHead()
head.appId = System
head.name = "1111"

inputStr = head.SerializeToString()

outputHead = MessageHead()
outputHead.ParseFromString(inputStr)

print(outputHead)
