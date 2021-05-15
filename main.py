# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

import pandas
not_correct = True

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
letter_codes = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# while not_correct:
#     result = []
#     user_input = input("Enter your name : ").upper()
#     user_codes = list(user_input)
#     for code in user_codes:
#         try:
#             result.append(letter_codes[code])
#             not_correct = False
#         except KeyError:
#             print('Sorry, only letters in the alphabet letters')
#             break
#         else:
#             result = [letter_codes[code] for code in user_codes]
#             not_correct = False
#     if len(result) > 0:
#         print(result)


def generate():
    user_input = input("Enter your name : ").upper()
    user_codes = list(user_input)
    try:
        result = [letter_codes[code] for code in user_codes]
    except KeyError:
        print('Sorry, only letters in the alphabet letters')
        generate()
    else:
        print(result)


generate()
