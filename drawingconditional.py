import turtle
t=turtle.Pen()

t.color('blue','green')
t.begin_fill()

count=0

for x in range(1,9):
    t.forward(300)
    t.left(225)
    count=count+1
    print("Count is: " + str(count))

    #if count>7:
    if count>7 and count<9:
        print("the star is complete")
        break
    
t.end_fill()
print("Done")
