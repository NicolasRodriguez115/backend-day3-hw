# 1. Python List Transformation

# Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)
total_grades = 0
for grade in grades:
    total_grades += grade
grades_avrg = total_grades / len(grades)
print(grades_avrg)

# 2. Advanced Slicing Techniques

# Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_wk_temp = temperatures[7:14]
print(second_wk_temp)

# Task 2
high_temp = []
for temperature in temperatures:
    if temperature > 100:
        high_temp.append(temperature)
print(high_temp)

# Task 3
print(temperatures[5:11])