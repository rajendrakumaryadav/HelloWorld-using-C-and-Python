import clr  
#Adding reference to class library!  
clr.AddReference('.\\HelloWorld.dll')
 
#importing specific class from this namespace, here!  
import Class1
wrapper = Class1()
# calling functions using class name, since these all are static!  
def pmethod1():  
     str = wrapper.Message()  
  
def pmethod2():  
     inte = wrapper.method2()  
  
def pmethod3():  
    doub= wrapper.method3()  
