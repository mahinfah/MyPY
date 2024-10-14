#array
cars = ["Ford", "Volvo", "BMW"]
for i in cars:
    print(i)


#string
a="Hello, World!"

print(a[1])

print(a[-2])
#printing from last 2nd character


#printing only hello
print(a[0:5])

#replacing things 

replace = a.replace("World","Mahin")
print(replace)

#splitting  


aaa="lol lll lol aasa asas aa  aaa   aa   aa lol lol"

#count

print(aaa.count("lol"))


#condition 
if 2>1:
    print("2 is greater than 1")



#loop
pi =1
while pi<=10:
   print("2 *  " ,pi,"  =  " ,2*pi)
   pi=pi+1

   #nested loop using for

l11=["small","medium","large"]
l1=["apple","banana","cherry"]

for i in l11:
    for j in l1:
        print(i,j)


#checking if number is even or odd

check = input("Enter a number: ")
check = int(check)
if check % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#range

#for i in range(10):
   # print(i+1)


#factorial
sum=1
a=input("enter a number to find factorial: ")
aa=int(a);
for i in range(1,aa+1):
    sum=sum*i
    print(sum)
    i=i+1


print("Factorial of digit",aa,"  : " ,sum)   



#panlindrom or reverse that are same of a number like 121, 1221, 12321

q=input("Enter a number to check if it is palindrom or not: ")
qq=int(q)
digit=0
while(qq!=0):
    lol=qq%10
    digit=(digit*10)+lol
    qq=qq//10


print("Reverse of the number is: ",digit)



