import base64
import os

f=open("sample")
string = f.read()

s=''
for i in range(0,len(string)):
	if string[i]==' ':
		s+='+'
	else:
		s+=string[i]
convert = base64.b64decode(s)
t = open("example.png", "w+")
t.write(convert)
t.close()

#x=os.system(cs)
#print x
