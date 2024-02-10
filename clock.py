for i in range(24):
    if i == 0:
        count = i + 12
        for j in range(4):
            if j == 0:
                print(count, ": 00 am")
            else: 
                print(count, ":", j * 15, "am")
        print("<----------Part 1----------->")
    elif 11 < i < 23:
        for j in range(4):
            count = i - 11
            if j == 0:
                print(count, ": 00 pm")
            else: 
                print(count, ":", j * 15, "pm")
        print("<----------Part 2----------->")
    elif i == 11:
        for j in range(4):
            count = i + 1
            if j == 0:
                print(count, ": 00 am")
            else: 
                print(count, ":", j * 15, "am")
        print("<----------Part 3----------->")
    elif 0 < i < 11:
        for j in range(4):
            if i == 0:
                count = i 
            else: 
                count = i + 1
            if j == 0:
                print(count, ": 00 am")
            else: 
                print(count, ":", j * 15, "am")
        print("<---------Part 4------------>")
    elif i == 23: 
        for j in range(4):
            if j == 0:
                 print(i - 11, ": 00 am")
            else:
                print(i - 11, ":", j * 15, "am")
        print("<-----------Part 5---------->")
