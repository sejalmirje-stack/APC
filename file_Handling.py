
# 1. Write a Python program to create a file named student.txt and write
# the student's name, roll number, branch, and semester into the file.
def create_student_file():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    semester = input("Enter semester: ")

    with open("student.txt", "w") as file:
        file.write("Name: " + name + "\n")
        file.write("Roll Number: " + roll_no + "\n")
        file.write("Branch: " + branch + "\n")
        file.write("Semester: " + semester + "\n")

    print("student.txt created successfully.")

create_student_file()


# 2. Write a program to open a text file and display its complete contents.
def display_file(filename):
    with open(filename, "r") as file:
        print(file.read())

display_file("student.txt")


# 3. Write a program to append additional student information to an existing
# file without deleting its previous contents.
def append_student_info(filename):
    info = input("Enter additional student information: ")
    with open(filename, "a") as file:
        file.write("\n" + info)
    print("Information appended successfully.")

append_student_info("student.txt")


# 4. Write a program to read a text file line by line and display each line separately.
def display_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

display_lines("student.txt")


# 5. Write a program to count and display the total number of lines present in a text file.
def count_lines(filename):
    with open(filename, "r") as file:
        return sum(1 for line in file)

print("Total lines:", count_lines("student.txt"))


# 6. Write a program to count the total number of words present in a text file.
def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
    return len(text.split())

print("Total words:", count_words("student.txt"))


# 7. Write a program to count the total number of characters in a text file,
# including spaces.
def count_characters(filename):
    with open(filename, "r") as file:
        return len(file.read())

print("Total characters:", count_characters("student.txt"))


