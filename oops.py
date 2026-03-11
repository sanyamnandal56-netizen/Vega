# class Factory:
#     def __init__(self,material,zip,pocekts):
#         self.material=material
#         self.zip=zip
#         self.pockets=pocekts
#     def show(self):
#         print(f"the objects are {self.material} , {self.zip} , {self.pockets}")
# reebok = Factory("leather",2,3)
# campus = Factory("nylon",3,4)
# reebok.show()
# campus.show()
# class Factory:
#     def __init__(self,age):
#         self.age=age
#     def show(self):
#         print(f"your age is {self.age}")        
#     @classmethod
#     def hello(cls):
#         print("how are you")
#     @staticmethod
#     def static():
#         print("how are you")

# obj = Factory(12)
# obj.show()
# obj.hello()
# obj.static()
# class Factory:
#     a= "i m mentioned inside class factory"
#     def hello(self):
#         print("how are you")
# class SubFactory(Factory):
#     pass
# obj=Factory()
# obj2=SubFactory()
# obj.hello()
# obj2.hello()
# class Animal:
#     def show2(self):
#         print("how are you ")
# class Human(Animal):
#     def show(self):
#         print("Heyooo")
# obj=Human()
# obj.show2()
# class Animal:
#     def show(self):
#         print("hello")
# class Human:
#     def show(self):
#         print("hello i am working")
# obj = Human()
# onj2= Animal()
# obj.show()
# onj2.show()

class Factory:
    a = "pune"
    def show(self):
        print("i am pune factory")
class Bhopal(Factory):
    def show2(self):
        print(super().a)
obj = Bhopal()
obj.a="mumbai"
print(obj.a)

        

