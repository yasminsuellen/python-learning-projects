# Create the 'sum_tuple' function to receive a tuple of integers as an argument

def sum_tuple(tuple):
    return sum(tuple)


if __name__ == "__main__":
    entry = input("Enter integers separated by spaces to calculate their sum: ")

    # Defines tuple to receive integers
    elements = tuple(map(int, entry.split()))

    result = sum_tuple(elements)
    print(f"The sum of the elements of the tuple is: {result}")