__author__ = 'cnzhao'
from Person_pb2 import Person
p = Person()
p.id = 3
p.str = "111"

str = p.SerializeToString()

print(str)

po = Person()
po.ParseFromString(str)

print(po.id)
print(po.str)