# File Objects

'''
save as test.txt:

1) This is a test file
2) With multiple lines of data...
3) Third Line
4) Fourth Line
5) Fifth Line
6) Sixth Line
7) Seventh Line
8) Eighth Line
9) Ninth Line
10) Tenth Line
'''

################READING FILES#################


# Opening file w/o contacts manager(Not recommended)
'''
Modes of the file:
'r' = opens file for reading
'w' = opens file for writing
'a' = opens file for appending
'r+' = opens file for reading and writing

open('somefile.txt', 'modehere')
'''

# f = open('test.txt', 'r') #Opens test.txt for reading

# Shows name of the file
# print(f.name)

# Shows mode of the file
# print(f.mode)

# We need to always close the file
# f.close()


##############################################

# Opening file using contacts manager(recommended)
# It closes file automatically if an error has occured and it do not need
# to call the close() function
with open('test.txt', 'r') as f:
    f_contents = f.read()  # Reads the contents and puts into a variable
    print(f_contents)

print("\n")

with open('test.txt', 'r') as f:
    f_contents = f.readlines()  # Makes a list of all the lines in the text file
    print(f_contents)

print("\n")

with open('test.txt', 'r') as f:
    f_line = f.readline()  # Reads each line
    print(f_line)
    f_line = f.readline()  # Reads the second
    print(f_line)

print("\n")

# Iterates through each line
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

print("\n")

# Prints the file with a limit of n characters(chunk)
with open('test.txt', 'r') as f:
    f_contents = f.read(100)  # Prints 1st 100 characters of the file
    print(f_contents)
    f_contents = f.read(100)  # Running it again prints the next 100 character
    print(f_contents)
    # It will not print another because it will return empty string and all of
    # the contents were printed
    f_contents = f.read(100)
    print(f_contents, end='')

print("\n")

# Printing a large file by chunks
with open('test.txt', 'r') as f:
    size_to_read = 100  # 100 chunks
    f_contents = f.read(size_to_read)

    # This will run until f_contents has nothing left to print
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)

print('\n')

# Check this
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)  # Resets the contents from 1st character

    f_contents = f.read(size_to_read)
    print(f_contents)

##########WRITING FILES###########

# Create new test file
with open('test2.txt', 'w') as f:
    # Writes test to the test2.txt, and creates it if it doesnt exist, but if
    # the file exists, it will overwrite it
    f.write("Test")
    f.write("Test")  # Writes another "test" into the text file


# Check this
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)  # Starts the next write at the first character
    # Basically overwrites the Test because it is written in the first
    # character
    f.write('Test')

# Check this too
with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')  # Replaces the 1st index with R, it becomes Rest

# Making a copy using read and write seprately
with open('test.txt', 'r') as readfile:
    with open('test_copy.txt', 'w') as writefile:
        for line in readfile:  # Reads each line
            writefile.write(line)  # Writes into the test_copy


# Copying a picture using file handling
# rb - read bytes
# wb - write bytes
with open('BinaryTree.png', 'rb') as rf:
    with open('BinaryTree_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)

# Copying image chunk by chunk
with open('BinaryTree.png', 'rb') as rf:
    with open('BinaryTree_copy.png', 'wb') as wf:
        chunksize = 4096
        rf_chunk = rf.read(chunksize)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunksize)
