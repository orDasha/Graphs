class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle(color="blue", doors=5, tires=4, vtype="car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())

my_set:set = {1, 2, 3, 2}
my_list = [1, 3, 5]

for i in my_set:
    print(i)
    i += 1

def gd(a, b):
    if b==0:
        return a
    return gd(b, a % b)
print(gd(225, 150))

# branch master


