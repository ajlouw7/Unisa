import pandas as pd
import numpy as np 
import Utils as utils
import kNN as knn
import kfold as kfold

class CentroidData:
    centoid = []
    nearestDataPoints = []

df = pd.read_csv("test.csv")
x_df = df[['Health_Expenditure','GDP_Per_Capita','Education','Unemployment']]
y_df = df[['Life_Expectancy']]

def randomN(df):
    return pd.DataFrame( np.random.rand(1,11), columns=df.columns)

def getKCentroids(k,df):
    list = []
    for i in range(k):
        list.append( randomN(df) )
    return list
    

#sort datapoints according to nearest centroid


def getInitialCentroidDatas(k,df):    
    centroidDatas = []
    centroids = getKCentroids(k,df)
    for i in range(len(centroids)):
        centroidData = CentroidData()
        centroidData.centoid = centroids[i]
        centroidData.centoid.Country_Name = 'Centroid' + str(i)
        centroidData.nearestDataPoints = pd.DataFrame( columns=df.columns)
        centroidDatas.append(centroidData)
    return centroidDatas

def getClosestCentroid(datapoint,centroidDatas):
    closestCentroidData = []
    closestDistance = 9999999999.9
    for i in range(len(centroidDatas)):
        distance = knn.distance(centroidDatas[i].centoid, datapoint)
        if( distance < closestDistance):
            closestCentroidData = centroidDatas[i]
            closestDistance = distance
    return closestCentroidData


#closest = getClosestCentroid(df.head(1),centroidDatas )


def getMeanPoint(nearestDataPoints,trainingData):
    meanPoint = randomN(trainingData)

    meanPoint.head(1).Health_Expenditure = nearestDataPoints['Health_Expenditure'].mean()
    meanPoint.head(1).GDP_Per_Capita = nearestDataPoints['GDP_Per_Capita'].mean()
    meanPoint.head(1).Unemployment = nearestDataPoints['Unemployment'].mean()
    meanPoint.head(1).Education = nearestDataPoints['Education'].mean()
    return meanPoint






def CalculateCentroids(trainingData, k):
    centroidDatas = getInitialCentroidDatas(k,trainingData)  
    for j in range(100):
        #assign training data point to closest centroid
        for i in range(len(trainingData)):
            dataRow = trainingData.iloc[i]
            centroidData = getClosestCentroid( dataRow, centroidDatas)
            centroidData.nearestDataPoints = centroidData.nearestDataPoints.append( dataRow, ignore_index=True )

        
        for i in range(len(centroidDatas)):
            newCentroid = getMeanPoint(centroidDatas[i].nearestDataPoints,trainingData)
        
        
        
        
            #calculate mean of data points assigned to the centroid
            #newCentroid = utils.GetMeanPointOfDataset( centroidDatas[i].nearestDataPoints)
            #get the change in position of the centroid
            old = kfold.getX(centroidDatas[i].centoid)
            new = kfold.getX(newCentroid)
            diffrenceInCentroid = old - new 
            print( "centroid difference" + str(i) )
            print( diffrenceInCentroid )
            #set new mean of data points as the new centroid
            centroidDatas[i].centoid = newCentroid
            #removing all nearest points
            centroidDatas[i].nearestDataPoints.dropna()
    return centroidDatas


k = 2

cen = CalculateCentroids(kfold.testSet(1).trainingDF, k)




#l = getKCentroids(2)

#a = randomN()

dist = utils.GetEuclideanDistanceBetweenFeatureVectors( a, x_df.head(1).to_numpy())






b = 1