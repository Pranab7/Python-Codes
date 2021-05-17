#Extract data from file and add the numbers from file
import re
x=open("Myfile.txt","r")
z=x.read()
y=re.findall('[0-9]+',z)
print(y)
n=0
for i in y :
    l=int(i)
    n=n+l
print(n)
#print file in uppercase
fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)
