def is_prime(num):
    for i in range(2, num):
        if num%i == 0: 
            return False
    return True

counter=0
for x in range(200,1000):
    if is_prime(x) == True:
        print(x, "is a prime number")
        counter+=1
    if counter == 10:
        break