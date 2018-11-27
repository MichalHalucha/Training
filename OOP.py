#import class from file car.py
# or """A set of classes used to represent gas and electric cars."""
#for car import Car
#import multiple class
#from car import Car, ElectricCar
#Importing an Entire Module
#import car
#Importing All Classes from a Module
#from module_name import * (not recommended)



class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        #super().__init__(make, model, year)
        super(ElectricCar, self).__init__(make, model, year)
        #self.battery_size = 70
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
    print("This car doesn't need a gas tank!")

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

def write_file(file_name,text):
    #read mode ( 'r' ), write mode ( 'w' ), append mode ( 'a' ), read and write ('r+')
    try:
        with open(file_name, "w") as file_object:
            contents = file_object.write(text+"\n")
            contents = file_object.write(text)
            print(contents)
    except:
        print("Nie ma takiego pliku!")


def read_file(file_name):
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
            print(contents)
            #file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
            # with open(file_path) as file_object:
    except:
        print("Nie ma takiego pliku!")


if __name__ == '__main__':

    read_file("text.txt")
    write_file("text.txt","I love programming!")

    print("Main")
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_descriptive_name())
    #my_tesla.describe_battery()
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
