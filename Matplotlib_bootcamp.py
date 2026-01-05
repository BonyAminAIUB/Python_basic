import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("your_file.csv")
plt.hist(df['Study Hours'], edgecolor='black')
plt.xlabel('Study Hours') # X-axis a eta thakbe
plt.ylabel('Number of students') # Y-axis a eta thakbe
plt.show()  # Histogram show korbe

plt.scatter(df['Study_Hours'],df['Playing_Hours'])
plt.xlabel('Study_Hours') 
plt.ylabel('Playtime') 
plt.show() # Scatter type graph show korbe
