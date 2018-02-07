num1 = int(input("input a number: " ))
num2 = int(input("input a second number: "))#gets number
num3 = int(input("input a third number: "))

if num1<num2 and num1<num3:
    print(num1)
elif num2<num1 and num2<num3:
    print(num2)
elif num3<num2 and num3<num1: #determines lowest and prints
    print(num3)
    
