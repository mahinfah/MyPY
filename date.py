import datetime
print("HELLO \n HOW ARE U")
a=datetime.datetime.now()
print (a)


#mathmatical function
a=2
b=3
print(min(a,b))
print(max(a,b))
print(pow(a,b))
print(pow(b,3))


#using math module python has a built in module 

import math
print("Using module________________")
x= math.sqrt(25)
print(x)
p = math.pi
print(p)

#regex it actually means strings manipulation type things or function
import re

sen = "1 : it is safe to call you"
check=re.search("^1",sen)

if check:
    print("hellyeah")

else:
    print("no match")

