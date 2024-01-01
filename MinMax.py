import random
def minMax(*a):
    a = list(a)
    # Repeat the sorting process until no more swaps are needed
    while True:
        swapped = False  # Flag to track whether any swaps were made in the current pass
        for item in range(len(a) - 1):
            if a[item] > a[item + 1]:
                temp = a[item]
                a[item] = a[item + 1]
                a[item + 1] = temp
                swapped = True  # Set the flag to True if a swap was made

        if not swapped:
            break  # Exit the loop if no swaps were made in the current pass

    return f"Min: {a[0]}, Max: {a[len(a)-1]}"

def main(): 
    a = [random.randint(1, 100) for _ in range(30)]
    print(*a)
    result = minMax(*a)
    print(result)

if __name__ == "__main__":
    main()