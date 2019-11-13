import cv2
import numpy as np
from shapely.geometry import Polygon

def polygonArea(X, Y, n): 
    area = 0.0
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i         
  
    return int(abs(area / 2.0)) 

def combineXY(X,Y):
  bothXY=[]
  for i in range(len(X)):
    temp=[]
    for j in range(1):
        temp.append(X[i])
        temp.append(Y[i])
        bothXY.append(temp)
  return bothXY

def centroidTotal(areaList, centroidList):
  shapeCentroid=[]
  areaSum=0
  sigmaX=0
  sigmaY=0
  for i in range(len(areaList)):
    areaSum += areaList[i]
    pointXY=centroidList[i][0]
    sigmaX+=areaList[i]*pointXY[0]
    sigmaY+=areaList[i]*pointXY[1]
  finalX=sigmaX/areaSum
  finalY=sigmaY/areaSum
  shapeCentroid.append(finalX)
  shapeCentroid.append(finalY)
  return shapeCentroid

areaList=[]
centroidList=[]
img = np.zeros([512,512,1],dtype=np.uint8)
img.fill(255)
cv2.line(img,(256,0),(256,512),(0,0,0),1)
cv2.line(img,(0,256),(512,256),(0,0,0),1)
for choice in range(int(input("Enter a number OF shapes : "))):
  X=[]
  Y=[]
  for vertice in range(1,(int(input("Enter the number of sides :"))+1)):
    print("Note the maximum lenth is 256 units")
    X.append(int((input("Enter the x co-ordinate of the side " +str(vertice)+" : "))))
    Y.append(int((input("Enter the y co-ordinate of the side " +str(vertice)+" : ")))) 
  for x in range(len(X)-1):
    cv2.line(img,(X[x]+256,256-Y[x]),(X[x+1]+256,256-Y[x+1]),(0,0,0),2)
  cv2.line(img,(X[0]+256,256-Y[0]),(X[len(X)-1]+256,256-Y[len(X)-1]),(0,0,0),2)
  areaList.append(polygonArea(X, Y, len(X)))
  centroidList.append(list(Polygon(combineXY(X,Y)).centroid.coords))

print("The centroids are "+str(centroidList))
print("The areas are "+str(areaList))
print("The centroid of the whole shape is "+str(centroidTotal(areaList,centroidList)))
cv2.imshow('Single Channel Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


