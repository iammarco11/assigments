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

areaList=[]
centroidList=[]
inertiaList=[]
img = np.zeros([512,512,1],dtype=np.uint8)
img.fill(255)
cv2.line(img,(256,0),(256,512),(0,0,0),1)
cv2.line(img,(0,256),(512,256),(0,0,0),1)
for choice in range(int(input("Enter a number OF shapes : "))):
    X=[]
    Y=[]
    Cx=0.0
    Cy=0.0
    Ix=0.0
    Iy=0.0
    n = int(input("Enter the number of sides :"))
    for vertice in range(1,n+1):
        print("")
        print("Note the maximum length is 256 units")
        print("Also note to enter the vertices in counter-clockwise direction")
        print("Make sure to ensure that the coordinates are entered w.r.t your origin of choice")
        print("")
        X.append(int((input("Enter the x co-ordinate of the vertex " +str(vertice)+" : "))))
        Y.append(int((input("Enter the y co-ordinate of the vertex " +str(vertice)+" : ")))) 
    for x in range(len(X)-1):
        cv2.line(img,(X[x]+256,256-Y[x]),(X[x+1]+256,256-Y[x+1]),(0,0,0),2)
    cv2.line(img,(X[0]+256,256-Y[0]),(X[len(X)-1]+256,256-Y[len(X)-1]),(0,0,0),2)
    areaList.append(polygonArea(X, Y, len(X)))
    for i in range(0,n):
        k=i+1
        if k>=n:
            k=0
        Cx+=(X[i]+X[k])*(X[i]*Y[k]-X[k]*Y[i])
        Cy+=(Y[i]+Y[k])*(X[i]*Y[k]-X[k]*Y[i])
        
    Cx=1/(6*areaList[choice])*Cx
    Cy=1/(6*areaList[choice])*Cy
    for i in range(len(X)):
        X[i]=X[i]+Cx
    for i in range(len(Y)):
        Y[i]=Y[i]+Cx
    for i in range(0,n):
        k=i+1
        if k>=n:
            k=0
        Ix+=(X[i]*Y[k]-X[k]*Y[i])*(Y[i]*Y[i]+Y[i]*Y[k]+Y[k]*Y[k])
        Iy+=(X[i]*Y[k]-X[k]*Y[i])*(X[i]*X[i]+X[i]*X[k]+X[k]*X[k])
    Ix=(1/12)*Ix
    Iy=(1/12)*Iy
    tempList1=[]
    tempList1.append(Cx)
    tempList1.append(Cy)
    centroidList.append(tempList1)
    tempList2=[]
    tempList2.append(Ix)
    tempList2.append(Iy)
    inertiaList.append(tempList2)

print("The centroids are "+str(centroidList))
print("The moment of inertias are "+str(inertiaList))
print("The areas are "+str(areaList))
cv2.imshow('Single Channel Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



