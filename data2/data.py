#You will write a Python program that does some interesting analysis on one or more data sets.
#Text analysis or use two data sources, use csv
#Use Matplotlib to visualize part or all of your analysis. - maybe
#Use multiple aspects of a single data source in your analysis - definitely
#Use more than one data source and have your analysis compare,contrast, or correlate them. - no
#Do an analysis that includes the language processing work (Bag of Words type analysis for example). - yes

import csv
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

