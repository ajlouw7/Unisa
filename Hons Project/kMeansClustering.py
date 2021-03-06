import pandas as pd
import numpy as np 
import Utils as utils
import kNN as knn
import kfold as kfold
import OLS as ols

class CentroidData:
    def __init__(self):
        self.centoid = []
        self.nearestDataPoints = []
        #for performance
        self.nearestDataPointsTempList = []
        #testing data for centroid
        self.testingData = []
        #for performance
        self.nearestDataPointsTempListForTestingData = []

class CentroidResults:
    def __init__(self):
        self.centroidData = []
        self.olsRuns = []

def randomN(df):
    return pd.DataFrame( np.random.rand(1,11), columns=df.columns)

def getKCentroids(k,df):
    list = []
    for i in range(k):
        list.append( randomN(df) )
    return list

def getKSpacedCentroids(k,df,delta):
    list = []
    for i in np.arange(0.0,1.1,delta):
        for j in np.arange(0,1.1,delta):
            for k in np.arange(0,1.1,delta):
                for l in np.arange(0,1.1,delta):
                    centroid = randomN(df)
                    centroid.head(1).Health_Expenditure = i
                    centroid.head(1).GDP_Per_Capita = j
                    centroid.head(1).Unemployment = k
                    centroid.head(1).Education = l
                    list.append( centroid )
    return list   


def getK(delta):
    k = int(1/delta) + 1
    return k**4



def getSpacedCentoids(ddf):
    centroidsDF = pd.read_csv("clustering-InitialCentroids0.5.csv")
    l = []
    for i in range(len(centroidsDF)):
            df = pd.DataFrame( columns=ddf.columns)
            df = df.append(centroidsDF.iloc[i])
            l.append(df)
    return l

#sort datapoints according to nearest centroid


def getInitialCentroidDatas(k,df,delta):    
    centroidDatas = []
    centroids = getKSpacedCentroids(k,df,delta)
    #centroids = getSpacedCentoids(df)
    for i in range(len(centroids)):
        centroidData = CentroidData()
        centroidData.centoid = centroids[i]
        centroidData.centoid.Country_Name = 'Centroid' + str(i)
        centroidData.nearestDataPoints = pd.DataFrame( columns=df.columns)
        centroidDatas.append(centroidData)
    return centroidDatas


#onlySelectCentroidIfNearsestPointsIsEmpty means that thre needs to be nearest points already selected 
def getClosestCentroid(datapoint,centroidDatas,onlySelectCentroidIfNearsestPointsIsEmpty):
    closestCentroidData = []
    closestDistance = 9999999999.9
    for i in range(len(centroidDatas)):
        #distance = knn.distance(centroidDatas[i].centoid, datapoint)
        distance = utils.GetEuclideanDistanceBetweenFeatureVectors(kfold.getX(centroidDatas[i].centoid),kfold.getX(datapoint) )
        if( distance < closestDistance):
            #this centroid can oly be selected if nearest points exists. This is in the case for selecting centroids for testing data
            if onlySelectCentroidIfNearsestPointsIsEmpty:
                if not centroidDatas[i].nearestDataPoints.empty:
                    closestCentroidData = centroidDatas[i]
                    closestDistance = distance
                else:
                    uu = 0
            #select centroid regardless
            else:
                closestCentroidData = centroidDatas[i]
                closestDistance = distance
    return closestCentroidData



def getMeanPoint(nearestDataPoints,trainingData):
    #create new centroid  
    meanPoint = randomN(trainingData)

    #set values of centroid to mean of each dimension
    meanPoint.head(1).Health_Expenditure = nearestDataPoints['Health_Expenditure'].mean()
    meanPoint.head(1).GDP_Per_Capita = nearestDataPoints['GDP_Per_Capita'].mean()
    meanPoint.head(1).Unemployment = nearestDataPoints['Unemployment'].mean()
    meanPoint.head(1).Education = nearestDataPoints['Education'].mean()
    return meanPoint



