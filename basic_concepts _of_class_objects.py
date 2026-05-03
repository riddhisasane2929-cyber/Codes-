# Define the Mobile class
class Mobile:
def __init__(self, brand, model, price):
self.brand = brand
self.model = model
self.price = price

# Method to display mobile details
def display(self):
print("Brand:", self.brand)
print("Model:", self.model)
print("Price:", self.price)
print("-" * 30)


# Creating objects (instances of the class)
mobile1 = Mobile("Samsung", "Galaxy S23", 75000)
mobile2 = Mobile("Apple", "iPhone 14", 80000)
mobile3 = Mobile("OnePlus", "11R", 40000)

# Displaying mobile details
print("Mobile Details:\n")
mobile1.display()
mobile2.display()
mobile3.display()
 
Output 

# Define the Mobile class
class Mobile:
def __init__(self, brand, model, price):
self.brand = brand
self.model = model
self.price = price

# Method to display mobile details
def display(self):
print("Brand:", self.brand)
print("Model:", self.model)
print("Price:", self.price)
print("-" * 30)


# Creating objects (instances of the class)
mobile1 = Mobile("Samsung", "Galaxy S23", 75000)
mobile2 = Mobile("Apple", "iPhone 14", 80000)
mobile3 = Mobile("OnePlus", "11R", 40000)

# Displaying mobile details
print("Mobile Details:\n")
mobile1.display()
mobile2.display()
mobile3.display()
