print("Please help us giving information")
class check:
    def __init__(self,A,B,C):
        self.Name=A
        self.mark=B
        self.cgpa=C

    def display(self):
        print("Hello ",self.Name)
        print("You got mark total ",self.mark)
        print("Your Avg mark is ",self.cgpa)


Name=input("Enter your name: ")
T=input("Enter your total subject: ")
total=int(T)

sum = 0
i=0
while i < total:
     
     total_mark=input(f"Enter your No {i+1} subject mark: ")
     tt=int(total_mark)
     sum = sum+tt 
     i = i + 1
     

def checkcgpa(sum,total):
   avg = sum / total    
   return avg

avgO = checkcgpa(sum, total)
x = check(Name, sum, avgO)
x.display()