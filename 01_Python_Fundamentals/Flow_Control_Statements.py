# Flow control statements - Assignments :-

# Q1. Write a program to check if a given number is positive , negative or zero 
# Sol.
num = int(input("Enter a number : "))
if(num>0) :
    print(f"{num} is positive")
elif(num<0) :
    print(f"{num} is negative")
else : 
    print(f"{num} is zero")


# Q2. Write a program to check if a given number is odd or even.
# Sol. 
num = int(input("Enter the number : ")) 
if(num%2 == 0) :
    print(f"{num} is even")
else :
    print(f"{num} is odd")


#Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
#Sol :
num1 = int(input("Enter first number : "))
num2 = int(input("Enter first number : "))
if((num1%10) == (num2%10)) :
    print(True)
else :
    print(False)


# Q4. Write a program to print numbers from 1 to 10 in a single row with one tab space.
# Sol:
for i in range(1,11) :
    print(i,end='\t') 


# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
# Sol.
for i in range(23,57) :
    if(i%2==0) :
        print(i)


# Q6. Write a program to check if a given number is prime or not.
# Sol. 
num = int(input("Enter a number : "))
if(num == 0 or num == 1) :
    print(f"{num} is not a prime number")
elif(num>1) :
    for i in range(2,num) :
        if(num%i==0) :
            print(f"{num} is not a prime number")
            break
    else :
        print(f"{num} is a prime number")
else :
    print("Please enter a non-negative integer")


# Q7.  Write a program to print prime numbers between 10 and 99.
# Sol.
for num in range(10,99) :
    for i in range(2,num) :
        if(num%i==0) :
            break
    else :
        print(num)


# Q8. Write a program to print the sum of all the digits of a given number.
# Sol.
num = int(input("Enter a number : "))
temp_num = num
Sum_of_digits = 0
while(temp_num>0) :
    digit = temp_num%10
    Sum_of_digits += digit
    temp_num //=10
print(f"Sum of digits of {num} is {Sum_of_digits}")


# Q9. Write a program to reverse a given number and print.
# Sol.
num = int(input("Enter a number : "))
temp_num = num
rev_num = 0
while(temp_num>0) :
    digit = temp_num%10
    rev_num = rev_num*10 + digit
    temp_num //= 10
print(f"Reverse of {num} is {rev_num}")


# Q10. Write a program to find if the given number is palindrom or not.
# Sol.
num = int(input("Enter a number : "))
temp_num = num
rev_num = 0
while(temp_num>0) :
    digit = temp_num%10
    rev_num = rev_num*10 + digit
    temp_num //= 10
if(rev_num==num) :
    print(f"{num} is a palindrome")
else :
    print(f"{num} is not a palindrome")