##class student:
##    def __init__(self):
##        self.name="vignesh"
##        self.register="1CR23MC118"
##    def display(self):
##        print("name:",self.name)
##        print("register:",self.register)
##s1=student()
##s2=student()
##s3=student()
##
##s1.name="manoj"
##s1.register="1cr23mc111"
##s2.name="preethi"
##s2.register="1cr23mc011"
##s1.display()
##s2.display()    
##s3.display()
##

##class fruit:
##    def __init(self,col):
##        self.color=col
##apple=fruit("red")
##print(apple.color)

##class teacher:
##    def __init__(self,name,regno):
##        self.name=name
##        self.regno=regno
##    def display(self):
##        print("name:",self.name)
##        print("regno:",self.regno)
##t1=teacher("alpha","1")
##t2=teacher("beta","2")
##t1.display()
##t2.display()
##        

class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        print(a/b)

