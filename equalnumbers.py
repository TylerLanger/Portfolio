num1 = int(input("input a number: " ))
num2 = int(input("input a second number: "))#gets number
num3 = int(input("input a third number: " ))

if num1== num2 and num1==num3: #determines if numbers are equal
    print(3)
elif num1==num2 and num1!=num3:
    print(2)
elif num1!=num2 and num1!=num3 and num2!=num3:
    print(0)
elif num2==num3 and num2!=num1:
    print(2)
elif num3==num1 and num2!=num3:
    print(2)
