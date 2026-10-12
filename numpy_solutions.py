
# Q1
header(1, "1-D array of 10 integers: size, dtype, ndim")
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Array           :", arr)
print("Size            :", arr.size)
print("Data type       :", arr.dtype)
print("No. of dimensions:", arr.ndim)

# Q2
header(2, "Arithmetic operations on two arrays")
a = np.array([10, 20, 30, 40, 50])
b = np.array([3, 4, 5, 6, 7])
print("a =", a, "\nb =", b)
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)


# Q3
header(3, "Max, min, sum, average")
arr = np.array([12, 45, 7, 23, 89, 34, 56, 2, 67, 41])
print("Array   :", arr)
print("Maximum :", arr.max())
print("Minimum :", arr.min())
print("Sum     :", arr.sum())
print("Average :", arr.mean())


# Q4
header(4, "Boolean indexing: even and odd numbers (1 to 20)")
arr = np.arange(1, 21)
print("Array :", arr)
print("Even  :", arr[arr % 2 == 0])
print("Odd   :", arr[arr % 2 != 0])


# Q5
header(5, "Reshape 1..12 into 2x6, 3x4, 4x3")
arr = np.arange(1, 13)
print("Original:", arr)
print("\n2 x 6:\n", arr.reshape(2, 6))
print("\n3 x 4:\n", arr.reshape(3, 4))
print("\n4 x 3:\n", arr.reshape(4, 3))


# Q6
header(6, "Matrix addition (3x3)")
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)
print("Sum:\n", np.add(m1, m2))


# Q7
header(7, "Matrix multiplication (2x3 @ 3x2)")
m1 = np.array([[1, 2, 3], [4, 5, 6]])       # 2 x 3
m2 = np.array([[7, 8], [9, 10], [11, 12]])  # 3 x 2
print("Matrix 1 (2x3):\n", m1)
print("Matrix 2 (3x2):\n", m2)
print("Product (2x2) using np.dot():\n", np.dot(m1, m2))
print("Same using np.matmul():\n", np.matmul(m1, m2))


# Q8
header(8, "Transpose of a 3x4 matrix")
m = np.arange(1, 13).reshape(3, 4)
print("Original (3x4):\n", m)
print("Transpose (4x3):\n", m.T)


# Q9
header(9, "Indexing a 4x4 array")
m = np.arange(1, 17).reshape(4, 4)
print("Array:\n", m)
print("First row               :", m[0])
print("Last column             :", m[:, -1])
print("Diagonal elements       :", np.diag(m))
print("Second and third rows   :\n", m[1:3])


# Q10
header(10, "Row-wise and column-wise sum of a 4x4 matrix")
m = np.arange(1, 17).reshape(4, 4)
print("Matrix:\n", m)
print("Sum of each row    :", m.sum(axis=1))
print("Sum of each column :", m.sum(axis=0))


# Q11
header(11, "Slicing on numbers 1 to 20")
arr = np.arange(1, 21)
print("Array              :", arr)
print("First 5 elements   :", arr[:5])
print("Last 5 elements    :", arr[-5:])
print("Alternate elements :", arr[::2])
print("Reverse order      :", arr[::-1])


# Q12
header(12, "Replace elements > 50 with 0")
arr = np.array([12, 55, 78, 34, 90, 21, 51, 49, 65, 8])
print("Before:", arr)
arr[arr > 50] = 0
print("After :", arr)

# Q13
header(13, "Sort ascending and descending")
arr = np.array([45, 12, 89, 3, 67, 23, 90, 1])
print("Unsorted   :", arr)
print("Ascending  :", np.sort(arr))
print("Descending :", np.sort(arr)[::-1])


# Q14
header(14, "Unique elements")
arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 6])
print("Array  :", arr)
print("Unique :", np.unique(arr))


# Q15
header(15, "Concatenate horizontally and vertically")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("a:\n", a)
print("b:\n", b)
print("Horizontal (hstack):\n", np.hstack((a, b)))
print("Vertical (vstack):\n", np.vstack((a, b)))
print("Using np.concatenate axis=1:\n", np.concatenate((a, b), axis=1))
print("Using np.concatenate axis=0:\n", np.concatenate((a, b), axis=0))


# Q16
header(16, "Statistics of marks of 10 students")
marks = np.array([78, 85, 92, 67, 74, 88, 95, 60, 81, 70])
print("Marks              :", marks)
print("Highest marks      :", marks.max())
print("Lowest marks       :", marks.min())
print("Average marks      :", marks.mean())
print("Median             :", np.median(marks))
print("Standard deviation :", round(marks.std(), 2))


# Q17
header(17, "Marks of 20 students above class average")
marks = np.array([56, 78, 90, 45, 67, 88, 92, 34, 71, 65,
                  80, 59, 73, 84, 96, 41, 62, 77, 69, 83])
avg = marks.mean()
print("Marks         :", marks)
print("Class average:", avg)
print("Scored above average:", marks[marks > avg])

# Q18
header(18, "3-D array (2,3,4) with numbers 1 to 24")
arr3 = np.arange(1, 25).reshape(2, 3, 4)
print(arr3)
print("Number of dimensions:", arr3.ndim)
print("Shape               :", arr3.shape)
print("Size                :", arr3.size)


# Q19
header(19, "Accessing elements of a (2,3,4) array")
arr3 = np.arange(1, 25).reshape(2, 3, 4)
print(arr3)
print("First element        :", arr3[0, 0, 0])
print("Last element         :", arr3[-1, -1, -1])
print("Element at [0,1,2]   :", arr3[0, 1, 2])
print("Element at [1,2,3]   :", arr3[1, 2, 3])


# Q20
header(20, "Sums on a (2,3,4) array")
arr3 = np.arange(1, 25).reshape(2, 3, 4)
print(arr3)
print("Sum of all elements       :", arr3.sum())
print("Sum of each layer (axis 0 blocks):", arr3.sum(axis=(1, 2)))
print("Sum along rows (axis=2)   :\n", arr3.sum(axis=2))
print("Sum along columns (axis=1):\n", arr3.sum(axis=1))


# Q21
header(21, "Random 3-D array (1-100): replace values > 50 with 0")
arr3 = np.random.randint(1, 101, size=(2, 3, 4))
print("Before:\n", arr3)
arr3[arr3 > 50] = 0
print("After:\n", arr3)


# Q22
header(22, "Statistics of random 3-D array (3,4,5)")
arr3 = np.random.randint(1, 101, size=(3, 4, 5))
print(arr3)
print("Mean               :", arr3.mean())
print("Median             :", np.median(arr3))
print("Standard deviation :", arr3.std())
print("Variance           :", arr3.var())
print("Minimum            :", arr3.min())
print("Maximum            :", arr3.max())


# Q23
header(23, "Flatten a (2,3,4) array")
arr3 = np.arange(1, 25).reshape(2, 3, 4)
print("Original:\n", arr3)
print("Flattened:", arr3.flatten())


# Q24
header(24, "3-D array 1..27, flatten and calculate")
arr3 = np.arange(1, 28).reshape(3, 3, 3)
flat = arr3.flatten()
print("Flattened :", flat)
print("Sum       :", flat.sum())
print("Average   :", flat.mean())
print("Maximum   :", flat.max())
print("Minimum   :", flat.min())


# Q25
header(25, "Flatten random (3,4,5) array and filter elements")
arr3 = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr3.flatten()
avg = flat.mean()
print("Flattened      :", flat)
print("Average value  :", avg)
print("Greater than 50:", flat[flat > 50])
print("Even numbers   :", flat[flat % 2 == 0])
print("Less than avg  :", flat[flat < avg])
