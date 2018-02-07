import matplotlib.pyplot as p

values=[1,2,3,4,5,6]
cubes=[1,8,27,64,125,216]

p.plot(values, cubes, linewidth=5)

p.title("cubed numbers", fontsize=24)
p.xlabel("value", fontsize=14)
p.ylabel("cube of value", fontsize=14)

p.tick_params(axis='both', labelsize=14)

p.show()

