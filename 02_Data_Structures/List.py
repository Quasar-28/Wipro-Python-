# List Assignments :-

# Q1. Write a program to create a list of five integers and display the list items.Access individual elements through index
# Sol.
my_list = [1,2,3,4,5];
for i in range(0,len(my_list)) :
    print(my_list[i])


# Q2. Write a program to append a new item to the end of list.
# Sol.
my_list = [1,2,3,4,5]
print(my_list)
my_list.append(6)
print(my_list)


# Q3. Write a program to reverse the order of items in the list
#Sol.
some_list = ["John",34,23.4,True]
print(some_list)
some_list.reverse()
print(some_list)


# Q4. Write a program to print the number of occurrences of a specified element in a list
# Sol. 
my_list = [1,1,4,4,2,2,2,2,-1]
print(my_list.count(2))


# Q5. Write a program to append the items of list1 to list2 in the front
# Sol.
# Define the lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)


# Q6. Write a program to insert a new item before the second element in an existing list
# Sol.
my_list = [5,2,1,6,7]
print(my_list)
my_list.insert(1,"new item")
print(my_list)


# Q7. Write a program to remove the item from a specified index in a list.
# Sol.
my_list = [3,1,2,8,9,5]
print(my_list)
my_list.pop(3) 
print(my_list)


# Q8. Write a program to remove the first occurence of a specified element from a list
# Sol.
my_list = [10, 20, 30, 20, 40, 50]
print(my_list)
my_list.remove(20)
print(my_list)