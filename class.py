# class basics

#class F:
 # name =""
  #number=" "
 # property=""
 # flat=""

#a= F()
##a.name = "John"
#a.number=1234

#print(a.name)
#print(a.number)


#INHERITENSED

class father:
  flat="Head"
  property=""


father.flat="2B"

class mother(father):
   name=""
   id=" "
  
m = mother()
#print(m.flat) 
#print(m.property)


class child(mother):
    age="24"
    name="mahin"


cC=child()
cC.flat="Purbachal"
print("hello "+cC.name )

print("yOU ARTE HAVING IN THE AGE OF " +cC.age)

print(" A FLAT NAME:  "+cC.flat)

