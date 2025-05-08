# Question 1: Getting to Know the User

# Let's ask the user for their name and save it
name = input("What is your name? ")

# Now ask them how old they are and save that too
age = input("How old are you? ")

# Greet the user using the information they gave us
print(f"Hello, {name}! You are {age} years old.")

#------------------------------------------------------------------------------------
# Question 2: Calculating the Area of a Rectangle

# Ask the user to enter the length of a rectangle (as a whole number)
length = int(input("Enter the length of the rectangle: "))

# Now ask for the width (also as a whole number)
width = int(input("Enter the width of the rectangle: "))

# Multiply length and width to get the area
area = length * width

# Show the user the result
print(f"The area of the rectangle is {area} square units.")

#------------------------------------------------------------------------------------
# Question 3: Converting Temperature

# Ask the user for a temperature in Celsius (this can be a decimal number)
celsius = float(input("Enter the temperature in Celsius: "))

# Use the formula to convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display the Fahrenheit temperature, rounded to 2 decimal places
print(f"The temperature in Fahrenheit is {round(fahrenheit, 2)}°F.")
