from ch3day4 import carMaker

class dealerShip:
    def __init__(self, dealershipname, location, cars={}):
        self.dealershipname = dealershipname
        self.location = location
        self.cars = cars

    def __str__(self):
        return (
            f"Dealer's Name: {self.dealershipname}\n"
            f"Location: {self.location}\n\n"
            f"Cars Available:\n\n {self.cars}")
    
#     print("[This is red text")


# print("\033[92mThis is green text\033[0m")
# print("\033[94mThis is blue text\033[0m")

myCars=[]
myCars.append(carMaker("India", 2008, 1980, 1234, 50, 140))
myCars.append(carMaker("russia", 2009, 1680, 1254, 60, 940))


# what is the quick fix to this
delarship = dealerShip("Engine Moto", "Egypt", myCars)
print(delarship)

