class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price < 10000:
            self.tax = str(0.12)
        else:
            self.tax = str(0.15)
    def display_All(self):
        print self.price + " " + self.speed + " " +  self.fuel + " " +  self.mileage + " " + self.tax

Car1 = Car("2000", "35 mph", "half-full", "60 mpg", "")
Car2 = Car("5000", "35 mph", "half-full", "60 mpg", "")
Car3 = Car("3000", "35 mph", "half-full", "60 mpg", "")
Car4 = Car("2050", "35 mph", "half-full", "60 mpg", "")
Car5 = Car("22000", "35 mph", "half-full", "60 mpg", "")
Car6 = Car("27000", "35 mph", "half-full", "60 mpg", "")
Car3.display_All()