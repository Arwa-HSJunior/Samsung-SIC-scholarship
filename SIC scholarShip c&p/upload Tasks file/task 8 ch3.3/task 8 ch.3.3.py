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

print("Welcome to the Sic clothe store! \n\n")
total_price = 0
items = int(input("how many items did you buy? "))

for i in range(items):
    clothes_types = input("Enter the type of clothes (shirt, pants, shoes): ").lower()
    model_year = input("Enter the model year: ")
    brand = input("Enter the brand: ")
    price = int(input("Enter the price of the item: "))

    # gbna kol el items acssesed mra wahda
    item = SicClothes(clothes_types, model_year, brand,
                      price)  # Creating an object of the class SicClothes

    # i.e. how to acesse & use the method from the class on the created object
    discounted_price = item.calculate_discounted_price()

    print("The price after discount for this item is: ", discounted_price)
    total_price += discounted_price

print("\ntotal price is: ", total_price)

