import matplotlib.pyplot as p

values=[1,2,3,4,5]
squares=[1,4,9,16,25]

p.plot(values, squares, linewidth=5)

p.title("square numbers", fontsize=24)
p.xlabel("value", fontsize=14)
p.ylabel("square of value", fontsize=14)

p.tick_params(axis='both', labelsize=14)

p.show()

