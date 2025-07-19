# Dictionary Assignments :-

"""
Q1. Write a program to add a key and value to a dictionary.
    Sample Dictionary : {0: 10, 1: 20}
    Expected Result : {0: 10, 1: 20, 2: 30}
"""
# Sol.
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print(my_dict)


"""
Q2. Write a program to concatenate the following dictionaries to create a new one.
    Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""
# Sol.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)
print(result)


# Q3. Write a program to check if a given key already exists in a dictionary.
# Sol.
my_dict = {1: 'john', 2: 'sam', 3: 'wilson'}
key = int(input("Enter the key to check: "))
if key in my_dict:
    print(f"Key {key} exists in the dictionary with value '{my_dict[key]}'.")
else:
    print(f"Key {key} does not exist in the dictionary.")


"""
Q4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
"""
# Sol.
my_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(f"{key}: {value}")    


# Q5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.
# Sol.
squares_dict = {}
for x in range(1, 16):
    squares_dict[x] = x ** 2
print(squares_dict) 


# Q6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
# Sol.
my_dict = {'a': 100, 'b': 200, 'c': 300}
total = 0
for value in my_dict.values():
    total += value
print("Sum of all values in the dictionary:", total)
