#Py to understand File objects
import os

#easy but not recommnded
# f = open('test.txt', 'r')
# print(f.name)
# f.close()

#This Context Manager way we dont need to close explicitly, and f obj can be available even after file is closed.So file contents are not accessible 
with open('test.txt', 'r') as f:
    f_contents = f.read()#loads full contents.
    #f.read(100) limits to reading first 100 chars
    #f.readlines() loads all lines in list
    #f.readline() loads one line at a time and points to next line in the next execution.
    #print(f_contents, end='') To avoid next line char while printing
    print(f_contents) # works fine for small files

    #Best way is to iterate uisng For loop, line by line
    for line in f :
        print(line, end='')

    #Another way to read small chunks of 100 chars
    size_to_read=100
    f_contents=f.read(size_to_read)
    #f.tell() to report the posion it has reached
    #f.seek(0)  To go back to starting position
    while len(f_contents) > 0:
        print(f_contents. end='')
        f_contents=f.read(size_to_read)



#WRITE to a FILE
with open('test_new.txt', 'w') as f:
    f.write('Test')#Writes to file
    f.seek(0) #works in write mode also.
    f.write('R')#Makes the file content: Rest

#READ and WRITE of multiple files together
with open('test.txt', 'r') as rf:
    with open('test_cp.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


##Reading a Picture file using binary mode- rb/wb etc.
with open('dog.jpg', 'rb') as rf:
    with open('dog_cp.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

##CHUNK based reading
with open('dog.jpg', 'rb') as rf:
    with open('dog_cp.jpg', 'wb') as wf:
        chunk_size=4096
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)


