from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, vehicle_id, license_plate, owner_name):
        self.vehicle_id = vehicle_id
        self.__license_plate = license_plate
        self.__owner_name = owner_name

    def get_license_plate(self):
        return self.__license_plate

    def get_owner_name(self):
        return self.__owner_name

    def display(self):
        print(f"ID: {self.vehicle_id}, Plate: {self.__license_plate}, Owner: {self.__owner_name}")

    def calculate_parking_fee(self, hours):
        return 0


class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required=True):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats=4):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car  → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive=True):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV  → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity=10):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck→ ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}")

    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size
        self.__occupied = False
        self.__vehicle = None

    def assign_vehicle(self, vehicle):
        if self.__occupied:
            return False
        if isinstance(vehicle, Bike) and self.size not in ["S", "M", "L", "XL"]:
            return False
        if isinstance(vehicle, Car) and self.size not in ["M", "L", "XL"]:
            return False
        if isinstance(vehicle, SUV) and self.size not in ["L", "XL"]:
            return False
        if isinstance(vehicle, Truck) and self.size != "XL":
            return False

        self.__vehicle = vehicle
        self.__occupied = True
        return True

    def remove_vehicle(self):
        if not self.__occupied:
            return None
        v = self.__vehicle
        self.__vehicle = None
        self.__occupied = False
        return v

    def get_vehicle(self):
        return self.__vehicle

    def is_occupied(self):
        return self.__occupied

    def show_status(self):
        if self.__occupied:
            print(f"Spot {self.spot_id} ({self.size}): Occupied → {self.__vehicle.__class__.__name__} ({self.__vehicle.get_license_plate()})")
        else:
            print(f"Spot {self.spot_id} ({self.size}): Empty")


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def park_vehicle(self, vehicle):
        for s in self.spots:
            if not s.is_occupied():
                if s.assign_vehicle(vehicle):
                    print(f"{vehicle.__class__.__name__} ({vehicle.get_license_plate()}) parked at Spot {s.spot_id}")
                    return True
        print(f"No suitable spot available for {vehicle.__class__.__name__} ({vehicle.get_license_plate()})")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for s in self.spots:
            if s.get_vehicle() == vehicle:
                s.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"{vehicle.__class__.__name__} ({vehicle.get_license_plate()}) removed from Spot {s.spot_id}")
                print(f"Parking Fee = ₹{fee}")

                print("Select Payment Method: 1. Cash 2. Card 3. UPI")
                choice = int(input("Enter choice: "))
                if choice == 1:
                    CashPayment().process_payment(fee)
                elif choice == 2:
                    CardPayment().process_payment(fee)
                elif choice == 3:
                    UPIPayment().process_payment(fee)
                else:
                    print("Invalid payment method")
                return fee
        print("Vehicle not found in parking lot.")
        return 0

    def show_spots(self):
        print("\nParking Status:")
        for s in self.spots:
            s.show_status()


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} in cash")


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using UPI")


if __name__ == "__main__":
    lot = ParkingLot("CityMall Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "M"))
    lot.add_spot(ParkingSpot(4, "L"))
    lot.add_spot(ParkingSpot(5, "XL"))
    print(f"Parking Lot Created: {lot.name} Total Spots Added: {len(lot.spots)}")

    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

    print("Vehicles Created:")
    bike1.display()
    car1.display()
    suv1.display()
    truck1.display()

    lot.park_vehicle(bike1)
    lot.park_vehicle(car1)
    lot.park_vehicle(suv1)
    lot.park_vehicle(truck1)
    lot.show_spots()

    lot.unpark_vehicle(car1, hours=3)

    lot.show_spots()

