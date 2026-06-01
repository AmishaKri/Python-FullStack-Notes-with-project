#Inheritence and composition

class BaseChai:
    def __init__(self, type_):
        self.type=type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai...")
        
class Masalachai(BaseChai):  #inheritance
    def addSpices(self):
        print("addng masalas")
      
class ChaiShop:
    chaiCls=BaseChai  #reference of baseclass
    
    def __init__(self):  
        self.chai=self.chaiCls("Regular")
        
    def serve(self):
        
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
        
class fancyshop(ChaiShop):  #composition
    chaiCls=Masalachai
    
    
shop=ChaiShop()
fancy=fancyshop()

shop.serve()
fancy.serve()
#fancy.chaiCls.addSpices()  #error
fancy.chai.addSpices()

#MRO  ....Method Resolution Order