# file openning reading
r= open("main.html", "r")
print (r.read())

# file writing
newfile=open("new.txt","w")
newfile.write("hello everyone \nToday is very special \nBecause Dr younus came to bd and take his oath \n")
newfile.write("Hope everyone Will be happy ")

# file appending
neww = open("new.txt", "a")
neww.write("nOW LET'S SEE N HOPE FOR THE BEST")

import os

os.remove("lol.txt")