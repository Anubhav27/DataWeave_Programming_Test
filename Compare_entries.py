"""
This is Question 2 of the assignment to compare files with entries and find the count of common entries

solution:

the program will read entries from 2 files namely file1.txt and file2.txt and will compare the entries and prints the results



"""

file1_content=[]
file2_content=[]

match={}


with open('file1.txt') as fp:
    for line in fp:
        file1_content.append(line.strip())



#print file1_content.__len__();

with open('file2.txt') as fp:
    for line in fp:
        file2_content.append(line.strip())

#print file2_content.__len__();


for i in file1_content:
    count = 0
    for j in file2_content:
        if i==j:
            count = count+1
            match[i] = count



#print match.__len__()

for key in match:
    print key , "is repeated " , match[key]




