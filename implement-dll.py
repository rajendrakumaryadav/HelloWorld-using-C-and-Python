from ctypes import *
lib = cdll.LoadLibrary(
    "./bin/Debug/netcoreapp3.1/HelloWorld.dll")
print(lib.Add(10, 20))
