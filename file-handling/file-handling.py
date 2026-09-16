# operations
# read
# write
# append
# binary operations

# open(file-path, mode)
#modes -> r, w, a, b
# r - read
# w - write
# a - append
# b - binary

# reading from a text file
# file = open("sample.txt", "r")

# content = file.read()
# print(content)

# reading certain portion of the file

# file = open("sample.txt", "r")
# # number of letters you want to get from the text file
# content = file.read(10)

# print(content)

# open(filepath) -> also means read mode
# open(filepath, "r") -> also means read mode
# file = open("sample.txt")

# content = file.read()
# print(content)

# to read only the first line from the text file

# file = open("sample.txt", "r")

# content = file.readline()
# print(content)

# to read all the files from the text

# file2 = open("sample.txt", "r")

# content2 = file2.read()
# print(content2)

# to get all the lines from the text file in a list

# file = open("sample.txt", "r")
# content = file.readlines()

# print(content)

