from rental import Vehicle, Renter, ElectricCar, Motorbike
def main():
    print("--- 1. Testing Vehicle & Renter Basics ---")
    car = Vehicle("Toyota", "Yaris", "1AB234")
    renter = Renter("Alice Smith", 12345)
    print(f"Initial status: {car}")
    car.rent()
    renter.rented.append(car)
    print(f"After renting: {car}")
    car.return_vehicle()
    renter.rented.remove(car)
    print(f"After returning: {car}")
    print("\n--- 2. Testing Encapsulation Checks ---")
    try:
        invalid_renter1 = Renter("", 99999)
    except ValueError as error:
        print(f"Caught invalid name error: {error}")
    try:
        invalid_renter2 = Renter("Bob Jones", -50)
    except ValueError as error:
        print(f"Caught invalid license error: {error}")
    print("\n--- 3. Testing Polymorphism (Mixed Vehicle List) ---")
    fleet = [
        Vehicle("Toyota", "Corolla", "ABC-123"),
        ElectricCar("Tesla", "Model 3", "EV-567", 75.0),
        Motorbike("Honda", "CB500", "MB-999", 500)
    ]
    for vehicle in fleet:
        print(vehicle)
if __name__ == "__main__":
    main()