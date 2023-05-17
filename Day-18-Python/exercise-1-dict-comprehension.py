sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_list = sentence.split()
sentence_dict = {word:len(word) for word in sentence_list}

print(sentence_dict)

