#Find how many a in Alphabet
word = 'alphabet'
count=0
for letter in word :
    if letter == 'a':
        count=count+1
print(count)

#summ of the number
n=20
m=int(n)+1
print(m)

#Extract 3 Character after the "." 
data = 'From stephen.ma2rquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+4])

#Print line from 14 to 17
x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])

#Print specific line from text 
text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
pos2 =text.find('5')
print(float(text[pos:pos2+1]))