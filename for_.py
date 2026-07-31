#Write a PYTHON program to print the natural numbers up to n
num  = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i, end=' ')
    
#Write a PYTHON program to print even numbers up to n
num = int(input("\nEnter a number: "))
for i in range(2, num + 1, 2):
    print(i, end=' ')
    
    
#Write a PYTHON program to print odd numbers up to n
n = int(input("Enter the value of n: "))
for i in range(1, n + 1, 2):
    print(i, end=" ")
    

#Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n = int(input("Enter the value of n: "))
limit = n ** 2
for exponent in range(limit + 1):
    val = 2 ** exponent
    if val <= limit:
        print(val, end=" ")
    else:
        break


#Write a PYTHON program to sum the given sequence
      #1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!

n = int(input("Enter the value of n: "))
sum = 1.0 
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    sum += 1 / factorial

print("The sum of the sequence is:", sum)



#Write a PYTHON program to compute the cosine series
         # cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))
cos_sum = 1.0
sign = -1
for i in range(1, n):
    power = 2 * i
    num = x ** power
    fact = 1
    for j in range(1, power + 1):
        fact *= j
    cos_sum += sign * (num / fact)
    sign = -sign  
print("Cosine value:", cos_sum)



#Write a short PYTHON program to check weather the square root of number is prime or  not.
num = int(input("Enter an integer: "))
sqrt = int(num ** 0.5)
is_prime = True
if sqrt < 2:
    is_prime = False
else:
    for i in range(2, sqrt):
        if sqrt % i == 0:
            is_prime = False
            break
if is_prime:
    print("Yes, the square root is prime.")
else:
    print("No, the square root is not prime.")



#Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 
for i in range(3):
    print("A B C")
    
    



#Write a PYTHON program to produce following design
     # A
      #A B
      #A B C
      #A B C D 
      #A B C D E
      #If user enters n value as 5

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


'''Write a PYTHON program to produce following design
       A B C D E
       A B C D
       A B C
       A B
       A                      
      (If user enters n value as 5)'''
      
n = int(input("Enter the value of n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
      
      

'''Write a PYTHON program to produce following  
      design
      1
      1 2
      1 2 3
      1 2 3 4
      1 2 3 4 5
      If user enters n value as 5'''
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


'''Write a PYTHON program to produce following design
      1
      2 2
      3 3 3
      4 4 4 4 
      5 5 5 5 5
      If user enters n value as 5'''
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
    



