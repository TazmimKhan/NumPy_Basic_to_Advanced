import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print("Array:", numbers)
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# Convert the array into 2 rows and 3 columns
matrix = numbers.reshape(2, 3)
print("Matrix:\n", matrix)
