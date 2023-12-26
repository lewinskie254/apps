f = open('read.txt', 'r')
x = f.readlines()
concat = ""

for i in range(len(x)):
    x[i] = list(x[i])
    for j in range(len(x[i])): 
        x[i][j] = x[i][j].lower()
        x[i][j] = x[i][j].replace("\n", " ")
    for j in range(len(x[i])):
        concat += x[i][j]
    
new_string= concat.split(". ")


for i in range(len(new_string)):
    index = len(new_string[i]) - 1
    published = ""
    for j in range(len(new_string[i])): 
        published += new_string[i][index]
        index -= 1
    file = open('daer.txt', 'a')
    file.write(f"{published} \n")
    f.close()
