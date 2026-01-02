class Vehicle:
    def __init__(self,make, model):
        self.make = make       
        self.model = model     

    def get_info(self):
        return f"марка:{self.make} и модель:{self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)   
        self.fuel_type = fuel_type      

    def get_info(self):
        return f"{super().get_info()} и тип топлива: {self.fuel_type}"
