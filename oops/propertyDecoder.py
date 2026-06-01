class chaiOrder:
    def __init__(self, tea_type , sweetness, size):  #constructor
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size
        
        @classmethod
        def from_dict(cls, data):
            return cls(data['type'], data['sweetness'], data['size'])
        
        def from_string(cls, string):
            type, sweetness, size = string.split('-')
            return cls(type, sweetness, size)
        
        
order1=chaiOrder.from_dict({"type":"Masala Chai", "sweetness":3, "size":150})
order2=chaiOrder.from_string("Masala Chai-3-150")

class chaiUtility:
    @staticmethod
    def get_chai_order(tea_type, sweetness, size):
        return chaiOrder(tea_type, sweetness, size)