# # class decleratin
# class ClassName:
#     # declaring the class attribuets
#     # class attributes not every time in classes requierd
#     class_attribute = "an attribute value"

#     # the class method aka the funcutionality of the class
#     # here by Constructor method
#     constructor(optional)

#     def __init__(self, parameter1, parameter2):
#         self.instance_attribute1 = parameter1
#         self.instance_parameter2 = parameter2

#     # instance functionality aka method
#     def methode1(self):
#         # oly el method bt3ml eh hna code here
#         # code for method 1

#     def methode2(self):
#         # el code for method2

#         # creating obgects(instance)of the class
#     objectName = ClassName(argument1, argument2)

#     #  accesing the class attributes
#     print(ClassName.class_attribute)

#     # accessing Instance Attributes
#     print(objectName.instance_attribute1)
#     # accessing and calling aa method
#     print(objectName.methode1())


# el task
class SicClothes:
    # initializing the attributes of the class
    def __init__(self, clothes_types, model_year, brand, price):
        self.clothes_types = clothes_types
        self.model_year = model_year
        self.brand = brand
        self.price = price

    # doing the methods of the class:
    def calculate_discounted_price(self):
        if self.clothes_types == "shirt":
            return self.price * 0.6  # 40% off
        if self.clothes_types == "pants":
            return self.price * 0.7  # 30% off
        if self.clothes_types == "shoes":
            return self.price * 0.5  # 50% off
        else:
            return self.price  # law mafesh discount

    # hanigy bra el class n creat object mn el input


total_price = 0
items = int(input("how many items did you buy? "))

for i in range(items):
    clothes_types = input("Enter the type of clothes (shirt, pants, shoes): ")
    model_year = input("Enter the model year: ")
    brand = input("Enter the brand: ")
    price = int(input("Enter the price of the item: "))

    # gbna kol el items acssesed mra wahda
    item = SicClothes(clothes_types, model_year, brand,
                      price)  # gbna el items fe heta whda

    # i.e. how to acesse & use the method from the class
    discounted_price = item.calculate_discounted_price()

    print("The price after discount for this item is: ", discounted_price)
    total_price += discounted_price

    print = ("total price is: ", total_price)



class Vehicle:
    def __init__(self,maker,model,year,engine_power, maxSpeed,price):
        self.maker = maker
        self.model=model
        self.year = year
        self.engine_power = engine_power
        self.maxSpeed = maxSpeed
        self.price = price
 

