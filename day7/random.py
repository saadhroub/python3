import random

# Generate a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)
print("Random Integer:", random_int)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random floating-point number between a specified range
random_range_float = random.uniform(5.0, 10.0)
print("Random Range Float:", random_range_float)

# Generate a random element from a list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
random_element = random.choice(my_list)
print("Random Element from List:", random_element)

# Shuffle the elements of a list in place
random.shuffle(my_list)
print("Shuffled List:", my_list)
