import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
# lots of variable definitions. mole count gives the count of moles, although I guess I don't need this
# it's just there to make sure everything's working okay
# zolecount gives the amount of data cleaned
# the c in front of the names of arrays means it's for celebrity data
molecount=[0,0]
zolecount=[0,0]
xpoints=[]
cxpoints=[]
ypoints=[]
cypoints=[]
sizes=[]
csizes=[]
# not perfect image but an approximation of where the mole goes. Remember Miis are 3D and
# the image is 2D
img=plt.imread("default.png")
df=pd.read_csv("world.csv")
# collect the data, add it to the array as needed
for i in range(1000):
    toggle = df.iloc[i]["mole_enable"]
    x,y = df.iloc[i]["mole_horizontal"], -df.iloc[i]["mole_vertical"]
    size = df.iloc[i]["mole_size"]
    if toggle and x<=16 and x>=0 and y>=-30 and y<=0 and size<=8 and size>=0:
        molecount[0]+=1
        xpoints+=[x]
        ypoints+=[y]
        sizes+=[size]
    elif toggle:
        zolecount[0]+=1
        print(i)
for i in range(1000,1050):
    toggle = df.iloc[i]["mole_enable"]
    x,y = df.iloc[i]["mole_horizontal"], -df.iloc[i]["mole_vertical"]
    size = df.iloc[i]["mole_size"]
    if toggle and x<=16 and x>=0 and y>=-30 and y<=0 and size<=8 and size>=0:
        molecount[1]+=1
        cxpoints+=[x]
        cypoints+=[y]
        csizes+=[size]
    elif toggle:
        zolecount[1]+=1
# so we can do some EDA
xpoints = np.array(xpoints)
ypoints = np.array(ypoints)
cxpoints = np.array(cxpoints)
cypoints = np.array(cypoints)
df2=pd.DataFrame({"x":xpoints,"y":ypoints,"s":sizes})
df3=pd.DataFrame({"x":cxpoints,"y":cypoints,"s":csizes})
print(df2.describe())
print(df3.describe())
# Kmeans stuff :D
data = list(zip(np.concatenate([xpoints,cxpoints]),np.concatenate([ypoints,cypoints])))
inertias = []
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
# so we can plot with the sizes
fig,ax=plt.subplots()
ax.imshow(img,extent=[0,16,-30,0],aspect="auto")
ax.scatter(xpoints,ypoints,marker="*",alpha=0.2,color="blue",label="freerange",s=np.array(sizes)*10)
ax.scatter(cxpoints,cypoints,marker="*",alpha=0.2,color="red",label="celebrity",s=np.array(csizes)*10)
plt.xlabel("Horizontal")
plt.ylabel("Vertical")
ax.legend()
plt.xlim(0, 16)
plt.ylim(-30, 0)
plt.show()
# the inertias of the data. used to find the elbow. I can just eyeball it luckily, so no need for silhouette
plt.plot(range(1,11), inertias, marker="*")
# knee point
diffs=np.diff(inertias)
second_diffs=np.diff(diffs)
print(second_diffs)
print(np.argmax(second_diffs)+2)
plt.show()
kmeans=KMeans(n_clusters=2, random_state=67) # the elbow is 2, but I made a mistake
# and I thought it was 3. for that reason I accidentally started with 3, but it's lowkey more
# interesting. I'll plot both.
kmeans.fit(data)
plt.figure()
plt.imshow(img,extent=[0,16,-30,0],aspect="auto")
plt.scatter(np.concatenate([xpoints,cxpoints]),np.concatenate([ypoints,cypoints]),marker="*",s=np.concatenate([sizes,csizes])*10,c=kmeans.labels_)
plt.xlabel("Horizontal")
plt.ylabel("Vertical")
plt.xlim(0, 16)
plt.ylim(-30, 0)
plt.show()
kmeans=KMeans(n_clusters=3, random_state=67) 
kmeans.fit(data)
plt.figure()
plt.imshow(img,extent=[0,16,-30,0],aspect="auto")
plt.scatter(np.concatenate([xpoints,cxpoints]),np.concatenate([ypoints,cypoints]),marker="*",s=np.concatenate([sizes,csizes])*10,c=kmeans.labels_)
plt.xlabel("Horizontal")
plt.ylabel("Vertical")
plt.xlim(0, 16)
plt.ylim(-30, 0)
plt.show()
