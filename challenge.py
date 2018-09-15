from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import webcolors as wc

im = Image.open("image.png")
pixel = list(im.getdata())
array = np.asarray(pixel)
array = np.reshape(array,(1000,1000,3))

plt.imshow(array/255)
plt.show()

list_quad = []
list_trois = []
list_deux = []
list_une = []

count = 0

# loop over bigger blocks
for i in range(0,20): # (0,20) 
	for j in range(0,20): # (0,20)
		count = count + 1
		minCount = 4
		x_from, x_to = 50*i+ 1, 50*(i+1)
		y_from,y_to = 50*j+ 1, 50*(j+1)
		# print("Block:", count ," x:(", x_from ,":", x_to ,"); y:(", y_from,":",y_to,")")
		#print( array[x_from:x_to,y_from:y_to,:] )
		
		# What is the block and its color?
		# tuple = tuple(array[0,0,:].reshape(1,-1)[0])
		# wc.rgb_to_name(tuple)
		# if (count == 101):
		# print ("mini block 1: x:(", x_from ,":", x_from+10 ,"); y:(", y_from,":",y_from+10,")")
		# print ("mini block 1: ", array[x_from:x_from+10,y_from:y_from+10,:])
		# print ("mini block 1: ", np.mean(array[x_from:x_from+10,y_from:y_from+10,:],axis=(0,1)))

		#Top-left
		if np.sum([ [1 if np.mean(b,dtype=int)==255 or np.mean(b,dtype=int)==0 else 0 for b in a] for a in array[x_from:x_from+10,y_from:y_from+10,:] ]) != 0:
			minCount = minCount - 1

		# print ("mini block 2: x:(", x_to-10 ,":", x_to ,"); y:(", y_from,":",y_from+10,")")
		# print ("mini block 2: ", array[x_to-10:x_to,y_from:y_from+10,:])
		# print ("mini block 2: ", np.mean(array[x_to-10:x_to,y_from:y_from+10,:],axis=(0,1)))

		# top-right
		if np.sum([ [1 if np.mean(b,dtype=int)==255 or np.mean(b,dtype=int)==0 else 0 for b in a] for a in array[x_to-10:x_to,y_from:y_from+10,:] ]) != 0:
			minCount = minCount - 1

		# print ("mini block 3: x:(", x_from ,":", x_from+10 ,"); y:(", y_to-10,":",y_to,")")
		# print ("mini block 3: ", array[x_from:x_from+10,y_to-10:y_to,:])
		# print ("mini block 3: ", np.mean(array[x_from:x_from+10,y_to-10:y_to,:],axis=(0,1)))

		# bottom-left
		if np.sum([ [1 if np.mean(b,dtype=int)==255 or np.mean(b,dtype=int)==0 else 0 for b in a] for a in array[x_from:x_from+10,y_to-10:y_to,:] ]) != 0:
			minCount = minCount - 1

		# print ("mini block 4: x:(", x_to-10 ,":", x_to ,"); y:(", y_to-10,":",y_to,")")
		# print ("mini block 4: ", array[x_to-10:x_to,y_to-10:y_to,:])
		# print ("mini block 4: ", np.mean(array[x_to-10:x_to,y_to-10:y_to,:],axis=(0,1)))

		# bottom-right
		if np.sum([ [1 if np.mean(b,dtype=int)==255 or np.mean(b,dtype=int)==0 else 0 for b in a] for a in array[x_to-10:x_to,y_to-10:y_to,:] ]) != 0:
			minCount = minCount - 1

		if minCount == 4:
			list_quad.append((x_from,x_to,y_from,y_to))
		elif minCount == 3:
			list_trois.append((x_from,x_to,y_from,y_to))
		elif minCount == 2:
			list_deux.append((x_from,x_to,y_from,y_to))
		else: 
			list_une.append((x_from,x_to,y_from,y_to))
# size?
# len(list_une), len(list_deux), len(list_trois), len(list_quad)

# Create ordered array
ord_array = [] # np.zeros(array.shape)

# Print blocks in list_une
for elem in list_une:
	temp_array = array[elem[0]:elem[1],elem[2]:elem[3],:]
	#plt.imshow(temp_array/255)
	#plt.show()

	# Start forming the image
	# Start from the top-left block. That is the one which has a colour block bottom-right.
	if np.sum([ [1 if np.mean(b,dtype=int)==255 or np.mean(b,dtype=int)==0 else 0 for b in a] for a in temp_array[40:50,40:50,:] ]) != 0:
		ord_array.append(temp_array)

# Print ordered array
temp = np.array([np.array(xi/255) for xi in ord_array])
plt.imshow( np.reshape(temp,(1000,1000,3)) )
plt.show()

