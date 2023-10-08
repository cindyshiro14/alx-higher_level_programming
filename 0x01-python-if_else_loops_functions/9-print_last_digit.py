#!/usr/bin/python3

def print_last_digit(number):
    # Calculate the absolute value of the number to handle negative numbers
    abs_number = abs(number)

    # Get the last digit by taking the remainder when dividing by 10
    last_digit = abs_number % 10

    # Print the last digit and return its value
    print(last_digit, end='')
    return last_digit
