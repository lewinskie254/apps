def sumArray(*a):
    a = list(a)
    sum = 1
    for i in range(len(a)):
        sum += a[i] 

    return sum 

def productArray(*a):
    a = list(a)
    sum = 1
    for i in range(len(a)):
        sum *= a[i] 

    return sum 



def main():
    a = [1, 2, 4, 12, 15, 19, 20]
    print(f"Sum: {str(sumArray(*a))}")
    print(f"Product: {str(productArray(*a))}")

if __name__ == "__main__":
    main()