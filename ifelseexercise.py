##variable=int(input("Enter the income:"))
##if(variable>7000):
##    print("Scholorship is available")
##else:
##    print("Scholorship is not available")


##a=int(input("enter the number"))
##if(a%3==0):
##    print("Divisible by 3")
##else:
##    print("Not divisible by 3")
    

##a=int(input("enter the number"))
##if(a%3==0) and (a%5==0):
##    print("Divisible by 3 and 5")
##else:
##    print("Not divisible by 3 and 5")

##a=int(input("enter the number:"))
##if(a%2==0):
##    print("Its a even number")
##else:
##    print("Its a odd number")

##a=int(input("enter the Mark:"))
##if(a<35):
##    print("poor student")
##if(a>35 and a<70):
##    print("Average student")
##if(a>70):
##    print("Good student")


##a=int(input("enter the Mark:"))
##if(a<35):
##    print("poor student")
##elif(a>35 and a<70):
##    print("Average student")
##else:
##    print("Good student")

##a=int(input("enter the Mark:"))
##if(a<35):
##    print("fail")
##elif(a>=70 and a<=100):
##    print("good student")
##else:
##    print("invalid mark")

##a=int(input("A:"))
##b=int(input("B:"))
##operation=input("add/sub/mul/div")
##if(operation=="add"):
##    print(a+b)
##elif(operation=="sub"):
##    print(a-b)
##elif(operation=="mul"):
##    print(a*b)
##elif(operation=="div"):
##    print(a/b)
##else:
##    print("Invalid operation")
    
##percentage=int(input("Enter the percentage:"))
##if(percentage>=70):
##    print("you are eligible")
##    name=input("Enter your name:")
##    department=input("Enter your department:")
##    location=input("Enter your location:")
##    
##else:
##    print("you are not eligible")


##salary=int(input("Enter your salary:"))
##age=int(input("Enter your age:"))
##if(salary>=20000 or age<=25):
##        print("you are eligible to get loan")
##        loan=int(input("how much do you want:"))
##        if(loan>=50000):
##            print("not possible")
##        else:
##            print("Approved")
##else:
##    print("not eligible for loan")
    
           
sub1=int(input("Enter your sub1:"))
sub2=int(input("Enter your sub2:"))
sub3=int(input("Enter your sub3:"))
sub4=int(input("Enter your sub4:"))
sub5=int(input("Enter your sub5:"))
average=(sub1+sub2+sub3+sub4+sub5)/5
print("average of all sub:",average)
if(average<=35):
    print("Additional class is required")
else:
    print("you are good to go")
