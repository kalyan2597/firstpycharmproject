import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import sys

df=pd.read_csv('F:\\files\\Breast Cancer.csv')
sns.displot(df['radius_mean'])
plt.show()