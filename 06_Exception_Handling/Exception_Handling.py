# Exception Handling Assignments :-

# Q1. Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
# Sol.
num1 = input("Enter the numerator: ")
num2 = input("Enter the denominator: ")
try:
    a = float(num1)
    b = float(num2)
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numeric values.")
else:
    print("Result of division:", result)


"""
Q2. Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message.
"""
# Sol.
import math
user_input = input("Enter a number: ")
try:
    num = int(user_input)
    if num <= 1:
        print(num, "is not a prime number.")
    else:
        for i in range(2, math.isqrt(num) + 1):
            if num % i == 0:
                print(num, "is not a prime number.")
                break
        else:
            print(num, "is a prime number.")

except ValueError:
    print("Error: Please enter a valid integer.")



"""
Q3. Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
"""
# Sol.
filename = input("Enter the file name (with .txt extension): ")
try:
    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()
        print("\n--- File Content in Title Case ---\n")
        print(content.title())
except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")



"""
Q4. Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
"""
# Sol.
numbers = [12, -5, 0, 8, -3, 27, -11, 4, -9, 15]
try:
    index = int(input("Enter an index (0 to 9): "))
    value = numbers[index]
    if value > 0:
        print(f"The number at index {index} is positive.")
    elif value < 0:
        print(f"The number at index {index} is negative.")
    else:
        print(f"The number at index {index} is zero.")
except IndexError:
    print("Error: Invalid index. Please enter a number between 0 and 9.")
except ValueError:
    print("Error: Please enter a valid integer index.")

