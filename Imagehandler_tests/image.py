import base64
import os

f=open("smple.png")
data = f.read()
f.close()
string = base64.b64encode(data)
# print string

cs=''

cs += 'curl --data "idata='
cs += string
cs += '" http://127.0.0.1:8000/storefront/imagehandler'

print cs

convert = base64.b64decode(string)
t = open("example.png", "w+")
t.write(convert)
t.close()

#x=os.system(cs)
#print x
