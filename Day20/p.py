#06/10/25

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


sns.scatterplot(x=np.array(2,3,4),y=np.array([4,2,8]),s=250,marker="#",colot="r")
plt.grid(True)
plt.show()
