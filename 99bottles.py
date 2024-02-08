count = 100 

for i in range(count): 
    if count > 1: 
        count -= 1
        print(count, " bottles of beer on the wall.")
        print(count, " bottles of beer.")
        print("Take one down, ")
        print("Pass it around. ")
    else: 
        print(count, " bottles of beer on the wall.")
        print(count, " bottles of beer.")
        print("Take one down, ")
        print("No More bottles of beer on the wall . ")
