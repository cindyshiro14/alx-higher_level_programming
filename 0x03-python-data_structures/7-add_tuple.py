#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two integers from each tuple or use 0 for missing values
    a1, a2 = tuple_a[0] if len(tuple_a) > 0 else 0, tuple_a[1] if len(tuple_a) > 1 else 0
    b1, b2 = tuple_b[0] if len(tuple_b) > 0 else 0, tuple_b[1] if len(tuple_b) > 1 else 0

    # Calculate the sum of the first elements and the sum of the second elements
    sum1 = a1 + b1
    sum2 = a2 + b2

    # Return a tuple containing the sums
    return (sum1, sum2)

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
