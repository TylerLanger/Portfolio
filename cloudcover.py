import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='Weather2.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row = next(reader)

    dates, clouds=[],[]
    for row in reader:
        current_date= datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
                                        
        cloud=int(row[20])
        clouds.append(cloud)
        
    #print(highs)


#plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, clouds, c='red', alpha=0.5)

#format plot
plt.title("Cloud cover, july 2014", fontsize=24)
plt.xlabel('', fontsize=2)
fig.autofmt_xdate()
plt.ylabel("Cloud cover", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()
