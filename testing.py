class Fruit(object):
    def __init__(self):
        print("Parent : instance of class Fruit")

    def Nutrition(self):
        print("Parent: instance of Fruit.Nutrition")

    def Fruit_Shape(self):
        print("Parent: instance of Fruit.Shape")

    def ParentMethod(self):
        print("Parent : Parents have special methods as well")

class Pineapple(Fruit):
    def __init__(self):
        print("Child : instance of class Pineapple")

    def Nutrition(self):
        print("Child: instance of Nutrition")

    def Fruit_Shape(self):
        print("Child: instance of Fruit.Shape")

    def ChildMethod(self):
        print("Child : Yay...only i have this method")

p1= Fruit()
p1.Nutrition()
p1.Fruit_Shape()

print("___________________________")

c1= Pineapple()
c1.Nutrition()
c1.ParentMethod()
c1.ChildMethod()
