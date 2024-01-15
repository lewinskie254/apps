import random 
a = [random.randint(1, 100) for _ in range(30)]
print(*a)
print(str(max(*a)))