import matplotlib.pyplot as p

values=list(range(1, 1001))
squares=[x**2 for x in values]

p.scatter(values, squares, s=2, c=squares, cmap=p.cm.Blues, edgecolor="none")

p.title("square numbers", fontsize=24)
p.xlabel("value", fontsize=14)
p.ylabel("square of value", fontsize=14)

p.tick_params(axis='both', labelsize=14)

p.axis([0,1100,0,1100000])
p.show
p.savefig("squares_plot.png") 
