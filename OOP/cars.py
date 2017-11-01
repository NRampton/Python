class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()          # This line is vital if you're going to help __init__() find other class functions

    def display_all(self):
        print "Price: ${}".format(self.price)
        print "Speed: {}mph".format(self.speed)
        print "Fuel:", self.fuel
        print "Mileage: {}mpg".format(self.mileage)
        print "Tax: {}%".format(int(self.tax * 100))


car1 = Car(12000, 100, "Full", 33)
car2 = Car(2000, 40, "Damn near empty", 3)
car3 = Car(4500, 50, "Near full", 17)
car4 = Car(23000, 110, "Full", 22)
car5 = Car(45000, 145, "Electric", 100)
car6 = Car(200, 12, "Coal", 1)
