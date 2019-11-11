import cv2
import numpy as np

def polygonArea(X, Y, n): 
    area = 0.0
  
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i         
  
    return int(abs(area / 2.0)) 

X=[]
X1=[]
Y=[]
Y1=[]
sides =int(input("Enter the number of sides :"))
for vertice in range(1,(sides+1)):
  X.append(int((input("Enter the x co-ordinate of the side " +str(vertice)+" : "))))
  Y.append(int((input("Enter the y co-ordinate of the side " +str(vertice)+" : "))))

n = int(len(X)) 
print(polygonArea(X, Y, n)) 

#Making the image
img = np.zeros([512,512,1],dtype=np.uint8)
img.fill(255)
for x,y in range(0,n):
  cv2.line(img,(X[x],Y[y]),(X[x+1],Y[y+1]),(0,0,0),5)
cv2.imshow('Single Channel Window', img)

print("image shape: ", img.shape)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



