from factories.electric_car_assembly_line import ElectricCarAssemblyLine
from factories.battery_factory import BatteryFactory

class ElectricCarFactory():
    def __init__(self):
        self.electric_car_assembly_line = ElectricCarAssemblyLine()
        self.battery_factory = BatteryFactory()
        
    def build_electric_car(self, build_specification):
        electric_car_model = self.electric_car_assembly_line.assemble_car_model(build_specification)
        battery = self.battery_factory.build_battery(build_specification.battery_capacity)
        self.electric_car_assembly_line.replace_battery(battery)
        return electric_car_model