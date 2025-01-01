import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 2])
w = np.array([4, -6])
vPlusW = v + w
vMinusW = v - w

plt.figure(figsize=(6,6))
a1 = plt.arrow(0,0,v[0],v[1],head_width=.3,width=.1,color='k',length_includes_head=True)

plt.grid(linestyle='--',linewidth=.5)
plt.axis('square')
plt.axis([-6,6,-6,6])

print("v+w want, input 0 \nv-w want, input 1\n")
key = int(input())
if key == 0:
    a2 = plt.arrow(v[0],v[1],w[0],w[1],head_width=.3,width=.1,color=[.5,.5,.5],length_includes_head=True)
    a3 = plt.arrow(0,0,vPlusW[0],vPlusW[1],head_width=.3,width=.1,color=[.8,.8,.8],length_includes_head=True)
    plt.legend([a1,a2,a3],['v','w','v+w'])
    plt.title('Vectors v, w and v+w')

else:
    a4 = plt.arrow(0,0,w[0],w[1],head_width=.3,width=.1,color=[.5,.5,.5],length_includes_head=True)
    a5 = plt.arrow(w[0],w[1],vMinusW[0],vMinusW[1],head_width=.3,width=.1,color=[.8,.8,.8],length_includes_head=True)
    plt.legend([a1,a4,a5],['v','w','v-w'])
    plt.title('Vectors v, w, and v-w')

#plt.savefig('Figure_01_02a.png',dpi=300) # write out the fig to a file
plt.show()