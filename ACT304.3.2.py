# Problem 1
# Create a new string with the specified characters:


sentence = "You learn more from failure than from success."
new_string = sentence[0] + sentence[3] + sentence[-1]
print(new_string)  # Output: "Y.s"

# Problem 2
# Replace the period with an exclamation mark:

modified_sentence = sentence.replace(".", "!")
print(modified_sentence)  # Output: "You learn more from failure than from success!"

# Problem 3
# Convert the string to lowercase:

new_str = "WHEN YOU Change your thougHts, remember to ALSO change your world."
lowercase_str = new_str.lower()
print(lowercase_str)

# Problem 4
# Convert the new_str variable to uppercase:

uppercase_str = lowercase_str.upper()
print(uppercase_str)

# Problem 5
# Check if the string starts with certain characters:

starts_with_Z = new_str.startswith("Z")
starts_with_t = new_str.startswith("t")
print(f"Starts with 'Z': {starts_with_Z}, Starts with 't': {starts_with_t}")

# Problem 6
# Find the index of the character "j":

index_of_j = new_str.index("j")
print(index_of_j)

# Problem 7
# Count occurrences of "t" and "o":

count_t = new_str.count("t")
count_o = new_str.count("o")
print(f"The letter 't' appears {count_t} times and the letter 'o' appears {count_o} times.")

# Problem 8
# Find the length of the string:

greeting = "Good Morning!"
length_of_greeting = len(greeting)
print(length_of_greeting)  # Output: 14

# Problem 9
# Check if all characters in the string are alphabetic:

alphabet = "abcdefghijklmnopqrstuvwxyz"
all_alpha = alphabet.isalpha()
print(all_alpha)  # Output: True

# Problem 10
# Use find() and index() for the value "y":

learning = "Learning is fun!"
find_y = learning.find("y")
index_y = learning.index("y")
print(f"Find 'y': {find_y}, Index 'y': {index_y}")

# Comment explaining the difference:
# The find() method returns the lowest index of the substring if found in the string, otherwise it returns -1.
# The index() method also returns the lowest index but raises a ValueError if the substring is not found.

# Problem 11
# Count the occurrences of each character in the string:

count_string = "Twinkle twinkle little star, how I wonder what you are"
from collections import Counter

character_count = Counter(count_string)
for char, count in character_count.items():
    print(f"'{char}': {count}")