sum = 0

for i in range(0,10):
    grade = int(input("Enter a grade: "))
    if grade<=99 and grade>=0:
        sum = sum + grade
    else:
        print("Wrong grade")
        break
print(sum)

for i in range (0,10):
    a = input("Enter grade 1: ")
    b = input("Enter grade 2: ")
    if a==b:
        print("You are done, thanks")
        break
    else: 
        print("Try again")















