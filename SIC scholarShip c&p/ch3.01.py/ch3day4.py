# class Vehicle:  # File: vehicle.py​
#     def __init__(self, maker, model, year, engine_power, max_speed, price):
#         self.maker = maker
#         self.model = model
#         self.year = year
#         self.engine_power = engine_power
#         self.max_speed = max_speed
#         self._price = price


#     def get_price(self):
#         return self._price
#     def set_price(self, new_price):
#         self._price = new_price
#     def show_properties(self):
#         print(f"Maker: {self.maker}", f"Model: {self.model}", f"Year: {self.year}", f"Engine Power: {self.engine_power} hp",
#         f"Max Speed: {self.max_speed} mph", f"Price: ${self._price:.2f}", sep='\n')


#     # File: car.py​
# class Car(Vehicle):

#     def __init__(self, maker, model, year, engine_power, max_speed, price, max_capacity):
#         super().__init__(maker, model, year, engine_power, max_speed, price)
#         self.max_capacity = max_capacity

#     def show_properties(self):
#         super().show_properties()
#         print(f"Max Capacity: {self.max_capacity} passengers")


# # File: truck.py​
# class Truck(Vehicle):

#     def __init__(self, maker, model, year, engine_power, max_speed, price, max_load_weight):
#         super().__init__(maker, model, year, engine_power, max_speed, price)
#         self.max_load_weight = max_load_weight

#     def show_properties(self):

#         super().show_properties()
#         print(f"Max Load Weight: {self.max_load_weight} lbs")


#         # File: main.py​
# car = Car("Toyota", "Camry", 2023, 200, 140, 30000, 5)
# truck = Truck("Ford", "F-150", 2023, 350, 120, 45000, 2000)

# print("Car Properties:")
# car.show_properties()
# print("\nTruck Properties:")
# truck.show_properties()

# class BookStore:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.status = "uncomplete" #default
#     def print_details(self):
#         print(self.title, self.author, self.year)
#     def mark_as_read(self):
#         self.status = "complete"

#     def display_info(self):
#         print(f"tile: {self.title} author {self.author} year {self.year}status {self.status}")
#     # def __str__ (self):
#     #     return f"Book: {self.title} by {self.author} [{self.status}]"


# book = BookStore("how to be loved", "dael carnige",2021)
# book.display_info()

class carMaker:

    def __init__(i, maker, model, year, licenseNumber, enginePower, maxspeed):
        i.maker = maker
        i.model = int(model)
        i.year = year
        i.licenseNumber = licenseNumber
        i.enginePower = int(enginePower)
        i.maxspeed = int(maxspeed)

    def clac_Sum(i):
        price = i.model+i.enginePower+i.maxspeed
        return price

    def __str__(i):
        return (
            f"Maker: {i.maker}\nModel: {i.model}\nYear: {i.year}\nLicense: {i.licenseNumber}\nEngine Power: {i.enginePower} HP\nMax Speed: {i.maxspeed} km/h\n\n\n")

    def __repr__(i):
        return i.__str__()
