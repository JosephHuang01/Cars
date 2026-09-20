from components.car import Car
from components.electric_car import ElectricCar

class AssemblyLine():
    def __init__(self):
        self.assembled_model = Car('', '', 0)
        
    def assemble_car_model(self, make, model, year):
        self.assembled_model = Car(make, model, year)
        return self.assembled_model

class ElectricCarAssemblyLine(AssemblyLine):
    def __init__(self):
        super().__init__()
    
    def assemble_car_model(self, build_specification):        
        self.assembled_model = ElectricCar(
            build_specification.make,
            build_specification.model,
            build_specification.year)
        return self.assembled_model
    
    def replace_battery(self, battery):
        self.assembled_model.replace_battery(battery)