# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# -----------------------------------------------------------------------------------------------------------
import pandas as pd


#TODO 1. Create a dictionary:
nato_phonetic_alphabet = pd.read_csv("Day-18-Python/NATO-alphabet-start/nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Word: ").upper()
word_phonetic_list = [data_dict[letter] for letter in user_input]
print(word_phonetic_list)