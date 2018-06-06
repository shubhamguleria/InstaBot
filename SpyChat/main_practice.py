class car():
    name="zoom"
    brand="bmw"
    model_type="sedan"
    
    def __init__(self, model, color):
        self.model=model
        self.color=color

       
car1=car(2,"Metal Black")            

print(car1.color)
print(car1.name)
    
    