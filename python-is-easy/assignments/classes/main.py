'''
Homework assignment for the 'Classes' topic in 'Python is easy' course by Pirple.

Written be Ed Yablonsky.
'''

import sys

'''
Represents any vehicle
'''
class Vehicle:
    def __init__(self):
        self.make = 'unknown'
        self.model = 'unknown'
        self.needsMaintenance = False
        self.tripsSinceMaintenace = 0
        self.weight = 1.0
        self.year = 0

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setYear(self, year):
        self.year = year

    def setWeight(self, weight):
        self.weight = weight

    def Print(self):
        print('Make:  ', self.make)
        print('Model: ', self.model)
        print('Year:  ', self.year)
        print('Weight:', self.weight)
        print('Trips: ', self.tripsSinceMaintenace)
        if self.needsMaintenance:
            print('Needs maintenance')
        else:
            print('No maintenance needed')

    def Repair(self):
        self.needsMaintenance = False
        self.tripsSinceMaintenace = 0

'''
Represents a car vehicle
'''
class Cars(Vehicle):
    def __init__(self):
        super().__init__()
        self.isDriving = False

    def Drive(self):
        self.isDriving = True

    '''
    Counts trips to know when the car needs to be repaired
    '''
    def Stop(self):
        if self.isDriving:
            self.tripsSinceMaintenace += 1
            if self.tripsSinceMaintenace >= 100:
                self.needsMaintenance = True
        self.isDriving = False

'''
Represents a plane vehicle
'''
class Planes(Vehicle):
    def __init__(self):
        super().__init__()
        self.isFlying = False

    '''
    Rejects to fly when the plane needs maintenance
    '''
    def Fly(self):
        if self.needsMaintenance:
            self.isFlying = False
            print("Can't fly until it's repaired", file=sys.stderr)
        else:
            self.isFlying = True
        return self.isFlying

    '''
    Counts trips to know when the plane needs to be repaired
    '''
    def Land(self):
        if self.isFlying:
            self.tripsSinceMaintenace += 1
            if self.tripsSinceMaintenace >= 100:
                self.needsMaintenance = True
        self.isFlying = False

'''
The main routine
'''

vehicles = [] # Hold all the vehicles

car = Cars()
vehicles.append(car)
car.setMake('Heavy Motors');
car.setModel('Bull');
car.setYear(1999);
car.setWeight(3.0);
for i in range(0, 50):
    car.Drive()
    car.Stop()

car = Cars()
vehicles.append(car);
car.setMake('LuxurZ');
car.setModel('Silver');
car.setYear(2001);
car.setWeight(1.5);
for i in range(0, 100):
    car.Drive()
    car.Stop()

car = Cars()
vehicles.append(car);
car.setMake('Nebula');
car.setModel('Model Y');
car.setYear(2020);
car.setWeight(1.35);
for i in range(0, 101):
    car.Drive()
    car.Stop()
car.Repair()
for i in range(0, 10):
    car.Drive()
    car.Stop()

plane = Planes()
vehicles.append(plane)
plane.setMake("EveryoneCanFly")
plane.setModel("Sparrow")
plane.setYear(2000)
plane.setWeight(1.0)
for i in range(0, 102):
    plane.Fly()
    plane.Land()

for vehicle in vehicles:
    vehicle.Print()
