number  = 112443545.657

def commaFormat(number):
    new_number = str(number)

    final = ''

    count = 0 
    snap = False 

    for i in range(len(new_number)):
        if new_number[i] == ".":
            count = i
            snap = True 

    if snap: 
        for k in range(0, count):
            if (count - k) % 3 == 0 and k > 0:
                final += ","
            final += new_number[k]
        for j in range(count, len(new_number)):
            final += new_number[j]
    else: 
        count = len(new_number)
        for k in range(0, count):
            if (count - k) % 3 == 0 and k > 0:
                final += ","
            final += new_number[k]

    
    return final 

def main():
    number = input("Number: ")
    print(commaFormat(number))

if __name__ == "__main__":
    main()