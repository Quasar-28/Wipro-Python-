# Mini Projects :-

"""
Project 1 (Sort the colors) :-
Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint: All the colors will be completely in either lower case or upper case.
Sample input 1: green-red-yellow-black-white
Sample output 1: black-green-red-white-yellow
Sample input 2: PINK-BLUE-TAN-PURPLE
Sample output 2: BLUE-PINK-PURPLE-TAN
"""
# Code :-
def sort_colors(text) :
    colors_list = text.split('-')
    colors_list.sort()
    sorted_colors = "-".join(colors_list)
    return sorted_colors
if __name__ == "__main__":
    colors_string = input("Enter hyphen-separated sequence of colors : ")
    sorted_colors_strings = sort_colors(colors_string)
    print(sorted_colors_strings)


"""
Project 2 (Playing with names) :-
Create a Python module with the following functions:
Function Names and their tasks :-
ispalindrome(name) : Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name) : Given the user name as input, this function should tell us how many vowels are present in it.
frequency_of_letters(name) : Given the user name as input, this function should tell us how many times each letter appears in the name.
Note: name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs.

Sample input 1: bob
Sample output 1:
Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

Sample input 2: marcel bentok tanaka
Sample output 2:
No it is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, I-1, b-1, n-2, t-2, o-1, k-2
"""
# Code :-
def ispalindrome(name) :
    if name == name[::-1] :
        print(f"Yes it is a palindrome")
    else :
        print(f"No it is not a palindrome")
def count_the_vowels(name) :
    vowels = "aeiou"
    vowels_count = 0
    for char in name :
        if char in vowels :
            vowels_count += 1
    print(f"No. of vowels : {vowels_count}")
def frequency_of_letters(name):
    freq = {}
    for char in name:
        if char == " " :
            continue
        freq[char] = freq.get(char, 0) + 1
    print("Frequency of letters :",end = " ")
    for char, count in freq.items():
        print(f"{char} - {count}",end=", ")

# Note that test script is in test_of_project2.py in the same directory







