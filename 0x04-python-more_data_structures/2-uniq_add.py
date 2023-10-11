#!/usr/bin/python3

def uniq_add(my_list=[]):
# Use a set to store unique integers
unique_set = set()
    
# Iterate through the list and add unique integers to the set
for num in my_list:
unique_set.add(num)

# Sum up the unique integers in the set
result = sum(unique_set)
    
return (result)

# Test the function
if __name__ == "__main__":
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
