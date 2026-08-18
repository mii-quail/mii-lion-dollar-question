import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom
from scipy.stats import norm
# np = mean of a binomial. we know there are 1000 freerange Miis, so we can work out an estimate of p.
n = 1000
p = 0.071652
# height ranges from 0 to 127, with 0 being 140cm, 127 being 203.5cm, and a linear scale between
df=pd.read_csv(r"C:\Users\chees\OneDrive\Microsoft Teams Chat Files\Documents\world.csv")
def height(miiheight):
    miiheight*=0.5
    miiheight+=140
    return miiheight
# exploratory data analysis
print(df[df["dataset"]=="nnid"].describe())
print(height(df[df["dataset"]=="nnid"]["body_height"].mean()))
print(height(df[df["dataset"]=="nnid"]["body_height"].std())-140)
# so I can plot the distribution of the empirical data alongside a binomial
counts = df[df["dataset"]=="nnid"]["body_height"].value_counts().sort_index()
# the data linearly coded to match human heights
x=0.5*counts.index + 140
y=counts.values / 1000
# binomial approximation of the data
xbin = 0.5*np.arange(128) + 140
ybin= np.array([binom.pmf(k,n,p) for k in range(128)])
# normal distribution of real life human height
xnorm = np.linspace(140, 203.5, 1000) # the 1000 value means this is really a pseudo-continuous distribution
ynorm = norm.pdf(xnorm,loc=171.55, scale=(107.59)**0.5) # Our World in Data: human height worldwide H ~ N(171.55, 107.59)
plt.bar(xnorm,ynorm,color="green",label="normal of human height",alpha=0.01)
plt.bar(x,y,color="blue",label="empirical of Mii height",alpha=0.3)
plt.bar(xbin,ybin,color="red",label="binomial of Mii height",alpha=0.3)
plt.xlabel("Mii heights / cm")
plt.ylabel("Probability")
plt.legend()
plt.show()
