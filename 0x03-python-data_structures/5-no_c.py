#!/usr/bin/env python3

def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string

# Test cases
if __name__ == "__main__":
    print(no_c("Best School"))  # Output: "Best Shool"
    print(no_c("Chicago"))      # Output: "hiago"
    print(no_c("C is fun!"))    # Output: " is fun!"
