try:
# Taking input from user
num = int(input("Enter an integer: "))

# If input is valid
print("You entered:", num)

except ValueError:
# Handling invalid input
print("Error: That is not a valid integer. Please enter a number.")

Output
Enter an integer: abc
Error: That is not a valid integer. Please enter a number.
