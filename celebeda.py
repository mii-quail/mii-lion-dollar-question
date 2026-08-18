import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import pearsonr
# actual celebrity heights
realheights = [171.5, 167.6, 171.5, 188, 188, 180.3, 154.9, 164, 156.2, 168, 167, 182.2, 185, 160, 184.2, 177.8, 172.1, 167.6, 167.6, 173, 185, 194.9, 155, 183.5, 155.6, 155, 174.6, 190, 175.3, 158, 163.8, 175.3, 189.9, 185.4, 171.5, 210.1, 183, 172, 176.5, 185.4, 214, 192.4, 192.4, 180.3, 170, 185, 175.9, 190.5, 174, 174]
# height ranges from 0 to 127, with 0 being 140cm, 127 being 203.5cm, and a linear scale between
df=pd.read_csv(r"C:\Users\chees\OneDrive\Microsoft Teams Chat Files\Documents\world.csv")
def height(miiheight):
    miiheight*=0.5
    miiheight+=140
    return miiheight
# exploratory data analysis
print(df[df["dataset"]=="celebrity"].describe())
print(height(df[df["dataset"]=="celebrity"]["body_height"].mean()))
print(height(df[df["dataset"]=="celebrity"]["body_height"].std())-140)
celebheights = height(df[df["dataset"]=="celebrity"]["body_height"].values.astype(float).copy())
# r is the PMCC p is the pvalue for that PMCC
r, p = pearsonr(celebheights, realheights)
print("Here is the PMCC, R^2, and its p value")
print(r)
print(r**2)
print(p)
# linear regression
gradient, intercept, r, p, stderr = stats.linregress(celebheights,realheights)
def linear(i):
    return gradient * i + intercept
mymodel = list(map(linear,celebheights))
print("Here is the line data")
print("y = " + str(gradient) + "x + " + str(intercept))
plt.scatter(celebheights,realheights)
plt.plot(celebheights,mymodel)
plt.xlabel("Heights of the celebrity Mii / cm")
plt.ylabel("Heights of the actual Mii / cm")
plt.show()
