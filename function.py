# 1. Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))


# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))


# 3. Define a function that accepts two numbers and returns the greater number.
def greater(a, b):
    return a if a > b else b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Greater number:", greater(a, b))


# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest:", simple_interest(p, r, t))


# 5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(is_prime(n))


# 6. Define a function to calculate the area of a circle using its radius.
def circle_area(radius):
    return 3.14159 * radius * radius

r = float(input("Enter radius: "))
print("Area:", circle_area(r))


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter n: "))
print("Sum:", sum_natural(n))


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Result:", power(base, exponent))


# 9. Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest(numbers):
    largest_value = numbers[0]
    for num in numbers[1:]:
        if num > largest_value:
            largest_value = num
    return largest_value

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Largest:", largest(numbers))


# 10. Define a function that accepts a string and returns the number of vowels present in it.
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")
print("Vowels:", count_vowels(text))


# 11. Write a function that accepts a string and returns its reverse.
def reverse_string(text):
    return text[::-1]

text = input("Enter a string: ")
print("Reverse:", reverse_string(text))


# 12. Create a function that checks whether a given string or number is a palindrome.
def is_palindrome(value):
    text = str(value)
    return text == text[::-1]

value = input("Enter a string or number: ")
print("Palindrome:", is_palindrome(value))


# 13. Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Average:", average(numbers))


# 14. Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_element(items, element):
    count = 0
    for item in items:
        if item == element:
            count += 1
    return count

items = input("Enter elements separated by spaces: ").split()
element = input("Enter element to count: ")
print("Occurrences:", count_element(items, element))


# 15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

items = input("Enter elements separated by spaces: ").split()
print("Unique elements:", unique_elements(items))


# 16. Create a function to find the second-largest number in a list.
def second_largest(numbers):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Second largest:", second_largest(numbers))


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter n: "))
print("Fibonacci:", fibonacci(n))


# 18. Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def percentage_grade(marks):
    percentage = sum(marks) / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade

marks = list(map(float, input("Enter marks of 5 subjects: ").split()))
percentage, grade = percentage_grade(marks)
print("Percentage:", percentage)
print("Grade:", grade)


# 19. Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6
    return bill

units = float(input("Enter units consumed: "))
print("Electricity Bill:", electricity_bill(units))


# 20. Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print("Gross Salary:", gross_salary(basic))


# 21. Create a function that accepts item prices and quantities and returns the total bill after applying a discount.
def total_bill(prices, quantities, discount=10):
    total = sum(price * quantity for price, quantity in zip(prices, quantities))
    return total - total * discount / 100

prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
print("Total Bill after discount:", total_bill(prices, quantities))


# 22. Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    return minimum, maximum, total, avg

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
minimum, maximum, total, avg = statistics(numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total)
print("Average:", avg)


# 23. Write a program using separate functions to process student records containing name, roll number, and marks in five subjects.
# Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def student_result(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade

def process_students(students):
    results = []
    for student in students:
        total, percentage, grade = student_result(student["marks"])
        results.append({
            "name": student["name"],
            "roll": student["roll"],
            "total": total,
            "percentage": percentage,
            "grade": grade
        })
    class_average = sum(r["percentage"] for r in results) / len(results)
    highest = max(results, key=lambda r: r["percentage"])
    lowest = min(results, key=lambda r: r["percentage"])
    return results, class_average, highest, lowest

students = [
    {"name": "Asha", "roll": 1, "marks": [85, 90, 78, 88, 92]},
    {"name": "Riya", "roll": 2, "marks": [75, 80, 70, 82, 77]},
    {"name": "Neha", "roll": 3, "marks": [92, 95, 90, 94, 96]}
]
results, class_average, highest, lowest = process_students(students)
for result in results:
    print(result)
print("Class Average:", class_average)
print("Highest Scorer:", highest["name"])
print("Lowest Scorer:", lowest["name"])


# 24. Create functions for deposit, withdrawal, balance enquiry, and transaction history.
# Prevent withdrawal when the balance is insufficient and maintain a transaction record.
balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Deposited: {amount}")
    return balance

def withdraw(amount):
    global balance
    if amount > balance:
        transactions.append(f"Failed withdrawal: {amount}")
        return "Insufficient balance"
    balance -= amount
    transactions.append(f"Withdrawn: {amount}")
    return balance

def balance_enquiry():
    return balance

