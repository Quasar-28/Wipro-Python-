# Mini Project :-

"""
Project 1 (Purchase) :-
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to
handle the possible exceptions.
Note:
. Data is stored in a text file Purchase-1.txt.
. Each line contains one item's details.
. Item name and price is separated by a space.
. You have to enter the file name during run time.
Sample input 1:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
(blank line)
Discount 5

Sample output 1:
Enter the file name: Purchase-1
No of items purchased: 3
No of free items: 0
Amount to pay: 135
Discount given: 5
Final amount paid: 130

Sample input 2:
Purchase-1.txt
Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250
(blank line)
Perfume Free
Soup Free
(blank line)
Discount 80

Sample output 2:
Enter the file name: Purchase-1
No of items purchased: 5
No of free items: 2
Amount to pay: 485
Discount given: 80
Final amount paid: 405
"""
# Sol.
def get_info():
    try:
        filename = input("Enter the file name: ") + ".txt"
        with open(filename, "r") as file:
            lines = file.readlines()
        purchase_count = 0
        free_count = 0
        total_amount = 0
        discount = 0
        section = 1  # 1: Purchased, 2: Free, 3: Discount
        for line in lines:
            line = line.strip()
            if line == "":
                section += 1
                continue
            parts = line.split()
            if section == 1 and len(parts) == 2:
                try:
                    price = float(parts[1])
                    total_amount += price
                    purchase_count += 1
                except ValueError:
                    print(f"Invalid price for item: {line}")
            elif section == 2 and len(parts) == 2 and parts[1].lower() == "free":
                free_count += 1
            elif section == 3 and len(parts) == 2 and parts[0].lower() == "discount":
                try:
                    discount = float(parts[1])
                except ValueError:
                    print("Invalid discount value.")
        final_amount = total_amount - discount
        print("No of items purchased:", purchase_count)
        print("No of free items:", free_count)
        print("Amount to pay:", int(total_amount))
        print("Discount given:", int(discount))
        print("Final amount paid:", int(final_amount))
    except FileNotFoundError:
        print("File not found. Please check the file name.")

if __name__ == "__main__":
    get_info()

