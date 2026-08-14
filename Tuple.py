#1.	Write a Python program to create a tuple of five integers and display it.
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


'''2.	Create a tuple containing five city names. Display:
•	First city 
•	Last city 
•	Third city
'''
cities = ("Pune", "Mumbai", "Kolhapur", "Nashik", "Nagpur")
print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


#3.	Create a tuple of student names and display the total number of students using the len() function.
students = ("Amit", "Sneha", "Rahul", "Priya", "Neha")
print("Total students:", len(students))


#4.	Create a tuple of colors. Check whether a given color exists in the tuple
colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = input("Enter a color: ")
if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist")
    


#5.	Create a tuple of fruits and display each fruit using a loop.
fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")
for fruit in fruits:
    print(fruit)


#6.	Create a tuple with repeated numbers and count how many times a particular number appears.
numbers = (10, 20, 10, 30, 10, 40, 20)
number = int(input("Enter number to count: "))
print("Count:", numbers.count(number))



#7.	Create a tuple of employee IDs and find the index of a given ID.
employee_ids = (101, 102, 103, 104, 105)
id = int(input("Enter employee ID: "))
if id in employee_ids:
    print("Index:", employee_ids.index(id))
else:
    print("ID not found")
    
    

#8.	Create two tuples of numbers and concatenate them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print("Concatenated tuple:", result)


#9.	Create a tuple containing three elements and repeat it four times.
numbers = (1, 2, 3)
result = numbers * 4
print(result)


'''10.	Create a tuple of 10 numbers and display:
•	First five elements 
•	Last five elements 
•	Middle four elements 
•	Alternate elements 
•	Reverse tuple
'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])



#11.	Convert a tuple into a list and add a new element.
numbers = (10, 20, 30, 40)
my_list = list(numbers)
my_list.append(50)
print("List:", my_list)


#12.	Accept five numbers from the user, store them in a list, and convert the list into a tuple.
numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers = tuple(numbers)
print("Tuple:", numbers)


#13.	Modify a tuple by converting it into a list and then back into a tuple.
numbers = (10, 20, 30, 40)
my_list = list(numbers)
my_list[1] = 200
numbers = tuple(my_list)
print("Modified tuple:", numbers)


#14.	Create a tuple and delete it completely.
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)
del numbers
print("Tuple deleted successfully")



#15.	Create a nested tuple containing student details and display each record.
students = (
    (1, "Amit", "CSE"),
    (2, "Sneha", "IT"),
    (3, "Rahul", "CSE")
)
for student in students:
    print(student)
    
    
    
#16.	Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = sum(numbers)
print("Sum:", total)


#17.	Find the largest and smallest number in a tuple without using max() and min().
numbers = (45, 12, 78, 23, 9, 56)
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)



#18.	Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
average = total / len(numbers)
print("Average:", average)



'''19.	Store 15 integers in a tuple and count:
•	Even numbers 
•	Odd numbers'''
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)


#20.	Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)
num = int(input("Enter a number: "))
if num in numbers:
    print("Number exists")
else:
    print("Number does not exist")
    
    
'''21.	Store student details in a tuple:
•	Roll Number 
•	Name 
•	Department 
•	Marks 
Display all the details.'''
student = (101, "Sneha", "CSE", 85)
print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])



'''22.	Create tuples containing:
•	Employee ID 
•	Name 
•	Salary 
Display all employee information.'''
employees = (
    (101, "Amit", 30000),
    (102, "Sneha", 35000),
    (103, "Rahul", 40000)
)
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()
    
    
    
''''23.	Store item prices in a tuple and calculate:
•	Total bill 
•	Average price 
•	Highest-priced item 
•	Lowest-priced item'''
prices = (100, 250, 150, 500, 300)
total = sum(prices)
average = total / len(prices)
highest = prices[0]
lowest = prices[0]
for price in prices:
    if price > highest:
        highest = price
    if price < lowest:
        lowest = price
print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)



'''24.	Store temperatures of seven days in a tuple and determine:
•	Maximum temperature 
•	Minimum temperature 
•	Average temperature '''
temperatures = (32, 35, 31, 30, 36, 34, 33)
maximum = max(temperatures)
minimum = min(temperatures)
average = sum(temperatures) / len(temperatures)
print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)



'''25.	Store runs scored in 10 matches and calculate:
•	Total runs 
•	Highest score 
•	Lowest score 
•	Average score '''
runs = (45, 78, 23, 90, 56, 34, 100, 67, 88, 41)
total = sum(runs)
highest = max(runs)
lowest = min(runs)
average = total / len(runs)
print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)



#26.	Create two tuples and find the common elements between them.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common = ()
for num in tuple1:
    if num in tuple2:
        common = common + (num,)
print("Common elements:", common)



#27.	Merge two tuples and remove duplicate elements.
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
merged = tuple(set(tuple1 + tuple2))
print("Merged tuple without duplicates:", merged)



#28.	Count the frequency of each element in a tuple.
numbers = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num, count in frequency.items():
    print(num, "appears", count, "times")
    
    
#29.	Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (50, 20, 40, 10, 30)
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)



'''30.	Create a tuple containing patient records:
•	Patient ID 
•	Name 
•	Age 
•	Blood Group 
Perform the following operations:
•	Display all records 
•	Search for a patient by ID 
•	Count the total number of patients 
•	Display patients with a specific blood group '''
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 28, "A+"),
    (104, "Priya", 35, "O+")
)
print("All Patient Records:")
for patient in patients:
    print(patient)
search_id = int(input("\nEnter Patient ID to search: "))
found = False
for patient in patients:
    if patient[0] == search_id:
        print("Patient found:", patient)
        found = True
if not found:
    print("Patient not found")
print("\nTotal patients:", len(patients))
blood_group = input("\nEnter blood group: ")
print("Patients with blood group", blood_group, ":")
for patient in patients:
    if patient[3] == blood_group:
        print(patient)