def transaction_history():
    return transactions

deposit(5000)
print("Balance after deposit:", balance_enquiry())
print("Withdrawal:", withdraw(1500))
print("Balance:", balance_enquiry())
print("Transactions:", transaction_history())


# 25. Create functions to add books, issue books, return books, search books, and display available books.
# Maintain book availability using dictionaries.
books = {}

def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}

def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        return "Book issued"
    return "Book not available"

def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        return "Book returned"
    return "Book not found"

def search_book(title):
    return [book for book in books.values() if title.lower() in book["title"].lower()]

def display_available():
    return [book["title"] for book in books.values() if book["available"]]

add_book(1, "Python Programming")
add_book(2, "Data Structures")
add_book(3, "Cloud Computing")
print(issue_book(1))
print("Search:", search_book("Python"))
print("Available:", display_available())
print(return_book(1))
print("Available:", display_available())


# 26. Develop a modular program using functions to calculate electricity bills using different consumption slabs.
# Include fixed charges, taxes, and discounts.
def calculate_energy_charge(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        return 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    return 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6

def calculate_electricity_bill(units):
    fixed_charge = 100
    energy = calculate_energy_charge(units)
    subtotal = energy + fixed_charge
    tax = subtotal * 0.05
    discount = subtotal * 0.05 if units < 100 else 0
    return subtotal + tax - discount

units = float(input("Enter units for modular bill: "))
print("Final Electricity Bill:", calculate_electricity_bill(units))


# 27. Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill.
# Apply discounts based on patient category.
def consultation_charges(amount):
    return amount

def laboratory_charges(amount):
    return amount

def medicine_charges(amount):
    return amount

def room_charges(days, rate):
    return days * rate

def final_hospital_bill(consultation, laboratory, medicine, room, category):
    subtotal = consultation + laboratory + medicine + room
    discount_rate = {"senior": 0.15, "child": 0.10, "general": 0}.get(category.lower(), 0)
    discount = subtotal * discount_rate
    return subtotal - discount

consultation = consultation_charges(500)
laboratory = laboratory_charges(1200)
medicine = medicine_charges(800)
room = room_charges(3, 1000)
category = input("Enter patient category (senior/child/general): ")
print("Final Hospital Bill:", final_hospital_bill(
    consultation, laboratory, medicine, room, category
))


# 28. Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
cart = {}

def add_product(name, price, quantity):
    cart[name] = {"price": price, "quantity": quantity}

def remove_product(name):
    if name in cart:
        del cart[name]

def calculate_subtotal():
    return sum(item["price"] * item["quantity"] for item in cart.values())

def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.90
    return subtotal

def calculate_gst(amount, rate=18):
    return amount * rate / 100

def generate_invoice(coupon=""):
    subtotal = calculate_subtotal()
    discounted = apply_coupon(subtotal, coupon)
    gst = calculate_gst(discounted)
    return subtotal, discounted, gst, discounted + gst

add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
subtotal, discounted, gst, final = generate_invoice("SAVE10")
print("Subtotal:", subtotal)
print("After Coupon:", discounted)
print("GST:", gst)
print("Final Invoice:", final)


# 29. Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(numbers, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if numbers[mid] == target:
        return mid
    if target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    return binary_search(numbers, target, mid + 1, high)

numbers = [10, 20, 30, 40, 50, 60]
target = int(input("Enter element to search: "))
index = binary_search(numbers, target, 0, len(numbers) - 1)
print("Index:", index)


# 30. Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter decimal number: "))
print("Binary:", decimal_to_binary(n) if n != 0 else "0")


# 31. Check whether a string is a palindrome using recursion.
def recursive_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return recursive_palindrome(text[1:-1])

text = input("Enter a string: ")
print("Palindrome:", recursive_palindrome(text))


# 32. Create separate functions for addition, subtraction, multiplication, and division.
# Pass these functions as arguments to another function called calculate().
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(addition, 10, 5))
print(calculate(subtraction, 10, 5))
print(calculate(multiplication, 10, 5))
print(calculate(division, 10, 5))


# Programs on Lambda Function

# 33. Write a lambda function to calculate the square of a given number.
square = lambda n: n ** 2
print("Square:", square(5))


# 34. Create a lambda function that returns the cube of a number.
cube = lambda n: n ** 3
print("Cube:", cube(4))


