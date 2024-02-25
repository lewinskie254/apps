def mergeLists(list_a, list_b):
    concat_list = list(list_a + list_b)

    for i in range(len(concat_list)-1):
        for j in range(len(concat_list)-1):
            if concat_list[j] > concat_list[j+1]:
                tmp = concat_list[j]
                concat_list[j] = concat_list[j+1]
                concat_list[j+1] = tmp

    return concat_list

def createList(length):
    count = 0 
    list_x = []

    while count < length:
        number = int(input(f"Enter the {count} digit: "))
        list_x.append(number)
        count += 1

    return list_x

def main():
    length_a = int(input("How many numbers do you want your first list to contain? "))
    list_a = createList(length_a)
    print("List_A: ", list_a)
    length_b = int(input("How many numbers do you want your second list to contain? "))
    list_b = createList(length_b)
    print("List_A: ", list_b)
    
    result = mergeLists(list_a, list_b)
    print("Result: ", result)

if __name__ == "__main__":
    main()