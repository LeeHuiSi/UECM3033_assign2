# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:16:22 2016

@author: HuiShi
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

# new picture Tree.tiff
img = mpimg.imread('fruit.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]


fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.savefig('ori_img.png')
plt.show()


# Decompose Red matrix
U_r, TS_r, V_r = np.linalg.svd(r, full_matrices = True, compute_uv = True)

# Decompose Green matrix
U_g, TS_g, V_g = np.linalg.svd(g, full_matrices = True, compute_uv = True)

# Decompose Blue matrix
U_b, TS_b, V_b = np.linalg.svd(b, full_matrices = True, compute_uv = True)

# convert Sigma from vector to diagonal matrix
S_r = np.zeros((800,1000))
S_g = np.zeros((800,1000))
S_b = np.zeros((800,1000))

for i in range(800):
    S_r[i][i] = TS_r[i]
    S_g[i][i] = TS_g[i]
    S_b[i][i] = TS_b[i]

# Compress - Lower resolution picture
S_r_first30 = np.zeros((800,1000))
S_g_first30 = np.zeros((800,1000))
S_b_first30 = np.zeros((800,1000))

# keeping the first 30 none zero elements as Sigma
s_red_new[0:30] = s_red[0:30]
rnew = U_red@s_red_new@Vh_red

#create new plot
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_new)
ax2.imshow(Red_30, cmap = 'Reds')
ax3.imshow(Green_30, cmap = 'Greens')
ax4.imshow(Blue_30, cmap = 'Blues')
plt.savefig('new_img.png')
plt.show()

#save the new image
img_new2 = Image.fromarray(img_new,'RGB')
img_new2.save('lowResolution_Tree.jpg')
        
###### Better resolution 200 ######
#create new image with better resolution
Red_S_200 = np.zeros((800,1000))
Green_S_200 = np.zeros((800,1000))
Blue_S_200 = np.zeros((800,1000))

for i in range(200):
    Red_S_200[i][i] = Red_S[i][i]
    Green_S_200[i][i] = Green_S[i][i]
    Blue_S_200[i][i] = Blue_S[i][i]
    
#combine USV to single matrix
Red_200 = np.asmatrix(Red_U)* np.asmatrix(Red_S_200)*np.asmatrix(Red_V)
Green_200 = np.asmatrix(Green_U)* np.asmatrix(Green_S_200)*np.asmatrix(Green_V)
Blue_200 = np.asmatrix(Blue_U)* np.asmatrix(Blue_S_200)*np.asmatrix(Blue_V)

#combine new RGB into new image
img_better = img
img_better[:,:,0] = Red_200
img_better[:,:,1] = Green_200
img_better[:,:,2] = Blue_200

#create new plot
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img_better)
ax2.imshow(Red_30, cmap = 'Reds')
ax3.imshow(Green_30, cmap = 'Greens')
ax4.imshow(Blue_30, cmap = 'Blues')
plt.savefig('img_better.png')
plt.show()

#save the new image
img_better = Image.fromarray(img_better,'RGB')
img_better.save('BetterResolution_Tree.jpg')