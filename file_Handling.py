
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

# 1. Create a Python module calculator.py containing functions for addition,
# subtraction, multiplication, and division. Create another program that imports
# the module and performs calculations based on user input.
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
# print("Patient:", patient)
# print("Doctor:", doctor)
# print("Bill:", bill)
# print("Medical Record:", record)
