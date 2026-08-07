#1.	Write a Python program to create a list of five fruits and display the list.
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruits:", fruits)


'''2.	Create a list of five integers. Display:
•	First element 
•	Last element 
•	Third element
'''
numbers = [10, 20, 30, 40, 50]
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Third:", numbers[2])


#3.	Create a list of colors. Replace the third color with another color and display the updated list.
colors = ["Red", "Blue", "Green", "Yellow"]
colors[2] = "Pink"
print(colors)


'''4.	Create a list of numbers. Add:
•	One element at the end 
•	One element at the beginning 
•	One element at a specified position 
Display the updated list.
'''
numbers = [10, 20, 30]
numbers.append(40)
numbers.insert(0, 5)
numbers.insert(2, 15)
print(numbers)


'''5.	Create a list of student names. Remove:
•	First student 
•	Last student 
•	A specific student by name 
Display the remaining list.
'''
students = ["Amit", "Rahul", "Priya", "Sneha", "Riya"]
students.pop(0)
students.pop()
students.remove("Priya")
print(students)

 
#6.	Write a program to find the largest and smallest number in a list without using max() or min().
numbers = [12, 45, 6, 89, 34]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest:", largest)
print("Smallest:", smallest)


'''7.	Accept 10 numbers from the user and store them in a list. Calculate:
•	Sum 
•	Average 
'''
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = sum(numbers)
avg = total / 10
print("Sum:", total)
print("Average:", avg)


'''8.	Store 15 integers in a list. Count how many numbers are:
•	Even 
•	Odd
'''
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)


#9.	Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.
cities = ["Pune", "Mumbai", "Delhi", "Chennai"]
city = input("Enter city: ")
if city in cities:
    print("City found")
else:
    print("City not found")
    
    

#10.	Write a program to reverse a list without using the reverse() method.
numbers = [10,20,30,40,50]
rev = []
for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])
print(rev)


'''11.	Create a list of 10 numbers and display:
•	First 5 elements 
•	Last 5 elements 
•	Middle 4 elements 
•	Alternate elements 
•	Reverse list using slicing
'''
numbers = [1,2,3,4,5,6,7,8,9,10]
print("First 5:", numbers[:5])
print("Last 5:", numbers[-5:])
print("Middle 4:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])



#12.	Display all elements present at even index positions.
numbers = [10,20,30,40,50,60]
for i in range(0,len(numbers),2):
    print(numbers[i])


'''13.	Accept 10 numbers and sort them in:
•	Ascending order 
•	Descending order
'''
numbers = []
for i in range(10):
    numbers.append(int(input("Enter number: ")))
numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)


#14.	Create a list containing duplicate values and display only unique elements
numbers = [1,2,2,3,4,4,5]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)


#15.	Find the second largest element in a list.
numbers = [12,45,67,89,23]
numbers.sort()
print("Second Largest:", numbers[-2])


'''16.	Create a nested list storing:
•	Student Name 
•	Roll Number 
•	Marks 
Display all student details.
'''
students = [
    ["Amit",101,85],
    ["Priya",102,90],
    ["Rahul",103,78]
]
for s in students:
    print(s)
    
    

#17.	Create two 3 × 3 matrices using nested lists and perform matrix addition.
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,8,7],[6,5,4],[3,2,1]]
C = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print(C)


'''18.	Create a shopping cart using a list.
Perform:
•	Add item 
•	Remove item 
•	Search item 
•	Display cart 
•	Count total items
'''
cart = ["Milk","Bread"]

cart.append("Eggs")
cart.remove("Bread")

item = input("Search item: ")

if item in cart:
    print("Found")
else:
    print("Not Found")

print(cart)
print("Total Items:", len(cart))



'''19.	Store names of students present in class.
Display:
•	Total students 
•	Search a student's attendance 
•	Add a new student 
•	Remove an absent student 
'''
students = ["Amit","Rahul","Priya"]

