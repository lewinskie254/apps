def average(*a):
    a = list(a) 
    sum = 0
    for i in range(len(a)):
        sum += a[i]

    return sum/len(a)

def ranged(*a):
    a = list(a) 
    small = min(a)
    big = max(a)

    return big - small

def median(*a):
    a = list(a)
 
    while True: 
        sorted = False 
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1]=temp 
                sorted = True

        if not sorted:
            break 
    
    if len(a)%2 == 0: 
        return (a[int(len(a)/2)] + a[int(len(a)/2 -1)])/2 
    elif len(a)%2 == 1:
        return a[int(len(a)/2)]

     

def main():
    a = [3, 7, 10, 4, 1, 9, 6, 5, 2, 8]
    print(f"Average: {str(average(*a))}")
    print(f"Range: {str(ranged(*a))}")
    print(f"Median: {str(median(*a))}")
    print(f"Count: {str(len(a))}")

if __name__ == "__main__":
    main()