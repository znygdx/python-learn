from ctypes import *
import binascii 
class TServerInfoVersion(Structure):
    _pack_  = 1
    _fields_  =  [
        ('ServerName',       c_char * 51),
        ('ServerVersion',    c_char * 51),
        ('ServerMD5',        c_char * 51)
    ]

a=TServerInfoVersion()
a.ServerName = "123"
a.ServerVersion = "222"
a.ServerMD5 = "aaa"


strinfo=binascii.b2a_hex(a)
print(strinfo)



