import pandas as pd
import numpy as np 
import Utils as utils

class CentroidData:
    centoid = []
    nearestDataPoints = []

df = pd.read_csv("test.csv")
x_df = df[['Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]
y_df = df[['Life_Expectancy']]

def randomN():
    return np.random.rand(1,4)

def getKCentroids(k):
    list = []
    for i in range(k):
        list.append( randomN() )
    return list
    

#sort datapoints according to nearest centroid
k = 2

centroidDatas = []
centroids = getKCentroids(k)
data = x_df.to_numpy()



for i in range(len(centroids)):
    centroidData = CentroidData()
    centroidData.centoid = centroids[i]
    centroidData.nearestDataPoints = []
    centroidDatas.append(centroidData)

def getClosestCentroid(datapoint,centroidDatas):
    closestCentroidData = []
    closestDistance = 9999999999.9
    for i in range(len(centroidDatas)):
        distance = utils.GetEuclideanDistanceBetweenFeatureVectors(centroidDatas[i].centoid, datapoint)
        if( distance < closestDistance):
            closestCentroidData = centroidDatas[i]
            closestDistance = distance
    return closestCentroidData

for j in range(100):
    for i in range(len(data)):
        centroidData = getClosestCentroid( data[i], centroidDatas)
        centroidData.nearestDataPoints.append( data[i] )

    for i in range(len(centroidDatas)):
        newCentroid = utils.GetMeanPointOfDataset( centroidDatas[i].nearestDataPoints)
        diffrenceInCentroid = centroidDatas[i].centoid - newCentroid
        print( "centroid difference" + str(i) )
        print( diffrenceInCentroid )
        centroidDatas[i].centoid = newCentroid
        centroidDatas[i].nearestDataPoints = []






l = getKCentroids(2)

a = randomN()

dist = utils.GetEuclideanDistanceBetweenFeatureVectors( a, x_df.head(1).to_numpy())






b = 1