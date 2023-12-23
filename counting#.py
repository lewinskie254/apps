n = int(input("Number: "))

for i in range(n):
    if i > 0: 
        print(" " * (n - i), end="")
        print("#" * i)
