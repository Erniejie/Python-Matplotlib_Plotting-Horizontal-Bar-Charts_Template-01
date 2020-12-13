# PLOTTING A HORIZONTAL BAR CHART-JIE JENN YT

import numpy as np
import matplotlib.pyplot as plt

labels =["A","B","C"]
values = [1000,2000,3000,]

plt.style.use("ggplot")

fig,ax = plt.subplots(figsize=(10,5))

#horizontal bar charts 
ax.barh(labels,values)


plt.show()
