class Vehicle:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.target_location = (-1, -1)

    def pickup(self, passenger):
        self.pickup_location = passenger.location
        self.target_location = passenger.target_location

class TaxiCompany:
    def __init__(self):
        self.vehicles = []
        self.assignments = {} # k,v = (vehicle_id, passenger_name)

    def register(self, vehicle):
        self.vehicles.append(vehicle)

    def request_pickup(self, passenger):
        v = self.schedule_vehicle(passenger)
        if v:
            self.assignments[v.id] = passenger.name
            v.pickup(passenger)
            return True
        else:
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

class Taxi(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)

class Minibus(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)

# main
tc = TaxiCompany()
t1 = Taxi('taxi-one', (1, 1))
t2 = Taxi('taxi-two', (2, 2))
m1 = Minibus('minibus-one', (0, 0))
m2 = Minibus('minibus-two', (1, 1))
tc.register(t1)
tc.register(t2)
tc.register(m1)
tc.register(m2)
p1 = Passenger('John', 1, (4,4), (5,0))
p2 = Passenger('Mary', 1, (5,5), (6,0))
p3 = Passenger('Ann', 4, (2,2), (7,0))
p4 = Passenger('Paul', 4, (11,3), (7,0))
p5 = Passenger('Sue', 4, (3,8), (7,0))