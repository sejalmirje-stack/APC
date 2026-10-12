import os
import pandas as pd

# ==========================================
# 1. Student Marks Analysis (DataFrame)
# ==========================================
print("=== 1. Student Marks Analysis ===")
student_data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Python Marks": [85, 90, 65, 78, 92],
    "DBMS Marks": [78, 88, 70, 80, 85],
    "Mathematics Marks": [92, 95, 60, 72, 90],
}
df_students = pd.DataFrame(student_data)
df_students["Total Marks"] = (
    df_students["Python Marks"]
    + df_students["DBMS Marks"]
    + df_students["Mathematics Marks"]
)
df_students["Average Marks"] = df_students["Total Marks"] / 3

print("\nAll Students DataFrame:")
print(df_students)

print("\nStudents with > 75% Average Marks:")
print(df_students[df_students["Average Marks"] > 75])


# ==========================================
# 2. Employee Data Analysis (DataFrame)
# ==========================================
print("\n=== 2. Employee Data Analysis ===")
emp_data = {
    "Employee ID": [1, 2, 3, 4, 5],
    "Employee Name": ["John", "Sarah", "Mike", "Emma", "Alex"],
    "Department": ["IT", "HR", "Finance", "IT", "HR"],
    "Salary": [55000, 48000, 65000, 72000, 45000],
    "Experience": [3, 5, 8, 6, 2],
}
df_emp = pd.DataFrame(emp_data)

print("\nEmployees with salary > ₹50,000:")
print(df_emp[df_emp["Salary"] > 50000])

print(f"\nAverage Salary: ₹{df_emp['Salary'].mean():.2f}")
print(f"Highest Salary: ₹{df_emp['Salary'].max()}")

highest_exp_emp = df_emp.loc[df_emp["Experience"].idxmax()]
print(
    f"Employee with highest experience: {highest_exp_emp['Employee Name']} ({highest_exp_emp['Experience']} years)"
)


# ==========================================
# 3. Product Sales Analysis (DataFrame)
# ==========================================
print("\n=== 3. Product Sales Analysis ===")
prod_data = {
    "Product ID": [201, 202, 203, 204],
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [60000, 800, 1500, 12000],
    "Quantity": [5, 20, 15, 8],
}
df_prod = pd.DataFrame(prod_data)
df_prod["Total Amount"] = df_prod["Price"] * df_prod["Quantity"]

print("\nProduct DataFrame:")
print(df_prod)

highest_sales_prod = df_prod.loc[df_prod["Total Amount"].idxmax()]
print(
    f"\nProduct with highest total sales: {highest_sales_prod['Product Name']} (₹{highest_sales_prod['Total Amount']})"
)


# ==========================================
# 4. Patient Medical Analysis (DataFrame)
# ==========================================
print("\n=== 4. Patient Medical Analysis ===")
patient_data = {
    "Patient ID": [1, 2, 3, 4, 5],
    "Patient Name": ["Ramesh", "Sita", "Gopal", "Anita", "Suresh"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Flu", "Hypertension", "Cold", "Heart Attack"],
    "Medical Charges": [45000, 5000, 80000, 3000, 120000],
}
df_patients = pd.DataFrame(patient_data)

print("\nPatients above 60 years:")
print(df_patients[df_patients["Age"] > 60])

print(f"\nAverage Medical Charge: ₹{df_patients['Medical Charges'].mean():.2f}")
print(f"Maximum Medical Charge: ₹{df_patients['Medical Charges'].max()}")

print("\nPatients with medical charges > ₹50,000:")
print(df_patients[df_patients["Medical Charges"] > 50000])


# ==========================================
# 5. Order Value Analysis (DataFrame)
# ==========================================
print("\n=== 5. Order Value Analysis ===")
order_data = {
    "Order_ID": [1001, 1002, 1003, 1004],
    "Customer": ["Amit", "Priya", "Rahul", "Neha"],
    "Product": ["Phone", "Tablet", "Headphones", "Smartwatch"],
    "Quantity": [1, 2, 3, 1],
    "Price": [20000, 15000, 2000, 8000],
    "Discount": [1000, 2000, 500, 500],
}
df_orders = pd.DataFrame(order_data)
df_orders["Final Amount"] = (
    df_orders["Quantity"] * df_orders["Price"] - df_orders["Discount"]
)

print("\nAll Orders:")
print(df_orders)

print("\nOrders above ₹5,000:")
print(df_orders[df_orders["Final Amount"] > 5000])

highest_order = df_orders.loc[df_orders["Final Amount"].idxmax()]
print(
    f"\nHighest-value Order: Order ID {highest_order['Order_ID']} (₹{highest_order['Final Amount']})"
)
print(f"Average Order Value: ₹{df_orders['Final Amount'].mean():.2f}")


# ==========================================
# 6. Student Attendance Analysis (DataFrame)
# ==========================================
print("\n=== 6. Student Attendance Analysis ===")
attendance_data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Karan", "Simran", "Raj", "Pooja", "Vikram"],
    "Department": ["CS", "IT", "CS", "ECE", "IT"],
    "Total_Classes": [50, 50, 50, 50, 50],
    "Classes_Attended": [42, 35, 48, 30, 38],
}
df_attendance = pd.DataFrame(attendance_data)
df_attendance["Attendance Percentage"] = (
    df_attendance["Classes_Attended"] / df_attendance["Total_Classes"]
) * 100