def CalculateCentroids(trainingData, k, movingThreshold, centroidDatas):
    for j in range(150):
        #assign training data point to closest centroid
        for i in range(len(trainingData)):
            dataRow = trainingData.iloc[i]
            centroidData = getClosestCentroid( dataRow, centroidDatas, onlySelectCentroidIfNearsestPointsIsEmpty = False)
            centroidData.nearestDataPointsTempList.append(dataRow)
            #centroidData.nearestDataPoints = centroidData.nearestDataPoints.append( dataRow, ignore_index=True,sort=False )

        numberOfCentroidsThatDidNotMove = 0
        for i in range(len(centroidDatas)):
              #removing all nearest points
            centroidDatas[i].nearestDataPoints.dropna()
            centroidDatas[i].nearestDataPoints = pd.DataFrame(centroidDatas[i].nearestDataPointsTempList, columns=trainingData.columns)
            # centroidDatas[i].nearestDataPoints = pd.concat( [centroidDatas[i].nearestDataPoints, centroidDatas[i].nearestDataPointsTempList])
            #clear temp list 
            centroidDatas[i].nearestDataPointsTempList = []
            
            #if no points are assosiated with the centroid then the centroid does not move
            if not centroidDatas[i].nearestDataPoints.empty:
                newCentroid = getMeanPoint(centroidDatas[i].nearestDataPoints,trainingData)
            else:
                newCentroid = centroidDatas[i].centoid
        
        
        
            #calculate mean of data points assigned to the centroid
            #newCentroid = utils.GetMeanPointOfDataset( centroidDatas[i].nearestDataPoints)
            #get the change in position of the centroid
            old = kfold.getX(centroidDatas[i].centoid)
            new = kfold.getX(newCentroid)
            diffrenceInCentroid = old - new 
            distanceBetweenOldAndNewCentroid = utils.GetEuclideanDistanceBetweenFeatureVectors(kfold.getX(centroidDatas[i].centoid),kfold.getX(newCentroid) )
            print( "centroid difference " + str(i) + ' distance= ' + str(distanceBetweenOldAndNewCentroid) )
            print( diffrenceInCentroid )
            #set new mean of data points as the new centroid
            centroidDatas[i].centoid = newCentroid
            if( distanceBetweenOldAndNewCentroid < movingThreshold ):
               numberOfCentroidsThatDidNotMove = numberOfCentroidsThatDidNotMove +1

        #return if none of the centroids have moved
        if( numberOfCentroidsThatDidNotMove >= k):
            print( "no centroids have moved with threshold=" + str(movingThreshold) + " on itteration " + str(j))
            return centroidDatas
    # return if j itterations have been reached
    print("returning after " + str(j) + "itterations")
    return centroidDatas

def RunClustering(testSet, k, movingThreshold, delta):
    centroidResults = CentroidResults()

    centroidDatas = getInitialCentroidDatas(k,testSet.trainingDF, delta)  

    centroidDatas = CalculateCentroids(testSet.trainingDF, k, movingThreshold, centroidDatas)
    
    #associate testing data to centroids
    for i in range(len(testSet.testingDF)):
        dataRow = testSet.testingDF.iloc[i]
        centroidData = getClosestCentroid( dataRow, centroidDatas, onlySelectCentroidIfNearsestPointsIsEmpty = True)
        centroidData.nearestDataPointsTempListForTestingData.append(dataRow)
    
    for i in range(k):
        centroidDatas[i].testingData = pd.DataFrame(centroidDatas[i].nearestDataPointsTempListForTestingData, columns=testSet.testingDF.columns)

        trainingX = kfold.getX(centroidDatas[i].nearestDataPoints).to_numpy()
        trainingY = kfold.getY(centroidDatas[i].nearestDataPoints).to_numpy()
        testingX = kfold.getX(centroidDatas[i].testingData).to_numpy()
        testingY = kfold.getY(centroidDatas[i].testingData).to_numpy()
        
        #training data and testing data has to be available for the OLS regression to run
        results = ols.OLSRun()
        if not centroidDatas[i].nearestDataPoints.empty and not centroidDatas[i].testingData.empty and ols.givesSingularMatrix(trainingX) == False:
            results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

        #store centroid data in results
        centroidResults.centroidData.append(centroidDatas[i])
        #store results of running ols on the test data for that centroid
        centroidResults.olsRuns.append( results )
    return centroidResults


#l = getKCentroids(2)

#a = randomN()

#dist = utils.GetEuclideanDistanceBetweenFeatureVectors( a, x_df.head(1).to_numpy())






#b = 1