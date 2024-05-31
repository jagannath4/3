import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

plt.hist(mtcars['mpg'], bins=10, color='skyblue', edgecolor='black')

plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')

plt.show()