print("\nStudents with attendance below 75%:")
print(df_attendance[df_attendance["Attendance Percentage"] < 75])


# ==========================================
# 7. Retail Shop Sales Analysis (DataFrame)
# ==========================================
print("\n=== 7. Retail Shop Sales Analysis ===")
retail_data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["TV", "Speaker", "AC", "Microwave", "Fan"],
    "Category": [
        "Electronics",
        "Audio",
        "Appliances",
        "Appliances",
        "Appliances",
    ],
    "Price": [30000, 4000, 40000, 8000, 2500],
    "Quantity": [2, 5, 1, 3, 2],
}
df_retail = pd.DataFrame(retail_data)
df_retail["Total_Sales"] = df_retail["Price"] * df_retail["Quantity"]

print("\nProducts with sales > ₹10,000:")
print(df_retail[df_retail["Total_Sales"] > 10000])

max_sales_prod = df_retail.loc[df_retail["Total_Sales"].idxmax()]
print(
    f"\nProduct with maximum sales: {max_sales_prod['Product_Name']} (₹{max_sales_prod['Total_Sales']})"
)
print(f"Average Sales: ₹{df_retail['Total_Sales'].mean():.2f}")


# ==========================================
# 8. Student Marks Analysis (Pandas Series)
# ==========================================
print("\n=== 8. Student Marks Analysis (Series) ===")
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 68,
    "David": 74,
    "Eva": 95,
}
s_student_marks = pd.Series(student_marks)

print("\nSeries Output:")
print(s_student_marks)

print(f"\nMarks of Bob: {s_student_marks['Bob']}")
print(f"Maximum Marks: {s_student_marks.max()}")
print(f"Minimum Marks: {s_student_marks.min()}")
print(f"Average Marks: {s_student_marks.mean():.2f}")

print("\nStudents who scored > 75:")
print(s_student_marks[s_student_marks > 75])


# ==========================================
# 9. Employee Salary Analysis (Pandas Series)
# ==========================================
print("\n=== 9. Employee Salary Analysis (Series) ===")
emp_salaries = {
    "John": 55000,
    "Sarah": 48000,
    "Mike": 65000,
    "Emma": 72000,
    "Alex": 45000,
}
s_emp_salaries = pd.Series(emp_salaries)

print("\nSeries Output:")
print(s_emp_salaries)

print(f"\nHighest Salary: ₹{s_emp_salaries.max()}")
print(f"Lowest Salary: ₹{s_emp_salaries.min()}")
print(f"Average Salary: ₹{s_emp_salaries.mean():.2f}")

print("\nEmployees earning > ₹50,000:")
print(s_emp_salaries[s_emp_salaries > 50000])


# ==========================================
# 10. Product Price Analysis (Pandas Series)
# ==========================================
print("\n=== 10. Product Price Analysis (Series) ===")
prod_prices = {
    "Book": 400,
    "Backpack": 1200,
    "Pen": 50,
    "Shoes": 2500,
    "Watch": 1800,
}
s_prod_prices = pd.Series(prod_prices)

