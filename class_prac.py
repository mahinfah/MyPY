class student:
#constructor must be defined with __init__ method
    def __init__(self,name,age,id):
       self.name=name
       self.age=age
       self.id=id
       print("This is a constructor")
#methods
    def hudai(self):
        print("This is a method if ykyk "+self.name)



s1=student("mahin",22,101)
print(s1.hudai())