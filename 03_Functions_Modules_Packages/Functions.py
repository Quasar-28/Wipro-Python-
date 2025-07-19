# Functions Assignments :-

"""
Q1. Write a function to return the sum of all numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
# Sol.
def calculate_sum(lst) :
    Sum = 0
    for i in lst :
        Sum += i
    return Sum
my_list = [8,2,3,0,7]
total_sum = calculate_sum(my_list)
print(total_sum)


"""
Q2. Write a function to return the reverse of a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
# Sol.
def get_reverse(text) :
    return text[::-1]
my_string = input("Enter a string : ")
rev_string = get_reverse(my_string)
print(rev_string)


# Q3. Write a function to calculate and return the factorial of a number (a non-negative integer).
# Sol.
def calculate_factorial(number) :
    factorial = 1
    for num in range(number,1,-1) :
        factorial *= num
    return factorial
number = int(input("Enter a non-negative integer : "))
result = calculate_factorial(number)
print(result)


# Q4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
# Sol.
def get_cases(text) :
    lower_count = 0
    upper_count = 0
    for i in text :
        if i.islower() :
            lower_count += 1
        else :
            upper_count += 1
    return lower_count,upper_count
my_string = input("Enter a string : ")
LC,UC = get_cases(my_string)
print(f"No. of upper case letters : {UC}\nNo. of lower case letters : {LC}")


"""
Q5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
"""
# Sol.
def find_even_number(lst) :
    even_num_list = []
    for i in lst :
        if i%2 == 0 :
            even_num_list.append(i)
    return even_num_list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_nums = find_even_number(num_list)
print(even_nums)


# Q6. Write a function that takes a number as a parameter and checks whether the number is prime or not.
# Sol.
import math as m
def prime_or_not(num) :
    flag = True
    if (num == 0) or (num == 1) :
        flag = False
        return flag
    for i in range(2,int(m.sqrt(num)+1)) :
        if num % i == 0 :
            flag = False
            break
    return flag
num = int(input("Enter a non-negative number : "))
if prime_or_not(num) :
    print(f"{num} is prime")
else :
    print(f"{num} is not prime")
