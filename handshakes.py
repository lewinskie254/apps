people = ['Alice', 'Bob', 'John', 'Wayne', 'Marlon']

numberOfHandshakes = 0

for i in range(0, len(people)-1):
    for j in range(i + 1, len(people)):
        print(people[i], "shakes hand with", people[j])
        numberOfHandshakes +=1 
print("Number of handshakes: ", numberOfHandshakes)