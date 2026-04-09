class Car:
    def __init__(self, license_plate, owner):
        self.license_plate = license_plate
        self.owner = owner
        self.status = "not parked"

    def park(self):
        self.status = "parked"
        print(f"{self.owner}'s car {self.license_plate} is now parked.")

    def leave(self):
        self.status = "not parked"
        print(f"{self.owner}'s car {self.license_plate} has left.")

    def info(self):
        print(f"{self.owner}'s car {self.license_plate} is currently {self.status}.")


class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cars = []

    def add_car(self, car):
        if len(self.cars) >= self.capacity:
            print("Parking lot full!")
        else:
            self.cars.append(car)
            car.park()

    def remove_car(self, license_plate):
        for car in self.cars:
            if car.license_plate == license_plate:
                self.cars.remove(car)
                car.leave()
                return
        print("Car not found.")

    def lot_info(self):
        for car in self.cars:
            car.info()

    def available_spots(self):
        spots = self.capacity - len(self.cars)
        print(f"Available spots: {spots}")


susan_car = Car("XYZ-123", "Susan")
susan_car.park()
susan_car.info()
susan_car.leave()
susan_car.info()

bill_car = Car("ABC-456", "Bill")
bill_car.park()
bill_car.info()

susan_car.status = "not parked"
bill_car.status = "not parked"

lot = ParkingLot(2)
lot.add_car(susan_car)
lot.add_car(bill_car)
lot.lot_info()
lot.available_spots()

ron_car = Car("RON-789", "Ron")
lot.add_car(ron_car)

lot.remove_car("XYZ-123")
lot.lot_info()
lot.available_spots()

lot.add_car(ron_car)