print("\nOriginal Products and Prices:")
print(s_prod_prices)

s_prod_prices_increased = s_prod_prices * 1.10
print("\nPrices increased by 10%:")
print(s_prod_prices_increased)

print(
    f"\nMost expensive product: {s_prod_prices.idxmax()} (₹{s_prod_prices.max()})"
)

print("\nProducts costing > ₹1,000 (original prices):")
print(s_prod_prices[s_prod_prices > 1000])


# ==========================================
# 11. Patient Age Analysis (Pandas Series)
# ==========================================
print("\n=== 11. Patient Age Analysis (Series) ===")
patient_ages = {
    "P101": 45,
    "P102": 68,
    "P103": 29,
    "P104": 74,
    "P105": 61,
}
s_patient_ages = pd.Series(patient_ages)

print(f"\nAverage Age: {s_patient_ages.mean():.2f} years")
print(
    f"Oldest Patient ID: {s_patient_ages.idxmax()} (Age: {s_patient_ages.max()})"
)
print(
    f"Youngest Patient ID: {s_patient_ages.idxmin()} (Age: {s_patient_ages.min()})"
)

print("\nPatients above 60 years:")
print(s_patient_ages[s_patient_ages > 60])


# ==========================================
# 12. Student Attendance Analysis (Pandas Series)
# ==========================================
print("\n=== 12. Student Attendance Analysis (Series) ===")
student_attendance = {
    "Karan": 88.5,
    "Simran": 72.0,
    "Raj": 94.0,
    "Pooja": 60.5,
    "Vikram": 91.0,
}
s_attendance = pd.Series(student_attendance)

print(f"\nAverage Attendance: {s_attendance.mean():.2f}%")

print("\nStudents with attendance < 75%:")
print(s_attendance[s_attendance < 75])

print("\nStudents with attendance > 90%:")
print(s_attendance[s_attendance > 90])

print(
    f"\nHighest Attendance: {s_attendance.idxmax()} ({s_attendance.max()}%)"
)


# ==========================================
# HELPER: Generate CSV Files for Tasks 13-16
# ==========================================
def create_sample_csv_files():
    pd.DataFrame(
        {
            "Student_ID": [101, 102, 103, 104, 105, 106],
            "Name": [
                "Aarav",
                "Bhavna",
                "Chetan",
                "Divya",
                "Esha",
                "Farhan",
            ],
            "Department": ["CSE", "ECE", "CSE", "MECH", "CSE", "ECE"],
            "Python": [85, 92, 70, 60, 95, 88],
            "DBMS": [80, 88, 65, 55, 90, 82],
            "Maths": [90, 95, 72, 58, 92, 80],
        }
    ).to_csv("students.csv", index=False)

    pd.DataFrame(
        {
            "Employee_ID": [1, 2, 3, 4, 5, 6],
            "Name": [
                "Amit",
                "Bina",
                "Chirag",
                "Deepa",
                "Eshwar",
                "Firoza",
            ],
            "Department": ["CSE", "ECE", "CSE", "MECH", "CSE", "ECE"],
            "Experience": [5, 3, 8, 2, 10, 4],
            "Salary": [60000, 45000, 85000, 40000, 95000, 52000],
        }
    ).to_csv("employees.csv", index=False)

    pd.DataFrame(
        {
            "Patient_ID": [101, 102, 103, 104, 105, 106],
            "Name": [
                "Ramesh",
                "Sita",
                "Gopal",
                "Anita",
                "Suresh",
                "Meena",
            ],
            "Age": [65, 45, 72, 30, 61, 55],
            "Gender": ["M", "F", "M", "F", "M", "F"],
            "Disease": [
                "Diabetes",
                "Flu",
                "Hypertension",
                "Flu",
                "Diabetes",
                "Diabetes",
            ],
            "Medical_Expense": [45000, 5000, 80000, 3000, 120000, 60000],
        }
    ).to_csv("patients.csv", index=False)

    pd.DataFrame(
        {
            "Date": [
                "2026-05-01",
                "2026-05-01",
                "2026-05-02",
                "2026-05-02",
                "2026-05-03",
            ],
            "City": [
                "Mumbai",
                "Delhi",
                "Mumbai",
                "Delhi",
                "Kolhapur",
            ],
            "Temperature": [34, 38, 36, 40, 32],
            "Humidity": [70, 40, 68, 38, 60],
            "Rainfall": [0, 0, 5, 0, 12],
        }
    ).to_csv("weather.csv", index=False)


