#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store True or False values
    result = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result

if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
        i += 1
