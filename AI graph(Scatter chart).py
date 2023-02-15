import numpy as ny
# import matplotlib.pyplot as plt
from matplotlib import *

x=ny.random.normal(20,40,100)
y=ny.random.normal(10,20,100)
z=ny.random.normal(20,20,100)
w=ny.random.normal(50,20,100)

plt.scatter(x,y,color='#00FF00',s=100)
plt.scatter(z,w,color='b',s=100)
plt.show() 