#count how many lines Starts with from(mail address)and count them
fname = input("Enter file name: ")
try:
    fh = open(fname)
    if len(fname) <= 1 :
        fname = "mbox-short.txt"
        fh = open(fname)
except:
    print('invalid entry!')
    quit()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    if words[0] != 'From':
        continue
    print(words[1])
    count += 1

print("There were " + str(count) + " lines in the file with From as the first word")