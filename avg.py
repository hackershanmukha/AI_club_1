# Student performance analysis

students = {
    "Ganesh": [85, 72, 91, 68],
    "Rahul": [78, 88, 69, 90],
    "Priya": [92, 81, 76, 89],
    "Anil": [65, 74, 82, 71]
}

averages = {} 

for name, marks in students.items():
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)
    averages[name] = average

highest = max(averages,key=averages.get)

print("Student Averages:")
for name, average in averages.items():
    print(f"{name}: {average:.2f}")

print("\nTop Student:", highest)
print("Highest Average:", averages[highest])
