import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.linalg as sp

img=mpimg.imread('fruit.jpg')
img2=mpimg.imread('fruit.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]

U_r,s_r,Vh_r = sp.svd(r,False,True,False,True)
U_g,s_g,Vh_g = sp.svd(g,False,True,False,True)
U_b,s_b,Vh_b = sp.svd(b,False,True,False,True)

# convert Sigma from vector to diagonal matrix
s_r = np.diag(s_r)
s_g = np.diag(s_g)
s_b = np.diag(s_b)

#print('There are ' + str(len(s_red)) + ' elements in Sigma matrix')
# Compress - Lower resolution picture
s_r_new = np.zeros_like(s_r)
s_g_new = np.zeros_like(s_g)
s_b_new = np.zeros_like(s_b)

# keeping the first 30 none zero elements as Sigma
s_r_new[0:30] = s_r[0:30]
s_g_new[0:30] = s_g[0:30]
s_b_new[0:30] = s_b[0:30]

red_new   = U_r.dot(s_r_new).dot(Vh_r)
green_new = U_g.dot(s_g_new).dot(Vh_g)
blue_new  = U_b.dot(s_b_new).dot(Vh_b)

img[:,:,0] = red_new
img[:,:,1] = green_new
img[:,:,2] = blue_new

fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(red_new, cmap = 'Reds')
ax3.imshow(green_new, cmap = 'Greens')
ax4.imshow(blue_new, cmap = 'Blues')

plt.show()

# Compress - better resolution picture
s_r_new = np.zeros_like(s_r)
s_g_new = np.zeros_like(s_g)
s_b_new = np.zeros_like(s_b)

# keeping the first 200 none zero elements as Sigma
s_r_new[0:200] = s_r[0:200]
s_g_new[0:200] = s_g[0:200]
s_b_new[0:200] = s_b[0:200]

red_new   = U_r.dot(s_r_new).dot(Vh_r)
green_new = U_g.dot(s_g_new).dot(Vh_g)
blue_new  = U_b.dot(s_b_new).dot(Vh_b)

img2[:,:,0] = red_new
img2[:,:,1] = green_new
img2[:,:,2] = blue_new

fig = plt.figure(2)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img2)
ax2.imshow(red_new, cmap = 'Reds')
ax3.imshow(green_new, cmap = 'Greens')
ax4.imshow(blue_new, cmap = 'Blues')

plt.show()
