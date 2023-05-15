#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Day-16-Python/Mail_Merge_Project/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Day-16-Python/Mail_Merge_Project/Input/Letters/starting_letter.txt") as starting_letter:
    the_letter = starting_letter.read()

for name in names_list:
    name = name.strip()
    to_send_letter = the_letter.replace("[name]", name, 1)
    with open(f"./Day-16-Python/Mail_Merge_Project/Output/ReadyToSend/letter_for_{name}", mode = "w") as output:
        output.write(to_send_letter)