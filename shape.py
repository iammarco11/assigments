areaList=[50, 100]
centroidList=[(3.333333333333333, 3.333333333333333)], [(5.0, -5.0)]]
shapeCentroid=[]
areaSum=0
for i in range(len(areaList)):
    areaSum += areaList[i]
    sigmaX=areaList[i]*centroidList[i][0]
    sigmaY=areaList[i]*centroidList[i][1]
finalX=sigmaX/areaSum
finalY=sigmaY/areaSum
shapeCentroid.append(finalX)
shapeCentroid.append(finalY)
print(shapeCentroid)