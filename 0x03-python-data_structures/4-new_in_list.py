#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list

    new_list = my_list.copy()  # Create a copy of the original list
    new_list[idx] = element   # Replace the element at the specified index
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)
    
    print(new_list)  # Print the modified list
    print(my_list)   # Print the original list to show it's not modified
