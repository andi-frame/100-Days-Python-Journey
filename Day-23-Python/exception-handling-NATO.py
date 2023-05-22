import pandas as pd

#TODO 1. Create a dictionary:
nato_phonetic_alphabet = pd.read_csv("Day-23-Python/nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
print(data_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def check_input():
    user_input = input("Enter a Word: ").upper()
    try:
        word_phonetic_list = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Please only insert letters in the alphabet")
        check_input()
    else:
        print(word_phonetic_list)

check_input()
