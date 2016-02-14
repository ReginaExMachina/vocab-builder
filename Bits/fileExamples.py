#!/usr/bin/env python

# CREATING A NEW FILE
file = open("newfile.txt", "w")
file.write("hello world in the new file\n")
file.write("and another line\n")
file.close()


# READING A FILE
file = open('newfile.txt', 'r')
print file.read() #Put n for the first n chars


# LOOPING OVER FILE

file = open('newfile.txt', 'r')

for line in file:
    print line


# WRITING IN A FILE

file = open("newfile.txt", "w")
file.write("This is a test\n")
file.write("And here is another line\n")
file.close()


# EXAMPLES

with open("newfile.txt") as f:
    for line in f:
        print line,
