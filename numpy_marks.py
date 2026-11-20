import numpy as np

# Each row contains one student's marks in three subjects.
names = np.array(["Amina", "Rafi", "Sara", "Hasan"])
marks = np.array([
    [85, 90, 78],
    [60, 55, 70],
    [95, 88, 92],
    [35, 50, 40],
])

# axis=1 calculates a result across the subjects for each student.
totals = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)

for name, total, average in zip(names, totals, averages):
    print(f"{name}: total = {total}, average = {average:.2f}")

# A student passes when every subject mark is at least 40.
passed = np.all(marks >= 40, axis=1)
print("\nStudents who passed:", names[passed])

best_index = np.argmax(averages)
print("Top student:", names[best_index])