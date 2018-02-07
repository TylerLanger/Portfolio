units= input('enter units used: ')#gets units
Hyp=int(input('input hypotenuse:'))#GETS hypotenuse
Side= int(input('input other known side:')) #gets other side
C2=(Hyp**2)-(Side**2) #determines C squared
C= C2**.5 #determines C
print('The length of the missing side is: '+ str(C) +units)#prints side length

