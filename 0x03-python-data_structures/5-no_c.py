#!/usr/bin/env python3

def no_c(my_string):
    # Initialize an empty string to store the result
    result = []

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C' and add it to the result list
        if char != 'c' and char != 'C':
            result.append(char)

    # Join the characters in the result list to form the final string
    return ''.join(result)

if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