# 35. Write a lambda function that returns True if a number is even and False otherwise.
is_even = lambda n: n % 2 == 0
print(is_even(8))


# 36. Use a lambda function to find the maximum of two numbers.
maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(10, 20))


# 37. Create a lambda function to calculate simple interest using principal, rate, and time.
si = lambda p, r, t: (p * r * t) / 100
print("Simple Interest:", si(10000, 5, 2))


# 38. Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


# 39. Use map() with lambda to calculate the cube of every element in a list.
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes:", cubes)


# 40. Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sums = list(map(lambda a, b: a + b, list1, list2))
print("Corresponding sums:", sums)


# 41. Take a list of integers, use filter() and lambda to extract all even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)


# 42. Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
def prime_check(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 11, 12]
prime_numbers = list(filter(lambda x: prime_check(x), numbers))
print("Prime numbers:", prime_numbers)


# 43. Use filter() and lambda to extract positive numbers from a list.
numbers = [-5, 3, -2, 7, 0, 10]
positive = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", positive)


# 44. Take a list of numbers, use filter() and lambda to find numbers greater than 50.
numbers = [20, 55, 70, 45, 90, 30]
greater_50 = list(filter(lambda x: x > 50, numbers))
print("Greater than 50:", greater_50)


# 45. Take a list of words, use filter() and lambda to find words having more than five characters.
words = ["apple", "banana", "cat", "python", "computer"]
long_words = list(filter(lambda word: len(word) > 5, words))
print("Words with more than 5 characters:", long_words)


# 46. Take a list of words; sort them according to their length using lambda.
words = ["python", "is", "easy", "programming", "code"]
sorted_words = sorted(words, key=lambda word: len(word))
print("Sorted by length:", sorted_words)


# 47. Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
students = [("Asha", 85), ("Riya", 92), ("Neha", 78), ("Pooja", 88)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Students sorted by marks:", sorted_students)


# 48. Take employee records containing name and salary, sort them according to salary using lambda.
employees = [("Amit", 55000), ("Ravi", 45000), ("Neha", 70000), ("Pooja", 60000)]
sorted_employees = sorted(employees, key=lambda employee: employee[1])
print("Employees sorted by salary:", sorted_employees)


# 49. Take a list containing student names and marks, use functions and lambda expressions to:
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.
students = [("Asha", 85), ("Riya", 72), ("Neha", 91), ("Pooja", 68)]

def student_average(records):
    return sum(map(lambda s: s[1], records)) / len(records)

print("Average marks:", student_average(students))
print("Above 75:", list(filter(lambda s: s[1] > 75, students)))
print("Sorted:", sorted(students, key=lambda s: s[1]))


# 50. Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
# a) Find employees earning more than ₹50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.
employees = [
    ("Amit", "IT", 55000),
    ("Ravi", "HR", 45000),
    ("Neha", "IT", 70000),
    ("Pooja", "Finance", 60000)
]

above_50000 = list(filter(lambda e: e[2] > 50000, employees))
increased_salaries = list(map(lambda e: (e[0], e[1], e[2] * 1.10), employees))
sorted_by_salary = sorted(employees, key=lambda e: e[2])

print("Above ₹50,000:", above_50000)
print("After 10% increase:", increased_salaries)
print("Sorted by salary:", sorted_by_salary)


# 51. Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
# a) Calculate total value of each product.
# b) Filter products costing more than ₹1,000.
# c) Sort products according to total value.
products = [
    ("Laptop", 50000, 1),
    ("Mouse", 800, 2),
    ("Keyboard", 1500, 1),
    ("Monitor", 12000, 2)
]

product_values = list(map(lambda p: (p[0], p[1], p[2], p[1] * p[2]), products))
above_1000 = list(filter(lambda p: p[1] > 1000, products))
sorted_products = sorted(product_values, key=lambda p: p[3])

print("Product total values:", product_values)
print("Products costing more than ₹1,000:", above_1000)
print("Sorted by total value:", sorted_products)


# 52. Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
# a) Find the length of every word.
# b) Extract words having more than five characters.
# c) Sort words according to their length.
words = ["python", "java", "programming", "code", "computer", "AI"]

lengths = list(map(lambda word: len(word), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_by_length = sorted(words, key=lambda word: len(word))

print("Lengths:", lengths)
print("Words with more than 5 characters:", long_words)
print("Sorted by length:", sorted_by_length)
