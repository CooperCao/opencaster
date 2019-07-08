#! /usr/bin/env python
def CRC_32(data,len):
    return 0xFFFFFFFF

try:
    import platform
    import os,sys
    from ctypes import *
    system = platform.system()
    if 'Windows' in system:
        if "64bit" == platform.architecture()[0]:
            libcrcpath = os.path.join(os.path.split(os.path.realpath(__file__))[0],"sectioncrc64.dll")
        else:
            libcrcpath = os.path.join(os.path.split(os.path.realpath(__file__))[0],"sectioncrc32.dll")
    elif 'Linux' in system:
        libcrcpath = os.path.join(os.path.split(os.path.realpath(__file__))[0],"sectioncrc.so")
    else:
        print("Error exit")
        sys.exit(1)
   
    libcrcdll = CDLL(libcrcpath)
    CRC_32 = libcrcdll.sectioncrc
    CRC_32.restype=c_uint32
except ImportError,OSError:
    print("### WRONG CRC32!!!")
    pass
