#Non local vs Global scope
chaiType='ginger'
def updateOrder():
    chaiType='Elaichi'
    
    def kitchen():
        # nonlocal chaiType  # inner to inner
        global chaiType  # ginger for global variable access
        chaiType='Kesar'
        print('After kitchen update', chaiType) #kesar
        
    kitchen()
    print('After kitchen update', chaiType) #kesar
updateOrder()
