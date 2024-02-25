sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
count = 0

for i in range(len(sorted_list)):
    new_list = sorted_list[-count:] + sorted_list[:-count] 
    print(count, new_list)


    count += 1


