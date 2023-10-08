#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = my_list[0]  # Initialize max_value with the first element of the list

    # Iterate through the list to find the maximum value
    for number in my_list:
        if number > max_value:
            max_value = number

    return max_value

if __name__ == "__main__":
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
