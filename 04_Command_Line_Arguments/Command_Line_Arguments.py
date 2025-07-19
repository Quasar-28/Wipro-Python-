# Command Line Arguments Assignments

# Q1. Write a program to accept two numbers as command line arguments and display their sum.
# Sol.
from sys import argv
def find_sum(a,b) :
    return a+b
a = int(argv[1])
b = int(argv[2])
Sum = find_sum(a,b)
print(Sum)


# Q2. Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
# Sol.
from sys import argv
filename = argv[0]
message = " ".join(argv[1:])
print(f"{filename} {message}")



# Q3. Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
# Sol.
import math as m
from sys import argv
Sum = 0
for i in range(1,11) :
    num = int(argv[i])
    if num == 1 or num == 0 :
        continue
    for j in range(2,m.isqrt(num) + 1) :
        if num % j == 0 : 
            break
    else :
        Sum += num 
print(Sum)    