# 8. Write a program to read a text file and display its lines in reverse order.
def reverse_lines(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in reversed(lines):
        print(line.strip())

reverse_lines("student.txt")


# 9. Read a text file and count the number of vowels and consonants present in the file.
def count_vowels_consonants(filename):
    with open(filename, "r") as file:
        text = file.read().lower()

    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants

vowels, consonants = count_vowels_consonants("student.txt")
print("Vowels:", vowels)
print("Consonants:", consonants)


# 10. Read a text file and calculate the number of alphabets, digits, spaces,
# and special characters.
def count_char_types(filename):
    with open(filename, "r") as file:
        text = file.read()

    alphabets = digits = spaces = special = 0

    for ch in text:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1

    return alphabets, digits, spaces, special

a, d, s, sp = count_char_types("student.txt")
print("Alphabets:", a)
print("Digits:", d)
print("Spaces:", s)
print("Special characters:", sp)


# 11. Read a text file and find the longest word present in the file.
def longest_word(filename):
    with open(filename, "r") as file:
        words = file.read().split()

    if not words:
        return ""

    return max(words, key=len)

print("Longest word:", longest_word("student.txt"))


# 12. Read a text file and count how many times each word occurs.
# Display the result using a dictionary.
def word_frequency(filename):
    with open(filename, "r") as file:
        words = file.read().lower().split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

print("Word frequency:", word_frequency("student.txt"))


# 13. Accept a word from the user and search for it in a text file.
# Display the number of occurrences and the line numbers where it appears.
def search_word(filename, word):
    count = 0
    line_numbers = []

    with open(filename, "r") as file:
        for line_no, line in enumerate(file, start=1):
            words = line.lower().split()
            occurrences = words.count(word.lower())

            if occurrences > 0:
                count += occurrences
                line_numbers.append(line_no)

    return count, line_numbers

word = input("Enter word to search: ")
count, lines = search_word("student.txt", word)
print("Occurrences:", count)
print("Line numbers:", lines)


# 14. Read a text file and replace all occurrences of a specified word with
# another word. Save the modified text in the same file or a new file.
def replace_word(input_file, output_file, old_word, new_word):
    with open(input_file, "r") as file:
        text = file.read()

    text = text.replace(old_word, new_word)

    with open(output_file, "w") as file:
        file.write(text)

    print("Modified file created successfully.")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
replace_word("student.txt", "student_modified.txt", old_word, new_word)


# 15. Read a Python source file and create another file after removing single-line comments.
def remove_comments(input_file, output_file):
    with open(input_file, "r") as source:
        lines = source.readlines()

    with open(output_file, "w") as target:
        for line in lines:
            stripped = line.lstrip()

            if stripped.startswith("#"):
                continue

            if "#" in line:
                line = line.split("#", 1)[0].rstrip() + "\n"

            target.write(line)

    print("Comments removed successfully.")

# Example:
# remove_comments("program.py", "program_without_comments.py")


# 16. Read a text file and create another file containing the same text in uppercase.
def convert_to_uppercase(input_file, output_file):
    with open(input_file, "r") as source:
        text = source.read()

    with open(output_file, "w") as target:
        target.write(text.upper())

    print("Uppercase file created successfully.")

convert_to_uppercase("student.txt", "student_uppercase.txt")


# 17. Create a file containing student records in the format:
# RollNo,Name,Marks
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to:
# • Display all records.
# • Find the student with the highest marks.
# • Calculate average marks.
# • Display students who scored more than 80.
def create_student_records():
    records = [
        ("101", "Amit", 85),
        ("102", "Priya", 92),
        ("103", "Rahul", 78)
    ]

    with open("student_records.txt", "w") as file:
        file.write("RollNo,Name,Marks\n")
        for roll, name, marks in records:
            file.write(f"{roll},{name},{marks}\n")

def read_student_records():
    students = []

    with open("student_records.txt", "r") as file:
        next(file)
        for line in file:
            roll, name, marks = line.strip().split(",")
            students.append((roll, name, int(marks)))

    return students

def process_student_records():
    students = read_student_records()

    print("All records:")
    for student in students:
        print(student)

    highest = max(students, key=lambda student: student[2])
    average = sum(student[2] for student in students) / len(students)

    print("Highest scorer:", highest)
    print("Average marks:", average)

    print("Students scoring more than 80:")
    for student in students:
        if student[2] > 80:
            print(student)

create_student_records()
process_student_records()


# 18. Store employee ID, name, department, and salary in a file.
# Write functions to:
# • Display all employees.
# • Find the highest-paid employee.
# • Calculate average salary.
# • Display employees earning above a given salary.
def create_employee_file():
    employees = [
        ("E101", "Amit", "IT", 55000),
        ("E102", "Priya", "HR", 45000),
        ("E103", "Rahul", "Finance", 70000)
    ]

    with open("employees.txt", "w") as file:
        file.write("ID,Name,Department,Salary\n")
        for emp_id, name, dept, salary in employees:
            file.write(f"{emp_id},{name},{dept},{salary}\n")

def read_employees():
    employees = []

    with open("employees.txt", "r") as file:
        next(file)
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append((emp_id, name, dept, float(salary)))

    return employees

def display_employees():
    for employee in read_employees():
        print(employee)

def highest_paid():
    return max(read_employees(), key=lambda employee: employee[3])

def average_salary():
    employees = read_employees()
    return sum(employee[3] for employee in employees) / len(employees)

def employees_above_salary(amount):
    return [employee for employee in read_employees() if employee[3] > amount]

create_employee_file()
display_employees()
print("Highest paid:", highest_paid())
print("Average salary:", average_salary())
print("Employees above 50000:", employees_above_salary(50000))


# 19. Store student attendance records in a file.
# Calculate the attendance percentage and display students having attendance below 75%.
def create_attendance_file():
    records = [
        ("101", "Amit", 80, 100),
        ("102", "Priya", 65, 100),
        ("103", "Rahul", 72, 90)
    ]

    with open("attendance.txt", "w") as file:
        file.write("RollNo,Name,Present,Total\n")
        for roll, name, present, total in records:
            file.write(f"{roll},{name},{present},{total}\n")

def attendance_report():
    with open("attendance.txt", "r") as file:
        next(file)

        for line in file:
            roll, name, present, total = line.strip().split(",")
            percentage = (int(present) / int(total)) * 100

            print(name, "Attendance:", percentage, "%")

            if percentage < 75:
                print("Below 75%:", name)

create_attendance_file()
attendance_report()


# 20. Store deposits and withdrawals in a file. Read the file and calculate:
# • Total deposits
# • Total withdrawals
# • Final balance
# • Largest transaction
def create_transactions_file():
    transactions = [
        ("Deposit", 5000),
        ("Withdrawal", 1200),
        ("Deposit", 3000),
        ("Withdrawal", 500)
    ]

    with open("transactions.txt", "w") as file:
        for transaction_type, amount in transactions:
            file.write(f"{transaction_type},{amount}\n")

def transaction_report():
    total_deposits = 0
    total_withdrawals = 0
    transactions = []

    with open("transactions.txt", "r") as file:
        for line in file:
            transaction_type, amount = line.strip().split(",")
            amount = float(amount)
            transactions.append(amount)

            if transaction_type == "Deposit":
                total_deposits += amount
            elif transaction_type == "Withdrawal":
                total_withdrawals += amount

    final_balance = total_deposits - total_withdrawals
    largest = max(transactions)

    print("Total deposits:", total_deposits)
    print("Total withdrawals:", total_withdrawals)
    print("Final balance:", final_balance)
    print("Largest transaction:", largest)

create_transactions_file()
transaction_report()


# 21. Maintain book records containing book ID, title, author, and availability status.
# Implement operations to:
# • Add a book.
# • Search for a book.
# • Issue a book.
# • Return a book.
# • Display available books.
books = {}

def add_book(book_id, title, author):
    books[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }

def search_book(book_id):
    return books.get(book_id, "Book not found")

def issue_book(book_id):
    if book_id not in books:
        return "Book not found"

    if not books[book_id]["available"]:
        return "Book is already issued"

    books[book_id]["available"] = False
    return "Book issued successfully"

def return_book(book_id):
    if book_id not in books:
        return "Book not found"

    books[book_id]["available"] = True
    return "Book returned successfully"

def display_available_books():
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["title"], "-", book["author"])