print("Total:", len(students))

name = input("Search student: ")

if name in students:
    print("Present")

students.append("Sneha")
students.remove("Rahul")

print(students)



'''20.	Create a list of books.
Implement:
•	Add a new book 
•	Search a book 
•	Remove a book 
•	Display all books 
•	Count total books
'''
books = ["Python","Java","C++"]
books.append("AI")
book = input("Search book: ")
if book in books:
    print("Book Found")
books.remove("Java")
print(books)
print("Total Books:", len(books))



#21.	Accept two lists and merge them into a single list.
list1 = [1,2,3]
list2 = [4,5,6]
merged = list1 + list2
print(merged)



#22.	Find common elements between two lists.
a = [1,2,3,4]
b = [3,4,5,6]
common = []
for i in a:
    if i in b:
        common.append(i)

print(common)


#23.	Count the frequency of each element in a list
numbers = [1,2,2,3,3,3]

for i in numbers:
    print(i,":",numbers.count(i))
    
    

'''24.	Rotate a list:
•	Left by one position 
•	Right by one position
'''
numbers = [1,2,3,4,5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Left:", left)
print("Right:", right)


#25.	Remove all duplicate elements while preserving the original order.
numbers = [1,2,2,3,4,3,5]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print(result)



'''26.	Store marks of 20 students in a list and determine:
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Number of students scoring above average 
•	Number of students scoring below average
'''
marks = [60,70,80,90,55,76,88,91,45,66,77,81,69,58,92,73,84,62,79,68]

highest = max(marks)
lowest = min(marks)
average = sum(marks)/len(marks)

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print(highest, lowest, average, above, below)



'''27.	Store salaries of employees and determine:
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning above ₹50,000 
•	Employees earning below ₹30,000 
'''
salary = [25000,35000,60000,52000,28000]

print("Highest:", max(salary))
print("Lowest:", min(salary))
print("Average:", sum(salary)/len(salary))

above = 0
below = 0

for s in salary:
    if s > 50000:
        above += 1
    if s < 30000:
        below += 1

print("Above 50000:", above)
print("Below 30000:", below)



'''28.	Store scores of a batsman in 10 matches and calculate:
•	Highest score 
•	Lowest score 
•	Total runs 
•	Average runs 
•	Number of centuries (≥100) 
•	Number of half-centuries (50–99)
'''
scores = [45,60,120,30,99,105,75,15,130,80]

print("Highest:", max(scores))
print("Lowest:", min(scores))
print("Total:", sum(scores))
print("Average:", sum(scores)/len(scores))

century = 0
half = 0

for s in scores:
    if s >= 100:
        century += 1
    elif s >= 50:
        half += 1

print("Centuries:", century)
print("Half-centuries:", half)



'''29.	Store the temperature of 30 days and determine:
•	Hottest day 
•	Coldest day 
•	Average temperature 
•	Days above average temperature 
•	Days below average temperature
'''
temp = [30,32,31,29,35,36,34,33,32,31]

print("Hottest:", max(temp))
print("Coldest:", min(temp))

avg = sum(temp)/len(temp)

above = 0
below = 0

for t in temp:
    if t > avg:
        above += 1
    elif t < avg:
        below += 1

print("Average:", avg)
print("Above Average:", above)
print("Below Average:", below)




'''30.	Store patient names and ages using lists.
Perform:
•	Add a patient 
•	Delete a patient 
•	Search a patient 
•	Display all patients 
•	Count total patients
''' 
names = ["Amit","Rahul","Priya"]
ages = [30,25,40]

names.append("Sneha")
ages.append(28)

index = names.index("Rahul")
names.pop(index)
ages.pop(index)

search = input("Enter patient name: ")

if search in names:
    print("Patient Found")
else:
    print("Patient Not Found")

for i in range(len(names)):
    print(names[i], ages[i])

print("Total Patients:", len(names))
