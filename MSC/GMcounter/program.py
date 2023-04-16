import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv('counter.csv')
avg = df['Avg Count'].to_list()
volts = df['EHT(V)'].to_list()

# Plot 
plt.plot(volts,avg)
plt.xlabel('Volts')
plt.ylabel('Count rate')
plt.show()

# calculating operating voltage
vs = float(input("Enter the first point of plateau from the plot:"))
ve = float(input("Enter the last point of plateau from the plot:"))
vo = (vs+ve)/2
print("Operating voltage is ",vo)


# Determine the slope of plateau
cvs = float(input("Enter the count rate for first point of plateau:"))
cve = float(input("Enter the count rate for last point of plateau:"))
dcv = cve-cvs
dvo = ve-vs
cent_slope = (dcv/dvo)*100
print("Slope of plateau is ",cent_slope)
