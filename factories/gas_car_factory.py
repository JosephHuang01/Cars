from factories.gas_car_assembly_line import GasCarAssemblyLine
from factories.gas_tank_factory import GasTankFactory
    
class GasCarFactory():
    def __init__(self):
        self.gas_car_assembly_line = GasCarAssemblyLine()
        self.gas_tank_factory = GasTankFactory()

    def build_gas_car(self, build_specification):
        gas_car_model = self.gas_car_assembly_line.assemble_car_model(build_specification)
        gas_tank = self.gas_tank_factory.build_gas_tank(build_specification.gas_tank_capacity)
        self.gas_car_assembly_line.add_gas_tank(gas_tank)
        return gas_car_model