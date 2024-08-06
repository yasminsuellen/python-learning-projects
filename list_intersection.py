def common_elements(list1, list2):
    # Converts list elements to integers and creates sets
    set1 = set(map(int, list1))
    set2 = set(map(int, list2))

    # Returns the list with common elements
    return list(set1.intersection(set2))


if __name__ == "__main__":
    # Reading the lists
    list1 = input("Enter the first list of integers separated by space: ").split()
    list2 = input("Enter the second list of integers separated by space: ").split()

    # Checks if all list elements can be converted to integers
    if all(item.isdigit() for item in list1) and all(item.isdigit() for item in list2):
        common = common_elements(list1, list2)
        print(f"Elements common to both lists: {common}")
    else:
        print("Invalid Input.")