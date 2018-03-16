from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")

# # Generate a large random dataset
# rs = np.random.RandomState(33)
# d = pd.DataFrame(data=rs.normal(size=(100, 26)),
#,,,,,,columns=list(ascii_letters[26:]))

# # Compute the correlation matrix
# corr = d.corr()

corr = np.array([[988,0,0,0,4,0,2,0,5,1],
 [0,990,1,1,1,1,0,6,0,0],
 [0,2,996,1,1,0,0,0,0,0],
 [2,71,1,731,51,20,88,28,3,5],
 [1,3,0,7,918,23,4,31,9,4],
 [1,3,0,3,0,964,3,5,21,0],
 [1,0,1,7,1,3,972,0,6,9],
 [0,16,0,0,22,26,0,931,2,3],
 [2,3,0,0,2,2,12,0,972,7],
 [0,3,1,1,7,3,11,5,9,960]])

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(1000, 500, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, square=True, annot=True, fmt='d',center=500)

plt.show()