from components.car import Car
from components.gas_car import GasCar

class AssemblyLine():
    def __init__(self):        
        self.assembled_model = Car('','', 0)
        
    def assemble_car_model(self, make, model, year):
        self.assembled_model = Car(make, model, year)
        return self.assembled_model

class GasCarAssemblyLine(AssemblyLine):
    def __init__(self):
        super().__init__()
    
    def assemble_car_model(self, build_specification):        
        self.assembled_model = GasCar(
            build_specification.make, 
            build_specification.model, 
            build_specification.year)
        return self.assembled_model
    
    def add_gas_tank(self, gas_tank):
        self.assembled_model.add_gas_tank(gas_tank)