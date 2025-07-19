# Strings Assignments :-

# Q1. Write a program to count the number of upper and lower case letters in a String.
# Sol.
text = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


# Q2. Write a program that will check whether a given String is Palindrome or not.
# Sol.
text = input("Enter a string: ")
cleaned_text = text.replace(" ", "").lower()
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


"""
Q3. Given a string, return a new string made of n copies of the first 2 chars of   the original string where n is the length of the string. The string length will be >=2. 
If input is "Wipro" then output should be "WiWiWiWiWi".
"""
# Sol.
text = input("Enter a string (length >= 2): ")
first_two = text[:2]
n = len(text)
result = first_two * n
print("Output : ", result)


"""
Q4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. 
If the input is "xHix", then output is "Hi".
"""
# Sol.
text = input("Enter a string : ")
if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]
print("Output : ", text)


"""
Q5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive.
For example , if the inputs are "Wipro" and 3, then the output should be "propropro".
"""
# Sol.
text = input("Enter a string: ")
n = int(input("Enter an integer (0 to length of the string): "))
if 0 <= n <= len(text):
    last_n_chars = text[-n:]         
    result = last_n_chars * n       
    print("Result:", result)
else:
    print("Invalid input: n is out of range.")
