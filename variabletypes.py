class phone():
    chargertype="c-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)
samsung=phone("samsung","10000")
redmi=phone("redmi","7000")
google=phone("pixel","23000")

samsung.display()
redmi.display()
google.display()
