##Write a program to check whether a triangle can be formed with the given values for the angles.

angle_A=int(input("Enter the first angle:"))
angle_B=int(input("Enter the second angle:"))
angle_C=int(input("Enter the third angle:"))
if((angle_A + angle_B + angle_C) == 180):
    print("Triangle formed")
else:
    print("Triangle not formed")
