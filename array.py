#1. Create and display an array
from array import array
arr = array('i', [10, 20, 30, 40, 50])
print("Array:", arr)


#2. Access array elements
from array import array
arr = array('i', [10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])

    
#3. Traverse an array
from array import array
arr = array('i', [10, 20, 30, 40, 50])
for i in arr:
    print(i)
    

#4.Add an element using append()
from array import array
arr = array('i', [10, 20, 30])
arr.append(40)
print("Updated array:", arr)


#5. Insert an element using insert()
from array import array
arr = array('i', [10, 20, 40, 50])
arr.insert(2, 30)
print("Updated array:", arr)


#6. Remove an element using remove()
from array import array
arr = array('i', [10, 20, 30, 40, 50])
arr.remove(30)
print("Updated array:", arr)


#7. Find the index of an element
from array import array
arr = array('i', [10, 20, 30, 40, 50])
n = int(input("Enter element: "))
if n in arr:
    print("Index:", arr.index(n))
else:
    print("Element not found")
    
    
#8. Reverse an array
from array import array
arr = array('i', [10, 20, 30, 40, 50])
arr.reverse()
print("Reversed array:", arr)


#9. Find sum of array elements
from array import array
arr = array('i', [10, 20, 30, 40, 50])
total = sum(arr)
print("Sum:", total)


#10. Find largest and smallest element
from array import array
arr = array('i', [25, 10, 45, 5, 30])
print("Largest:", max(arr))
print("Smallest:", min(arr))


#11. Search for an element
from array import array
arr = array('i', [10, 20, 30, 40, 50])
n = int(input("Enter element to search: "))
if n in arr:
    print("Element found")
else:
    print("Element not found")