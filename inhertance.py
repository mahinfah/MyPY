#inheritence

class car:

    def START(self):
        print("Engine Started")

    def STOP(self):
        print("Engine Stopped") 


class BMW(car):

  def __init__(self,name):
           self.name=name 

  @staticmethod
  def hello():
    print("we are bmw company")   


car1=BMW("BMW")
print(car1.name)
print(car1.START())
print(car1.STOP())


class bmwfactory(BMW):

    def __init__(self,model):
        self.model=model

    @staticmethod
    def manu():
        print("BMW Factory")

carmanu1=bmwfactory("X5")
carmanu2=bmwfactory("X6")
print(carmanu1.model)
print(carmanu2.model)
print(carmanu1.hello())
print(carmanu1.manu())


