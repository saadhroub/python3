empty_list = []
students = int(input("Enter the number of students: "))
sum = 0

for i in range (0, students):
    empty_list.append(int(input("Enter a Mark: ")))
    sum+=empty_list[i]

average = sum/students
print("Sum: ", sum)
print("Top Student: ", max(empty_list))
print("Last Student: ", min(empty_list))
print("Class average: ", average)