add_book(101, "Python Programming", "John")
add_book(102, "Data Structures", "Robert")
add_book(103, "Cloud Computing", "James")

print(search_book(101))
print(issue_book(101))
print("Available books:")
display_available_books()
print(return_book(101))


# 22. Read the contents of two text files and create a third file containing the contents of both files.
def merge_files(file1, file2, output_file):
    with open(file1, "r") as first:
        content1 = first.read()

    with open(file2, "r") as second:
        content2 = second.read()

    with open(output_file, "w") as output:
        output.write(content1)
        output.write("\n")
        output.write(content2)

    print("Files merged successfully.")

# Example:
# merge_files("file1.txt", "file2.txt", "merged.txt")


# 23. Write a program to compare two text files and display whether their contents
# are identical. If different, identify the first line where they differ.
def compare_files(file1, file2):
    with open(file1, "r") as first:
        lines1 = first.readlines()

    with open(file2, "r") as second:
        lines2 = second.readlines()

    max_lines = max(len(lines1), len(lines2))

    for i in range(max_lines):
        line1 = lines1[i].rstrip("\n") if i < len(lines1) else "<No line>"
        line2 = lines2[i].rstrip("\n") if i < len(lines2) else "<No line>"

        if line1 != line2:
            print("Files are different.")
            print("First different line:", i + 1)
            print("File 1:", line1)
            print("File 2:", line2)
            return

    print("Files are identical.")

# Example:
# compare_files("file1.txt", "file2.txt")


# ============================================================
# PROBLEMS ON MODULE, PACKAGE AND DIRECTORY
# ============================================================

# 1. Create a Python module calculator.py containing functions for addition,
# subtraction, multiplication, and division. Create another program that imports
# the module and performs calculations based on user input.
#
# calculator.py
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

# In main.py:
# import calculator
# print(calculator.addition(10, 5))
# print(calculator.subtraction(10, 5))
# print(calculator.multiplication(10, 5))
# print(calculator.division(10, 5))


# 2. Create a module student.py containing functions to calculate total marks,
# percentage, and grade. Import the module into another Python program and generate
# a student's result.
#
# student.py
def total_marks(marks):
    return sum(marks)

def percentage(marks):
    return sum(marks) / len(marks)

