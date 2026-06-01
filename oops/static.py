class chaiUtils:
    @staticmethod
    def chaiStaus(cupLeft):
        if cupLeft==0:
            return "Sorry, chai over"
        return "chai is ready"
    
    def  cleanIngredients(text):
        return [item.strip() for item in text.split(",")]
    
raw="water, milk, black tea"
print(chaiUtils.cleanIngredients(raw))