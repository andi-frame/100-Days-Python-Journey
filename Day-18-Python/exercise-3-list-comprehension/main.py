# MY VERSION CODE:
# with open("Day-18-Python/exercise-3-list-comprehension/file1.txt") as file1:
#     data_1 = file1.read()
#     num_1 = data_1.split("\n")
    
# with open("Day-18-Python/exercise-3-list-comprehension/file2.txt") as file2:
#     data_2 = file2.read()
#     num_2 = data_2.split("\n")

# common_value = [num for num in num_1 if num in num_2 and num]
# print(common_value)

# THE SOLUTION
with open("Day-18-Python/exercise-3-list-comprehension/file1.txt") as file1:
    data_1 = file1.readlines()
with open("Day-18-Python/exercise-3-list-comprehension/file2.txt") as file2:
    data_2 = file2.readlines()

common_value = [int(num) for num in data_1 if num in data_2 and num]
print(common_value)
# Write your code above 👆


