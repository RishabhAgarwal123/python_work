# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint 1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint 2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint 3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"


with open('Input/Names/invited_names.txt') as names:
    invited_people = names.readlines()


with open('Input/Letters/starting_letter.txt') as letters:
    content = letters.read()
    for name in range(len(invited_people)):
        new_name = invited_people[name].strip()
        letter = content.replace(PLACEHOLDER, new_name)
        name = f"Output/ReadyToSend/letter_for_{new_name}.txt"
        with open(name, mode='w') as file:
            file.write(letter)
            print(f"Letter created with name :: {name}")
