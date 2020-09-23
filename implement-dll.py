from ctypes import *
lib = cdll.LoadLibrary(
    "/home/raju/Downloads/HelloWorld/bin/Debug/netcoreapp3.1/HelloWorld.dll")
print(lib.Add(10, 20))
