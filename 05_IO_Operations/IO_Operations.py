# IO operations Assignments :-

# Q1. Write a program to read the entire content from a txt file and display it to the user.
# Sol.
# with open('students.txt','r') as file :
#     content = file.read()
#     print(content)


# Q2. Write a program to read first n lines from a txt file. Get n as user input.
# Sol.
filename = input("Enter the file name (with .txt extension): ")
n = int(input("Enter the number of lines to read: "))
with open(filename, 'r') as file:
    print(f"\n--- First {n} lines from '{filename}' ---")
    for i in range(n):
        line = file.readline()
        if not line:
            break  
        print(line.strip())


# Q3. Write a program to accept input from user and append it to a txt file.
# Sol. 
filename = input("Enter the file name (with .txt extension): ")
text = input("Enter the text you want to append to the file: ")
with open(filename, 'a') as file:
    file.write(text + '\n')  
print("Text appended successfully.")


# Q4. Write a program to read contents from a txt file line by line and store each line into a list.
# Sol.
filename = input("Enter the file name (with .txt extension): ")
lines_list = []
with open(filename, 'r') as file:
    for line in file:
        lines_list.append(line.strip())  
print("\nLines stored in list:")
print(lines_list)


# Q5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
# Sol.
filename = input("Enter the file name (with .txt extension): ")
with open(filename, 'r') as file:
    content = file.read()
    words = content.split() 
    longest_word = max(words, key=len) 
print("The longest word is:", longest_word)


# Q6. Write a program to count the frequency of a user entered word in a txt file.
# Sol.
filename = input("Enter the file name (with .txt extension): ")
target_word = input("Enter the word to count: ")
count = 0
with open(filename, 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if word == target_word:
                count += 1
print(f"The word '{target_word}' appears {count} time(s) in the file.")
