class Factory:
    def __init__(self,material,zip,pocekts):
        self.material=material
        self.zip=zip
        self.pockets=pocekts
    def show(self):
        print(f"the objects are {self.material} , {self.zip} , {self.pockets}")
reebok = Factory("leather",2,3)
campus = Factory("nylon",3,4)
reebok.show()
campus.show()
