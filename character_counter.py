def count_characters(string):
    # Initializes an empty 'counter' dictionary to store character counts
    counter = {}

    # Iterates through each character in the string
    for character in string:
        # Checks if the character is already present in the counter dictionary
        if character in counter:
            # If present, increment the count
            counter[character] += 1
        else:
            # If not present, adds the character to the dictionary with an initial count of 1
            counter[character] = 1

    return counter


# Requests user input
entry = input("Please enter a string to count its characters: ")
result = count_characters(entry)
print(result)
