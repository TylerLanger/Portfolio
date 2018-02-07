import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename='Weather2.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row = next(reader)

    dates, highs, means, lows=[],[],[],[]
    for row in reader:
        current_date= datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
                                        
        high=int(row[1])
        highs.append(high)
        mean=int(row[2])
        means.append(mean)
        low=int(row[3])
        lows.append(low)
        
    #print(highs)


#plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, means, c='green', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows,means, facecolor='blue', alpha=0.1)

#format plot
plt.title("daily high and low temps, july 2014", fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("tempurature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.show()
