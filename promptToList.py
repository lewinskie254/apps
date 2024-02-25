length_a = int(input("How many numbers do you want your first list to contain? "))
list_a = createList(length_a)
length_b = int(input("How many numbers do you want your second list to contain? "))
list_b = createList(length_b)

def createList(length):
    count = 0 
    list_x = []

    while count < length:
        number = int(input(f"Enter the {count} digit: "))
        list_x.append(number)
        count += 1

    return list_x


print("List_A: ", list_a)
print("List_A: ", list_b)
