#Q1-->Write a Pyhton program to read n lines of a file.
f=open("1.txt",'r')
"""open is used to open the file in r mode i.e. read mode"""
data=f.read()
"""read reads the content of file"""
print(data)
f.close()
"""close closes the file"""
print()

#Q2-->Write a pyhton program to count the frequency of words in a file.
f=open("2.txt",'r')
data=f.read()
words=data.split()
dict={}
for word in words:
    dict[word]=words.count(word)
print(dict)
f.close()
print()

#Q3-->Write a python program to copy the contents of a file to another file
f=open("1.txt",'r')
line=f.readlines()    
for l in line:
    f1=open("3.txt",'a')
    f1.write(l)
    f1.close()
f.close()
print()

#Q4-->Write a python program to combine each line from first file with the corresponding line in second file.
f=open("1.txt",'r')
f1=open("3.txt",'r')
for l1,l2 in zip(f,f1):
    f2=open("4.txt",'a')
    f2.write(l1+l2)
    f2.close()
f.close()
f1.close()
print()

#Q5-->Read a file and sort it to another file.
a="6,2,8,5,10,1,9,4,7,3"
f=open("5.txt",'r+')
f1=open("5_1.txt",'a')
for i in a:
    f.write(i)
f.close()
f=open("5.txt",'r')
data=f.read()
b=data.split(',')
b.sort()
for i in b:
    print(i)
    f1.write('%s\n' %i)
f1.close()
f.close()
