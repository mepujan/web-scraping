import weakref, gc

class A:
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return str(self.value)
    
a = A(10)
# Create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a  #Doesnot create a reference
print(d['primary']) #fetch the object if it is still alive

del a  #remove one reference
print(gc.collect())  #run garbage collection right away

print(d['primary'])  #entry was automatically removed