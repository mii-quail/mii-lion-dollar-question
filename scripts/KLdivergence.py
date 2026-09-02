import pandas as pd
import numpy as np
from scipy.stats import binom
from scipy.stats import entropy
df = pd.read_csv("world.csv")
for power in range(-20,21):
 # empirical distribution
 heights = df[df["dataset"]=="nnid"]["body_height"].value_counts().sort_index() # gives you the amount of miis that are that height
 empirical = np.zeros(128) # 128 different heights, integers from 0-127
 for i, j in heights.items(): # populates with the data
     empirical[int(i)] = j
 for i in range(len(empirical)):
     empirical[i]+=10**power
 empirical/=empirical.sum() # normalises it so its a prob dist
 # binomial distribution
 n = 127
 p = 0.564188976
 bindist = np.array([binom.pmf(k, n, p) for k in range(128)]) # gives each probability for the binomial
 # KL divergence
 kl = entropy(empirical, bindist) # uses binomial distribution as an approximation
 kl2 = entropy(bindist,empirical) # can a stats noob learn what a binomial distribution looks like through the mii data?
 print("For buffer order of magnitude " + str(power))
 print(kl)
 print(kl2)
 print("")
message="So what I see makes sense ngl. This is my first time properly applying KL divergence"
message+=", and I'm getting it. The problem with the binomial model is that it's too low relative"
message+=" to the empirical data. The more we push it up, the higher the KL empirical||bindist."
message+=" However, boosting the laplace smooth makes the data more relative, which actually"
message+=" seems to lower the KL bindist||empirical."
print(message)
