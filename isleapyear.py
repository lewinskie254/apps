def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0: 
            if year % 400 == 0: 
                return True 
            else: 
                return False 
        else:
            return True
    else:
        return False 


def main():
    while True:
        year = input("Enter a year: ")
        if len(year) == 4:
            if year.isdigit():
                year = int(year)
                break
            else:
                print("Year must be in numbers.")
        else:
            print("Year must have four digits.")

    
    if isLeapYear(year): 
        print(year, "is a reap year. ")
    else: 
        print(year, "is not a reap year.")

if __name__ == "__main__":
    main()
