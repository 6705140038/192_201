class Vehicle:
    def __init__(self, make: str, model: str, plate: str):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False
    def rent(self):
        """Mark the vehicle as rented."""
        self.is_rented = True
    def return_vehicle(self):
        """Mark the vehicle as available."""
        self.is_rented = False
    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}]"
class Renter:
    def __init__(self, name: str, license_no: int):
        # Setting values through properties triggers validation checks immediately
        self.name = name
        self.license_no = license_no
        self.rented = []
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value
    @property
    def license_no(self):
        return self._license_no
    @license_no.setter
    def license_no(self, value: int):
        if value <= 0:
            raise ValueError("License number must be a positive number.")
        self._license_no = value
class ElectricCar(Vehicle):
    def __init__(self, make: str, model: str, plate: str, battery_kwh: float):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh
    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}] - Battery: {self.battery_kwh} kWh"
class Motorbike(Vehicle):
    def __init__(self, make: str, model: str, plate: str, engine_cc: int):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc
    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}] - Engine: {self.engine_cc} cc"