def grade(marks):
    percent = percentage(marks)

    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    return "F"

# In main.py:
# import student
# marks = [85, 90, 78, 88, 92]
# print(student.total_marks(marks))
# print(student.percentage(marks))
# print(student.grade(marks))


# 3. Create a module number_utils.py containing functions to check whether a number
# is prime, palindrome, Armstrong, or perfect. Import the required functions into a main program.
#
# number_utils.py
def check_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def check_number_palindrome(n):
    text = str(n)
    return text == text[::-1]

def check_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n

def check_perfect(n):
    if n <= 1:
        return False

    total = 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total == n

# In main.py:
# from number_utils import check_prime, check_number_palindrome
# from number_utils import check_armstrong, check_perfect
# n = int(input("Enter number: "))
# print(check_prime(n))
# print(check_number_palindrome(n))
# print(check_armstrong(n))
# print(check_perfect(n))


# 4. Create a module string_utils.py containing functions to count vowels,
# reverse a string, check palindrome, count words, and remove spaces.
#
# string_utils.py
def string_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def string_reverse(text):
    return text[::-1]

def string_palindrome(text):
    return text == text[::-1]

def string_word_count(text):
    return len(text.split())

def remove_spaces(text):
    return text.replace(" ", "")

# In main.py:
# from string_utils import *
# text = "Python is easy"
# print(string_vowels(text))
# print(string_reverse(text))
# print(string_palindrome(text))
# print(string_word_count(text))
# print(remove_spaces(text))


# 5. Create a module containing functions to calculate gross salary, deductions,
# and net salary for an employee.
#
# salary.py
def gross_salary(basic, hra_rate=20, da_rate=10):
    hra = basic * hra_rate / 100
    da = basic * da_rate / 100
    return basic + hra + da

def deductions(gross, deduction_rate=10):
    return gross * deduction_rate / 100

def net_salary(basic):
    gross = gross_salary(basic)
    deduction = deductions(gross)
    return gross - deduction

# In main.py:
# from salary import gross_salary, deductions, net_salary
# basic = 50000
# print(gross_salary(basic))
# print(deductions(gross_salary(basic)))
# print(net_salary(basic))


