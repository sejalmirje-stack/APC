#print a right angled tringle using *
n = 5
for i in range(1, n + 1):
    print("*" * i)
    
    
#count lines,words and characters  
line_c = 0
word_c= 0
char_c= 0
with open('sample.txt', 'w') as file:
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("Each line has several words.\n")
with open('sample.txt', 'r') as file:
    for line in file:
        line_c += 1
        words = line.split() 
        word_c += len(words)
        char_c+= len(line)
print ("Lines: ", line_c)
print ("Words: ", word_c)
print ("Characters: ", char_c)  



# Analyze employee data using pandas
import pandas as pd
data = {
    'Employee': ['Amit', 'Priya', 'Rahul', 'Sneha', 'Vikas'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'Salary': [50000, 40000, 70000, 60000, 45000]
}
df = pd.DataFrame(data)
print("Highest Salary:", df['Salary'].max())
print("\nHighest Paid Employee:")
print("\nAverage Salary:", df['Salary'].mean())
print("\nDepartment-wise Average Salary:")
print(df.groupby('Department')['Salary'].sum())
    