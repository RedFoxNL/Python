class Vehicle:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.target_location = (-1, -1)

    def pickup(self, passenger):
        self.pickup_location = passenger.location
        self.target_location = passenger.target_location

# class Taxi
class Taxi(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)
        pass

# class Minibus
class Minibus(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)
        pass

class TaxiCompany:
    def __init__(self):
        self.vehicles = []
        self.assignments = {} # k,v = (vehicle_id, passenger_name)

    def register(self, vehicle):
        self.vehicles.append(vehicle)

    def request_pickup(self, passenger):
        self.reguest_pickup = {}
        self.schedule_vehicle(passenger)
        if self.schedule_vehicle(passenger) == "Taxi" or self.schedule_vehicle(passenger)=="Minibus":
            self.reguest_pickup[passenger] = self.schedule_vehicle(passenger)
            if Vehicle.pickup(passenger)== True:
                return True
        return False

    def schedule_vehicle(self, passenger):
        for v in self.vehicles:
            if (v.target_location == (-1,-1) and 
                abs(v.location[0] - passenger.location[0]) < 10 and
                abs(v.location[1] - passenger.location[1]) < 10):
                if (passenger.nr_of_people <= 2 and isinstance(v, Taxi)) or (passenger.nr_of_people > 2 and isinstance(v, Minibus)):
                    return v


class Passenger:
    def __init__(self, name, nr_of_people, location, target_location):
        self.name = name
        self.nr_of_people = nr_of_people
        self.location = location
        self.target_location = target_location

# main
p1 = Passenger('John', 1, (4,4), (5,0))
p2 = Passenger('Mary', 1, (5,5), (6,0))
p3 = Passenger('Ann',  4, (2,2), (7,0))
p4 = Passenger('Paul', 4, (11,3), (7,0))
p5 = Passenger('Sue',  4, (3,8), (7,0))

# your code
tc = TaxiCompany()
taxione = Taxi(1,1)
taxitwo = Taxi(2,2)
mbone = Minibus(0,0)
mbtwo = Minibus(1,1)
tc.register(taxione)
tc.register(taxitwo)
tc.register(mbone)
tc.register(mbtwo)

tc.request_pickup(p1)
