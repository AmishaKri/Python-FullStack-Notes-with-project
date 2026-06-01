#code duplication, excplicit call, super()

class Chai:
    def __init__(self, type_, strength):
        self.type=type_
        self.strength=strength
        
# class GingerChai(Chai):
#     def __init__(self, type_, strength, spiceLevel):
#         self.type=type_
#         self.strength=strength   
#         self.spiceLevel=spiceLevel   


class GingerChai(Chai): #explicitly
    def __init__(self, type_, strength, spiceLevel):
       Chai.__init__(self, type_, strength, spiceLevel)  
       self.spiceLevel=spiceLevel 
       

class GingerChai(Chai):
     def __init__(self, type_, strength, spiceLevel):
       super().__init__(self, type_, strength, spiceLevel)  
       self.spiceLevel=spiceLevel


#MRO
class A:
    label="label a" 

class B(A):
    label="label b" 
    
class C(B):
    label="c"
    
class D(C, B):
    pass

cup=D()
print(cup.label)
print(D.__mro__)