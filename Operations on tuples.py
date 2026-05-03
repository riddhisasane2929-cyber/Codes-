# Creating a Tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# Accessing Elements
print("\nAccessing Elements:")
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Index (finding position of an element)
print("\nIndex of element 30:", my_tuple.index(30))

# Slicing
print("\nSlicing:")
print("Elements from index 1 to 3:", my_tuple[1:4])
print("Elements from start to index 2:", my_tuple[:3])
print("Elements from index 2 to end:", my_tuple[2:])

# Nested Tuples
nested_tuple = (1, 2, (3, 4, 5), 6)
print("\nNested Tuple:", nested_tuple)

# Accessing elements in nested tuple
print("Element inside nested tuple:", nested_tuple[2][1]) # Access 4

Output 
Tuple: (10, 20, 30, 40, 50)

Accessing Elements:
First element: 10
Last element: 50

Index of element 30: 2

Slicing:
Elements from index 1 to 3: (20, 30, 40)
Elements from start to index 2: (10, 20, 30)
Elements from index 2 to end: (30, 40, 50)

Nested Tuple: (1, 2, (3, 4, 5), 6)
Element inside nested tuple: 4
