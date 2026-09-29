# 1. Create a class Student with attributes such as roll_no, name, and marks.
# Create objects for multiple students and display their details and percentage.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage(), "%")
        print()

students = [
    Student(101, "Amit", [85, 90, 78, 88, 92]),
    Student(102, "Priya", [92, 88, 95, 90, 94]),
    Student(103, "Rahul", [75, 80, 72, 78, 85])
]

for student in students:
    student.display()


# 2. Create a class Employee with attributes emp_id, name, and basic_salary.
# Define methods to calculate HRA, DA, and gross salary.
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())

employee = Employee(1001, "Amit", 50000)
employee.display()


# 3. Create a class Rectangle with attributes length and breadth.
# Define methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle = Rectangle(10, 5)

print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())


# 4. Create a class Circle with an attribute radius.
# Define methods to calculate the area and circumference of the circle.
class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius * self.radius

    def circumference(self):
        return 2 * self.PI * self.radius

circle = Circle(7)

print("Circle Area:", circle.area())
print("Circle Circumference:", circle.circumference())


# 5. Create a class Book containing book_id, title, author, and price.
# Create objects for three books and display their information.
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()

books = [
    Book(101, "Python Programming", "John Smith", 550),
    Book(102, "Data Structures", "Robert Brown", 650),
    Book(103, "Cloud Computing", "James Wilson", 750)
]

for book in books:
    book.display()


# 6. Create a class ElectricityBill containing consumer number, consumer name,
# and units consumed. Define a method to calculate the electricity bill
# according to different unit slabs.
class ElectricityBill:
    def __init__(self, consumer_number, consumer_name, units):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.5
        elif self.units <= 200:
            bill = (100 * 1.5) + ((self.units - 100) * 2.5)
        elif self.units <= 500:
            bill = (100 * 1.5) + (100 * 2.5) + ((self.units - 200) * 4)
        else:
            bill = (100 * 1.5) + (100 * 2.5) + (300 * 4)
            bill += (self.units - 500) * 6

        return bill

    def display_bill(self):
        print("Consumer Number:", self.consumer_number)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())

consumer = ElectricityBill(1001, "Amit", 350)
consumer.display_bill()


# 7. Create a class MobilePhone with attributes brand, model, storage, and price.
# Define methods to display specifications and calculate the price after discount.
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specifications(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        return self.price - (self.price * discount / 100)

phone = MobilePhone("Samsung", "Galaxy A55", "256 GB", 40000)

phone.display_specifications()
print("Price after 10% discount:", phone.price_after_discount(10))


# 8. Create a class Patient containing patient ID, name, age, disease,
# and consultation fee. Define methods to display patient information
# and calculate the total bill.
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_information(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, laboratory=0, medicine=0, room=0):
        return self.consultation_fee + laboratory + medicine + room

patient = Patient(101, "Priya", 22, "Fever", 500)

patient.display_information()
print("Total Bill:", patient.total_bill(1000, 800, 2000))


# 9. Design an ATM class that allows a user to:
# a) Check balance
# b) Deposit money
# c) Withdraw money
# d) Display account details
# Create an object of the class and implement the operations through a menu-driven program.
class ATM:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm = ATM("ACC1001", "Amit", 10000)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.check_balance()

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)

    elif choice == "4":
        atm.display_account_details()

    elif choice == "5":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")


# 10. Create a class Vehicle containing vehicle number, model, rental rate,
# and availability. Implement methods to rent and return a vehicle and
# calculate rental charges based on the number of days.
class Vehicle:
    def __init__(self, vehicle_number, model, rental_rate):
        self.vehicle_number = vehicle_number
        self.model = model
        self.rental_rate = rental_rate
        self.availability = True

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Model:", self.model)
        print("Rental Rate per Day:", self.rental_rate)
        print("Available:", self.availability)

vehicle = Vehicle("MH09AB1234", "Swift", 1500)

vehicle.display()
vehicle.rent()
print("Rental Charges for 3 days:", vehicle.rental_charges(3))
vehicle.return_vehicle()
vehicle.display()


# 11. Create a class ShoppingCart with customer name and cart ID.
# Initialize these values using a constructor. Implement methods to add products,
# remove products, and calculate the total bill. Use a destructor to display
# a message when the shopping cart object is destroyed.
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price, quantity):
        self.products[name] = {
            "price": price,
            "quantity": quantity
        }
        print(name, "added to cart.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(name, "removed from cart.")
        else:
            print("Product not found.")

    def calculate_total(self):
        total = 0

        for product in self.products.values():
            total += product["price"] * product["quantity"]

        return total

    def display_cart(self):
        print("Customer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)

        for name, product in self.products.items():
            print(
                name,
                "Price:", product["price"],
                "Quantity:", product["quantity"]
            )

        print("Total Bill:", self.calculate_total())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Amit", "CART101")

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 800, 2)
cart.add_product("Keyboard", 1500, 1)

cart.display_cart()

cart.remove_product("Mouse")
print("Total after removing Mouse:", cart.calculate_total())

del cart


# 12. Create a class FoodOrder with order ID, customer name, food item,
# quantity, and price. Use a constructor to initialize the order.
# Define a method to calculate the total bill including tax.
# Implement a destructor to display an order completion message.
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def calculate_total(self, tax_rate=5):
        subtotal = self.quantity * self.price
        tax = subtotal * tax_rate / 100
        return subtotal + tax

    def display_order(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per Item:", self.price)
        print("Total Bill including tax:", self.calculate_total())

    def __del__(self):
        print("Order", self.order_id, "completed.")


order = FoodOrder(501, "Priya", "Pizza", 2, 300)
order.display_order()

del order


# 13. Create a class StudentResult with student name and marks in five subjects.
# Use a constructor to initialize the details. Define methods to calculate total,
# percentage, and grade. Implement a destructor to display a suitable message.
class StudentResult:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        print("Student Name:", self.student_name)
        print("Marks:", self.marks)
        print("Total:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")
        print("Grade:", self.calculate_grade())

    def __del__(self):
        print("Student result object destroyed.")


result = StudentResult("Rahul", [85, 90, 78, 88, 92])
result.display_result()

del result
