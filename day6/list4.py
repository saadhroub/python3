my_list = ["apple", "banana", "cherry"]
#           0         1          2
#          الثالث    الثاني    الأول 
# ['Tomato', 'Cucumber', 'Apricot', 'banana', 'cherry', 'Orange']
#    0           1           2           3       4           5
#   السادس    الخامس    الرابع     الثالث       الثاني    الأول
print(my_list)
print(my_list[1])
my_list[0] = "Cucumber"
print(my_list)

my_list.append("Orange")
print(my_list)

my_list.insert(0,"Tomato")
print(my_list)

my_list.insert(2,"Apricot")
print(my_list)

print(my_list[1:4])
print(my_list)
# بدون إندكس يحذف آخر عنصر 
# يتعامل مع الإندكس 
print(my_list.pop(1))

# يتعامل مع العناصر مباشرة
print(my_list.remove("cherry"))

print(my_list)

list2 = [45,50,69,95,45,99, 20, 15]

list5 = ["Ahmad", "Yazan", "Huda", "Kamil"]
print(sorted(list5, reverse=True))

list3 = sorted(list2, reverse=True)
print(list3)





