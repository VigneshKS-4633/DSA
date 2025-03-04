##Write a program using switch case which takes a value and prints the respective Size.
##If size is 29 then its small
##
##If size is 30 then its Medium
##
##If size is 38 then its Large
##
##If size is 42 then its XLarge
##
##If size is not any of the above then Invalid.

def size_category(size):
    match size:
        case 29:
            return "Small"
        case 30:
            return "Medium"
        case 38:
            return "Large"
        case 42:
            return "XLarge"
        case _:
            return "Invalid"

# Taking size as input
size = int(input("Enter the size: "))

# Determining and printing the size category
print("Size Category:", size_category(size))
