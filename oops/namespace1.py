class chai:
    origin="India"
    
print(chai.origin)

chai.isHot=True
print(chai.isHot)

#creating object from class chai
#if we change object it will not change class
masala=chai()
print(f"Masala {masala.origin}")
print(f"Masala { masala.isHot}")
masala.isHot=False