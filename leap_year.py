# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/27/2021
# This is the Leap Year program
# The user enters in the year
# The program tells the user if it is a leap year


def main():
    # this function checks to see if the year is a leap year

    # input
    year_as_string = input("Enter in the year: ")
    print("")

    # process and output
    try:
        year_as_number = int(year_as_string)
        if year_as_number % 4 == 0:
            if year_as_number % 100 == 0:
                if year_as_number % 400 == 0:
                    print("{0} is a leap year".format(year_as_string))
                else:
                    print("{0} is a common year".format(year_as_string))
            else:
                print("{0} is a leap year".format(year_as_string))
        else:
            print("{0} is a common year".format(year_as_string))

    except Exception:
        print("You didn’t enter in an integer.")

    print("\nDone")


if __name__ == "__main__":
    main()
