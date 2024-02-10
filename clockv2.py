hours = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
minutes = ["00", "15", "30", "45"]
period = ["am", "pm"]


for i in range(25):
    if i < 11:
        for j in range(4):
            print(hours[i], ":", minutes[j], period[0])
    if i == 11:
        for j in range(4):
            print(hours[len(hours)- 1], ":", minutes[j],  period[1])
    if 11 < i < 23:
        for j in range(4):
            print(hours[i - 12], ":", minutes[j],  period[1])
    if i == 24:
        for j in range(4):
            print(hours[len(hours)- 1], ":", minutes[j],  period[0])
