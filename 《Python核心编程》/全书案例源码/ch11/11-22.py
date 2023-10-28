import numpy as np
import matplotlib.pyplot as plt
import matplotlib

labels = np.array(['attack', 'price', 'load', 'speed', 'switch','pass'])
attrNum = 6
data = np.array([7, 5, 6, 9, 8, 7]) 
angles = np.linspace(0, 2*np.pi, attrNum, endpoint=False)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure(facecolor="white")
plt.subplot(1,1,1, polar=True)
plt.plot(angles,data,'bo-',color ='g',linewidth=2)
plt.fill(angles,data,facecolor='g',alpha=0.25)
plt.thetagrids(angles*180/np.pi, labels)
plt.figtext(0.52, 0.95, 'CSGO:AWP', ha='center')
plt.grid(True)
plt.show()