# 6. Create a module containing recursive functions for factorial, Fibonacci series,
# sum of digits, and binary conversion. Import and use these functions from another program.
#
# recursion_utils.py
def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def fibonacci_series(n):
    return [recursive_fibonacci(i) for i in range(n)]

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def decimal_binary(n):
    if n == 0:
        return ""
    return decimal_binary(n // 2) + str(n % 2)

# In main.py:
# from recursion_utils import *
# print(recursive_factorial(5))
# print(fibonacci_series(7))
# print(sum_digits(1234))
# print(decimal_binary(10))


# 7. Create a package named mathutils containing:
# a) basic.py – arithmetic operations
# b) number.py – prime, Armstrong, palindrome functions
# c) statistics.py – mean, maximum, minimum
# Create a main program that imports functions from each module.
#
# Directory:
# mathutils/
#     __init__.py
#     basic.py
#     number.py
#     statistics.py
# main.py
#
# basic.py
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# number.py
# def prime(n):
#     ...
# def armstrong(n):
#     ...
# def palindrome(n):
#     ...
#
# statistics.py
# def mean(numbers):
#     return sum(numbers) / len(numbers)
#
# def maximum(numbers):
#     return max(numbers)
#
# def minimum(numbers):
#     return min(numbers)
#
# main.py:
# from mathutils.basic import add, subtract
# from mathutils.number import prime, armstrong, palindrome
# from mathutils.statistics import mean, maximum, minimum
# print(add(10, 5))
# print(mean([10, 20, 30]))


# 8. Create a package student containing:
# a) marks.py – total and percentage
# b) grade.py – grade calculation
# c) attendance.py – attendance eligibility
# Write a main program that uses all three modules to generate a student report.
#
# Directory:
# student/
#     __init__.py
#     marks.py
#     grade.py
#     attendance.py
#
# marks.py:
# def total(marks):
#     return sum(marks)
#
# def percentage(marks):
#     return sum(marks) / len(marks)
#
# grade.py:
# def grade(percentage):
#     if percentage >= 90:
#         return "A+"
#     elif percentage >= 80:
#         return "A"
#     elif percentage >= 70:
#         return "B"
#     elif percentage >= 60:
#         return "C"
#     else:
#         return "D"
#
# attendance.py:
# def eligible(present, total):
#     return (present / total) * 100 >= 75
#
# main.py:
# from student.marks import total, percentage
# from student.grade import grade
# from student.attendance import eligible
# marks = [80, 85, 90, 75, 88]
# p = percentage(marks)
# print("Total:", total(marks))
# print("Percentage:", p)
# print("Grade:", grade(p))
# print("Attendance Eligible:", eligible(80, 100))


# 9. Develop a package banking containing:
# a) account.py – account creation and balance
# b) transaction.py – deposit and withdrawal
# c) loan.py – loan calculation
# Create a main program to use the package.
#
# banking/
#     __init__.py
#     account.py
#     transaction.py
#     loan.py
#
# account.py:
# class Account:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#
# transaction.py:
# def deposit(account, amount):
#     account.balance += amount
#
# def withdraw(account, amount):
#     if amount <= account.balance:
#         account.balance -= amount
#         return True
#     return False
#
# loan.py:
# def calculate_loan(principal, rate, years):
#     return principal + (principal * rate * years / 100)
#
# main.py:
# from banking.account import Account
# from banking.transaction import deposit, withdraw
# from banking.loan import calculate_loan
# account = Account("Amit", 5000)
# deposit(account, 2000)
# withdraw(account, 1000)
# print(account.balance)
# print(calculate_loan(100000, 8, 2))


# 10. Create a package texttools containing:
# a) cleaning.py – remove punctuation and extra spaces
# b) tokenization.py – tokenize text
# c) frequency.py – word-frequency analysis
# Create a main program to use the package.
#
# texttools/
#     __init__.py
#     cleaning.py
#     tokenization.py
#     frequency.py
#
# cleaning.py:
# import string
#
# def remove_punctuation(text):
#     return text.translate(str.maketrans("", "", string.punctuation))
#
# def remove_extra_spaces(text):
#     return " ".join(text.split())
#
# tokenization.py:
# def tokenize(text):
#     return text.split()
#
# frequency.py:
# def word_frequency(words):
#     result = {}
#     for word in words:
#         result[word] = result.get(word, 0) + 1
#     return result
#
# main.py:
# from texttools.cleaning import remove_punctuation, remove_extra_spaces
# from texttools.tokenization import tokenize
# from texttools.frequency import word_frequency
# text = "Python, is   easy. Python is powerful!"
# text = remove_punctuation(text)
# text = remove_extra_spaces(text)
# words = tokenize(text)
# print(word_frequency(words))


# 11. Create the following directory structure:
# a) college_project/
# b) main.py
# c) student/
# d) __init__.py
# e) details.py
# f) marks.py
# g) faculty/
# h) __init__.py
# i) details.py
# Write a program that imports functions from both packages and displays student
# and faculty information.
#
# Directory:
# college_project/
#     main.py
#     student/
#         __init__.py
#         details.py
#         marks.py
#     faculty/
#         __init__.py
#         details.py
#
# student/details.py:
# def student_info():
#     return "Name: Amit, Roll No: 101"
#
# student/marks.py:
# def student_marks():
#     return [85, 90, 88, 92, 80]
#
# faculty/details.py:
# def faculty_info():
#     return "Faculty: Professor Sharma, Department: CSE"
#
# main.py:
# from student.details import student_info
# from student.marks import student_marks
# from faculty.details import faculty_info
# print(student_info())
# print("Marks:", student_marks())
# print(faculty_info())


# 12. Create a directory structure for a library application with separate packages for:
# a) Books
# b) Members
# c) Transactions
# Each package should contain suitable modules and a main program should combine all functionality.
#
# Directory:
# library/
#     main.py
#     books/
#         __init__.py
#         book.py
#         search.py
#     members/
#         __init__.py
#         member.py
#         search.py
#     transactions/
#         __init__.py
#         issue.py
#         return_book.py
#
# books/book.py:
# def add_book(book_id, title):
#     return {"id": book_id, "title": title}
#
# members/member.py:
# def add_member(member_id, name):
#     return {"id": member_id, "name": name}
#
# transactions/issue.py:
# def issue_book(book, member):
#     return f"{book['title']} issued to {member['name']}"
#
# transactions/return_book.py:
# def return_book(book):
#     return f"{book['title']} returned"
#
# main.py:
# from books.book import add_book
# from members.member import add_member
# from transactions.issue import issue_book
# from transactions.return_book import return_book
# book = add_book(1, "Python Programming")
# member = add_member(101, "Amit")
# print(issue_book(book, member))
# print(return_book(book))


# 13. Create a directory named ecommerce containing packages for:
# a) Products
# b) Customers
# c) Orders
# d) Payments
# Each package should contain at least two modules.
#
# Directory:
# ecommerce/
#     main.py
#     products/
#         __init__.py
#         product.py
#         catalog.py
#     customers/
#         __init__.py
#         customer.py
#         profile.py
#     orders/
#         __init__.py
#         order.py
#         tracking.py
#     payments/
#         __init__.py
#         payment.py
#         invoice.py
#
# products/product.py:
# def create_product(name, price):
#     return {"name": name, "price": price}
#
# products/catalog.py:
# def show_product(product):
#     print(product["name"], product["price"])
#
# customers/customer.py:
# def create_customer(customer_id, name):
#     return {"id": customer_id, "name": name}
#
# customers/profile.py:
# def show_customer(customer):
#     print(customer["id"], customer["name"])
#
# orders/order.py:
# def create_order(product, quantity):
#     return product["price"] * quantity
#
# orders/tracking.py:
# def track_order(order_id):
#     return f"Order {order_id}: In Process"
#
# payments/payment.py:
# def make_payment(amount):
#     return f"Payment of {amount} successful"
#
# payments/invoice.py:
# def generate_invoice(amount):
#     return f"Invoice Amount: {amount}"
#
# main.py:
# from products.product import create_product
# from customers.customer import create_customer
# from orders.order import create_order
# from orders.tracking import track_order
# from payments.payment import make_payment
# from payments.invoice import generate_invoice
#
# product = create_product("Laptop", 50000)
# customer = create_customer(101, "Amit")
# amount = create_order(product, 1)
# print(customer)
# print(amount)
# print(track_order(1))
# print(make_payment(amount))
# print(generate_invoice(amount))


# 14. Create a project directory containing packages for:
# a) Patient management
# b) Doctor management
# c) Billing
# d) Medical records
# Implement simple functions in each module and access them from main.py.
#
# Directory:
# medical_project/
#     main.py
#     patient/
#         __init__.py
#         management.py
#     doctor/
#         __init__.py
#         management.py
#     billing/
#         __init__.py
#         bill.py
#     medical_records/
#         __init__.py
#         records.py
#
# patient/management.py:
# def create_patient(patient_id, name, age):
#     return {"id": patient_id, "name": name, "age": age}
#
# doctor/management.py:
# def create_doctor(doctor_id, name, specialization):
#     return {
#         "id": doctor_id,
#         "name": name,
#         "specialization": specialization
#     }
#
# billing/bill.py:
# def calculate_bill(consultation, laboratory, medicine):
#     return consultation + laboratory + medicine
#
# medical_records/records.py:
# def add_record(patient_id, diagnosis):
#     return {
#         "patient_id": patient_id,
#         "diagnosis": diagnosis
#     }
#
# main.py:
# from patient.management import create_patient
# from doctor.management import create_doctor
# from billing.bill import calculate_bill
# from medical_records.records import add_record
#
# patient = create_patient(101, "Amit", 21)
# doctor = create_doctor(1, "Dr. Sharma", "Cardiology")
# bill = calculate_bill(500, 1000, 800)
# record = add_record(101, "Fever")
#
# print("Patient:", patient)
# print("Doctor:", doctor)
# print("Bill:", bill)
# print("Medical Record:", record)
