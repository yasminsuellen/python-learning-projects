def vowel_count(text):
    # Defines a set of both lowercase and uppercase vowels
    VOWELS = "aeiouAEIOU"
    # Initializes a counter to count vowels
    vowel_count = 0
    # Iterates through the characters in the string
    for char in text:
        # Checks if the current character is a vowel and increments the counter value
        if char in VOWELS:
          vowel_count += 1
        else:
          continue
    return vowel_count
# Prompts the user to enter a string
text = input()

# Calls the vowel_count function and displays the result
result = vowel_count(text)
print(f"The number of vowels in the string '{text}' is: {result}")