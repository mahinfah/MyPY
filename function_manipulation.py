print("hi")

#using lamda funtion findind the maximum of two numbers
max= lambda a,b: a if a>b else b

print(max(2,33))



#using normal function

def check_max(a,b):
         if a>b:
           return a
         else:
           return b


print(check_max(2,55))