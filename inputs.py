age=input("enter your age: ") #gets age
amount=int(input("how many times would you like to receive this message? ")) #gets repitition amount
add = 100 - int(age) #gets number of years until userturns 100
year= 2018 + int(add)#adds that number to current year
print(amount *('you will turn 100 in the year: '+ str(year)+'\n'))#prints message

