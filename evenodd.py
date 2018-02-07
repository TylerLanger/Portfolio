number=int(input('input a number: '))#gets integer 
remainder=number%2 #determines remainder to see if integer is even
remainderfour=number%4 #check if integer is multiple of 4
if remainderfour == 0: 
    print('your number is a multiple of 4!')#if its a multiple of 4 let the user know
elif remainderfour != 0 and remainder ==0:
    print('your number is even')#if its a multiple of 2 let the user know
elif remainder != 0:
    print('your number is odd')#if its odd let the user know
    
