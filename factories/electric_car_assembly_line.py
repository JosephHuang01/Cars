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

# class AssemblyLine():
#     def __init__(self):
#         self.assembled_model = ElectricCar('', '', '')
#         self.reset_process()

#     def reset_process(self):
#         self.assembled_model

#     def assembled_car_model(self, make, model, year):
#         self.assembled_model.make = make
#         self.assembled_model.model = model
#         self.assembled_model.year = year
#         return self
    
#     def include_battery(self, capacity, kwh_used_per_mile):
#         self.assembled_model = Battery(capacity, kwh_used_per_mile)

#     def build_model(self):
#         finished_model = self.assembled_model
#         self.reset_process()
#         return finished_model

# class IncludeBattery(Battery):
#     def __init__(self, capacity, kwh_used_per_mile=0.2):
#         super().__init__(capacity, kwh_used_per_mile)