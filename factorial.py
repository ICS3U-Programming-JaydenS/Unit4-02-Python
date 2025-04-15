#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program tells you the factorial product of the user's number


def main():
    loop_counter = 0

    factorial_answer = 1

    # Get the user number
    user_number_as_string = input("Enter a positive whole number: ")
    try:

        # Converts user num to int
        user_number_as_int = int(user_number_as_string)

        # If the user num is 0 this happens
        if user_number_as_int == 0:
            print("0! = 1")

        # If its negative this happens
        elif user_number_as_int < 0:
            print((user_number_as_int), "is not a positive integer")

        # If not any of those code continues
        else:

            # Calculate the factorial of the user number using a loop

            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through loop.".format(loop_counter))

                if loop_counter >= user_number_as_int:
                    break

            print("")
            print("{}! = {}".format(user_number_as_int, factorial_answer))

    # If user num is not a int this happens
    except Exception:
        print((user_number_as_string), "is not a positive integer")


if __name__ == "__main__":
    main()
