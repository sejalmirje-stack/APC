#1.	String Length 
#Write a program to input a string and display its length without using the len() function. 
s = input("Enter a string: ")
count = 0
for i in s:
    count += 1
print("Length =", count)


#2.	Character Count 
#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
s = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


#3.	Reverse a String 
#Reverse the given string without using built-in reverse functions. 
s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev
print("Reverse =", rev)



#Palindrome Check 
#Check whether the entered string is a palindrome.
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome") 
    
    
#5.	Uppercase and Lowercase Count 
#Count the number of uppercase and lowercase letters in a string
s = input("Enter a string: ")
upper = lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)



#6.	Replace Characters 
#Replace all occurrences of a given character with another character. 
s = input("Enter a string: ")
old = input("Character to replace: ")
new = input("New character: ")
print(s.replace(old, new))


#Remove Spaces 
#Remove all spaces from the input string. 
s = input("Enter a string: ")
print("Without spaces:", s.replace(" ", ""))


#8.	Frequency of a Character 
#Find the number of times a specified character appears in a string
s = input("Enter a string: ")
ch = input("Enter character: ")
print("Frequency =", s.count(ch))



#9.	 First and Last Character 
#Print the first and last character of a string. 
s = input("Enter a string: ")
print("First =", s[0])
print("Last =", s[-1])


#10.	ASCII Values 
#Display each character of a string along with its ASCII value.
s = input("Enter a string: ")
for ch in s:
    print(ch, "=", ord(ch))
    
    
    
#11.	Word Count 
#a.	Count the total number of words in a sentence. 
s = input("Enter a sentence: ")
words = s.split()
print("Total words =", len(words))



#12.	Longest Word 
#a.	Find the longest word in a given sentence. 
s = input("Enter a sentence: ")
words = s.split()
longest = max(words, key=len)
print("Longest word =", longest)


#13.	Shortest Word 
#a.	Find the shortest word in a sentence. 
s = input("Enter a sentence: ")
words = s.split()
shortest = min(words, key=len)
print("Shortest word =", shortest)


#14.	Title Case 
#a.	Convert the first letter of every word to uppercase. 
s = input("Enter a sentence: ")
print(s.title())



#15.	Duplicate Characters 
#a.	Print all duplicate characters in a string
string = input("Enter a string: ")
printed = ""
for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count += 1
    if count > 1 and string[i] not in printed:
        print(string[i])
        printed += string[i]
        


#16.	Character Frequency 
#a.	Display the frequency of every character in a string. 
string=input("enter a string: ")
checked=""
for ch in string:
    if ch not in checked:
        count=0
        for c in string:
            if ch==c:
                count+=1
        print(ch,":",count)
        checked+=ch
        
        

#17.	Anagram Check 
#a.	Check whether two strings are anagrams. 
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
    


#18.	Remove Duplicate Characters 
#a.	Remove duplicate characters while maintaining the original order. 
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)



#19.	Substring Search 
#a.	Check whether a given substring exists in the main string. 
s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring found")
else:
    print("Not found")
    
    
#20.	Count Occurrences of a Word 
#a.	Count how many times a specific word appears in a sentence. 
s = input("Enter a sentence: ")
word = input("Enter word: ")
print("Count =", s.split().count(word))



'''21.	Password Validator
•	Validate a password based on these conditions: 
o	Minimum 8 characters 
o	At least one uppercase letter 
o	One lowercase letter 
o	One digit 
o	One special character
'''
password = input("Enter password: ")
upper = lower = digit = special = False
for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")
    

'''22.	Run-Length Encoding
•	Compress a string by counting consecutive repeated characters. 
•	Example:
	Input: aaabbccccd
	Output: a3b2c4d1
'''
s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
result += s[-1] + str(count)
print(result)



'''23.	String Compression 
•	Compress repeated characters and return the original string if compression does not reduce the length. 
'''
s = input("Enter string: ")
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
result += s[-1] + str(count)
if len(result) < len(s):
    print(result)
else:
    print(s)


'''24.	Most Frequent Character 
•	Find the character with the highest frequency. 
'''
string = input("Enter a string: ")
max_char = ""
max_count = 0
for ch in string:
    count = 0
    for c in string:
        if ch == c:
            count += 1
    if count > max_count:
        max_count = count
        max_char = ch
print("Character with highest frequency:", max_char)
print("Frequency:", max_count)



'''25.	Second Most Frequent Character 
•	Find the second most frequently occurring character. 
'''
string = input("Enter a string: ")
freq = {}
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
first_char = ""
second_char = ""
first_count = 0
second_count = 0
for ch in freq:
    if freq[ch] > first_count:
        second_count = first_count
        second_char = first_char
        first_count = freq[ch]
        first_char = ch
    elif freq[ch] > second_count and freq[ch] != first_count:
        second_count = freq[ch]
        second_char = ch
if second_char != "":
    print("Second most frequent character:", second_char)
    print("Frequency:", second_count)
else:
    print("No second most frequent character found.")
    
    

'''26.	Caesar Cipher 
•	Encrypt and decrypt a message using the Caesar Cipher algorithm. 
'''
# 26. Caesar Cipher
# Shift logic.
msg = input("Message: ")
shift = int(input("Shift: "))
enc = ""
for ch in msg:
    if ch.isalpha():
        base = 65 if ch.isupper() else 97
        enc += chr((ord(ch) - base + shift) % 26 + base)
    else:
        enc += ch
print("Encrypted:", enc)



'''27.	Email Validator 
•	Validate whether a given email address follows a valid format. 
'''
email = input("Enter email: ")
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
    


'''28.	Word Frequency Dictionary 
•	Count the frequency of every word in a paragraph. 
'''
s = input("Enter paragraph: ")
words = s.split()
freq = {}
for word in words:
    freq[word] = freq.get(word,0)+1
print(freq)



'''29.	Sentence Reversal 
•	Reverse the order of words in a sentence without changing the words themselves. 
•	Example:
•	Input: Python is easy
Output: easy is Python
'''
s = input("Enter sentence: ")
words = s.split()
print(" ".join(words[::-1]))



'''30.	String Rotation 
•	Check whether one string is a rotation of another. 
•	Example:
•	ABCD
•	CDAB
Output: Yes
'''
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1)==len(s2) and s2 in s1+s1:
    print("Yes")
else:
    print("No")