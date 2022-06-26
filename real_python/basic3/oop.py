# from pydoc import describe


# class Parrot:
#     # class attribute
#     species = 'bird'

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sing(self, song):
#         print(self.name, 'sing', song)

# class ExtraParrot(Parrot):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print('Extra parrot is here')
    
#     def whoIsThis(self):
#         print(type(self))
    
#     def run(self):
#         print('run faster')

# love = Parrot('love', 10)
# phat = Parrot('phat', 20)
# extra = ExtraParrot('minh', 100)

# # access the class attributes
# print("Blu is a {}".format(love.__class__.species))
# print("Woo is also a {}".format(phat.__class__.species))

# # access the instance attributes
# print("{} is {} years old".format( love.name, love.age))
# print("{} is {} years old".format( phat.name, phat.age))

# love.sing('hellouyeay')
# extra.run()
# extra.whoIsThis()
# print(extra.__class__.species)

# class Game:
#     type = 'entertainment'

#     def __init__(self, name, description):
#         self._name = name
#         self._description = description
        
#     def getName(self):
#         return self._name
    
#     def getDescription(self):
#         return self._description
    
#     def setDescription(self, decsription):
#         self._description = decsription
    
# game1 = Game('naruto', 'fighting style ninja holly shit')

# print(game1.getName())
# print(game1.getDescription())

# game1.__name = 'the holy panda'
# print(game1._name)

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)