create_sample_csv_files()


# ==========================================
# 13. students.csv Analysis
# ==========================================
print("\n=== 13. CSV Analysis: students.csv ===")
df_csv_students = pd.read_csv("students.csv")

print("\nFirst 5 Records:")
print(df_csv_students.head(5))

print("\nLast 5 Records:")
print(df_csv_students.tail(5))

df_csv_students["Total_Marks"] = (
    df_csv_students["Python"]
    + df_csv_students["DBMS"]
    + df_csv_students["Maths"]
)
df_csv_students["Average_Marks"] = df_csv_students["Total_Marks"] / 3

print("\nStudent Data with Total and Average Marks:")
print(df_csv_students[["Name", "Total_Marks", "Average_Marks"]])

print("\nStudents with Average Marks > 75:")
print(df_csv_students[df_csv_students["Average_Marks"] > 75])

top_student = df_csv_students.loc[df_csv_students["Average_Marks"].idxmax()]
print(
    f"\nStudent with Highest Average: {top_student['Name']} ({top_student['Average_Marks']:.2f})"
)

print("\nAverage Marks for each Subject:")
print(f"Python: {df_csv_students['Python'].mean():.2f}")
print(f"DBMS:   {df_csv_students['DBMS'].mean():.2f}")
print(f"Maths:  {df_csv_students['Maths'].mean():.2f}")


# ==========================================
# 14. employees.csv Analysis
# ==========================================
print("\n=== 14. CSV Analysis: employees.csv ===")
df_csv_emp = pd.read_csv("employees.csv")

print("\nEmployees from CSE Department:")
print(df_csv_emp[df_csv_emp["Department"] == "CSE"])

print(f"\nAverage Salary: ₹{df_csv_emp['Salary'].mean():.2f}")
print(f"Highest Salary: ₹{df_csv_emp['Salary'].max()}")
print(f"Lowest Salary:  ₹{df_csv_emp['Salary'].min()}")

print("\nEmployees with Salary > ₹50,000:")
print(df_csv_emp[df_csv_emp["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df_csv_emp.groupby("Department")["Salary"].mean())


# ==========================================
# 15. patients.csv Analysis
# ==========================================
print("\n=== 15. CSV Analysis: patients.csv ===")
df_csv_patients = pd.read_csv("patients.csv")

print("\nPatients above 60 years:")
print(df_csv_patients[df_csv_patients["Age"] > 60])

print(
    f"\nAverage Medical Expense: ₹{df_csv_patients['Medical_Expense'].mean():.2f}"
)

top_expense_patient = df_csv_patients.loc[
    df_csv_patients["Medical_Expense"].idxmax()
]
print(
    f"Patient with Highest Medical Expense: {top_expense_patient['Name']} (₹{top_expense_patient['Medical_Expense']})"
)

print("\nPatient count for each disease:")
print(df_csv_patients["Disease"].value_counts())

print("\nPatients whose Medical Expense exceeds ₹50,000:")
print(df_csv_patients[df_csv_patients["Medical_Expense"] > 50000])


# ==========================================
# 16. weather.csv Analysis
# ==========================================
print("\n=== 16. CSV Analysis: weather.csv ===")
df_csv_weather = pd.read_csv("weather.csv")

print(f"\nMaximum Temperature: {df_csv_weather['Temperature'].max()}°C")
print(f"Minimum Temperature: {df_csv_weather['Temperature'].min()}°C")
print(f"Average Temperature: {df_csv_weather['Temperature'].mean():.2f}°C")

print("\nRecords where Temperature > 35°C:")
print(df_csv_weather[df_csv_weather["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df_csv_weather.groupby("City")["Temperature"].mean())