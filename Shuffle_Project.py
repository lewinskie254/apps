import random

numbers = [15, 13, 12, 4, 5, 2, 7, 8, 1, 9]

random_index = []

new_numbers = []

for i in range(len(numbers)):
    random_number = random.randint(1, len(numbers))

    while random_number in random_index:
        random_number = random.randint(1, len(numbers))

    random_index.append(random_number)
    
    new_numbers.append(random_index[i])

print(new_numbers)
