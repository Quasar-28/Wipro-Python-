# Set Assignments :-

# Q1. Write a program to remove a given item from the set.
# Sol.
my_set = {10, 20, 30, 40, 50}
item = int(input("Enter the item to remove from the set: "))
if item in my_set:
    my_set.remove(item) 
    print(f"{item} has been removed.")
else:
    print(f"{item} is not in the set.")
print("Updated set:", my_set)


# Q2. Write a program to create an intersection of sets.
# Sol.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)


# Q3. Write a program to create an union of sets.
# Sol.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)


# Q4. Write a program to find the maximum and minimum value in a set.
# Sol.
my_set = {25, 10, 45, 5, 30}
max_value = max(my_set)
min_value = min(my_set)
print("Maximum value in the set:", max_value)
print("Minimum value in the set:", min_value)