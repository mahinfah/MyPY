#data types
#boolean = True
b=1
a=11#
print(a<b)
#format method for string   
name="noman"
roll="7"
id="23-41212-2"

print(f"My name is {name} and my roll number is {roll} and my ID is {id}")


# Byte data types

numlist = [2,3,4,5,6,7,8,9,10,11]
bb=bytes(numlist)

b=bytearray(numlist)  # bytearray can be assigned
b[0]=99
print(b[0])

#list

list_bucket=["sdd","s","s",2,3]
list_bucket[0]="as"
print(list_bucket)

#tuple
list_bucketuple=("sdd","s",3,5,343,4,43,2)
#list_bucket[0]="as"
print(list_bucketuple)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)



#loop
range(2)
fruits1 = {"apple", "banana", "cherry"}

numlist = [2,3,4,5,6,7,8,9,10,11]
for x in numlist:
  print(x)

fruits = ["apple", "banana", "cherry"]

i=0
while i < len(fruits):
   print(fruits[i])
   i += 1
print("helo")                  

set1 = {1,2,3,4,5}
#print(set[8])
set2={41,23,4121,3212,43,412}
set3=set1.union(set2)
for i in set3:
   print(set3)

#printng dictionary and only keys

   dic ={ 
       "number":3,
       "roll":1,
       "name": "mahin"
   }
print(dic.keys())
print(dic)



profile ={
   "info":{
      "name": "mahin",
      "age": 22,
      "job": "mernstack devleloepr"
   },
 "task":{
    "task1": "complete",
    "task2": "incomplete",
    "task3": "incomplete again"
      
   },
   "hobby":{
      "main": "fishing",
      "main2": "debuging",
      2:"coding"
   },
   "main22":"SAd"  

}
profile["hobby"]= "aaaaaaaaaaaaaaa"

profile["task"]= "lmao"

profile.update({"info":"marmu"})
#profile.pop("task")
#print(profile)

student={"mahin":
         {"id" :"23-4131-12",
          "clg":"rajuk",
          "Home":"bbaria"},
"rafin":{
"ssds":"SDSDs",
"FDfdf":"FDfdf"
},
"safin":{
   "sdsds":"fdfd",
   "fdfd":"SDsds",
}

}
#print(student)
#printing only keys
for i in student:
   print(i)
   print("____________________")

for j in student.keys():
   print(j)
#printing only values from the keys
for j  in student.values() :
  print(j)

#removing keys from dictionaries
#student.pop("rafin")
#student.pop("safin")

for j in student.keys():
   print(j)

#copying dictionaries
new_student=student.copy()
print("new line____________________")
for i in new_student:
   print(i)


#conditions
print("checking conditions ________________")
a=0
b=299
if (a<b):
 print("checking a choto")
elif(a==0):     
 print("checking a zero")
else:
   print("checking a boro ")

