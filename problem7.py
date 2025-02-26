##Write a program to get firstName and lastName and n as input and print fullName that is firstName+lastName for n times.


firstname=input("Enter the First Name:")
secondname=input("Enter the Second Name:")
n=int(input("Enter the no of times to print:"))

both=firstname+secondname
for i in range(n):
    print(both)


