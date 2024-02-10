
print("   1  2   3   4   5   6   7   8   9  10  ")
print('-+---------------------------------------+----')
for i in range(10):
    for j in range(10):
        print(str(((j+1) * (i+1))).rjust(4), end="")
    print(" :", str((i+1)).rjust(2))