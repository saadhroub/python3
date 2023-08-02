import math
print("let's start with Q1:-")
x = "********************************************************"
first_name = input("Enter your first name: ")
father_name = input("Enter your father name: ")
grand_father_name  = input("Enter grandfather name: ")
family_name = input("Enter Family name: ")

print(first_name.upper(), father_name.upper(), grand_father_name.upper(), 
    family_name.upper())
print(x)
###############################################################

#Question 2:Write a python code that asks the user to insert the student final marks
# for Arabic, English, Science, and Math. Then calculate the average of the student

Math = int(input("Please insert Math marks:  "))
English = int(input("Please insert English marks:  "))
Science  = int(input("Please insert Science marks:  "))
Arabic = int(input("Please insert Arabic marks:  "))

sum = Math + English + Science + Arabic
print(int(sum/4))

#################################################################

sta = input("Enter long text: ")

word1 = input("Enter the thing you to count: ")
counter1 = sta.count(word1)
print(counter1)

word2 = input("Enter the thing you to count: ")
counter2 = sta.count(word2)
print(counter2)

word3 = input("Enter the thing you to count: ")
counter3 = sta.count(word3)
print(counter3)