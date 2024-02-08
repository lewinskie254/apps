def get_valid_input(prompt):
    while True:
        user_input = input(prompt)


        if user_input.isdigit():
            return int(user_input)
        else:
            print(f"{prompt[:-2]} must be a whole number.")


def isValidDate(year, month, day):
    year_str = str(year)

    if len(year_str) == 4:
        if 1 <= month <= 12:
            if month in [9, 4, 6, 11]:
                max_days = 30
            elif month == 2:
                max_days = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
            else:
                max_days = 31

            if day > max_days:
                return False
        else:
            return False
    else:
        return False

    return True

def main():
    year = get_valid_input("Year: ", int)
    month = get_valid_input("Month: ", int)
    day = get_valid_input("Day: ", int)

    if isValidDate(year, month, day):
        print("Date is valid.")
    else:
        print("Invalid date")

if __name__ == "__main__":
    main()
