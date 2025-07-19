# Tuple Assignments :-

# Q1. Write a program to print the 4th element from first and 4th element from last in a tuple.
# Sol.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
if len(my_tuple) >= 4:
    fourth_from_start = my_tuple[3]       
    fourth_from_end = my_tuple[-4]        
    print("4th element from the beginning:", fourth_from_start)
    print("4th element from the end:", fourth_from_end)
else:
    print("The tuple has less than 4 elements.")


# Q2. Write a program to check whether an element exists in a tuple or not.
# Sol.
# Sample tuple
my_tuple = (10, 20, 30, 40, 50)
element = int(input("Enter an element to search: "))
if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


# Q3. Write a program to convert a list into a tuple.
# Sol.
my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print("Original list : ", my_list)
print("list converted into tuple : ", my_tuple)


# Q4. Write a program to find the index of an item in a tuple.
# Sol.
my_tuple = (10, 20, 30, 40, 50)
item = int(input("Enter the item to find its index: "))
if item in my_tuple:
    index = my_tuple.index(item)
    print(f"The index of {item} is: {index}")
else:
    print(f"{item} is not in the tuple.")


"""
Q5. Write a program to replace last value of tuples in a list to 100.
    Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
# Sol.
tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = []
for t in tuple_list:
    new_tuple = t[:-1] + (100,)
    updated_list.append(new_tuple)
print("Updated list:", updated_list)