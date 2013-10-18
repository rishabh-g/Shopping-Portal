import base64
import os

f=open("smple.png")
data = f.read()
f.close()
string = base64.b64encode(data)
print string

