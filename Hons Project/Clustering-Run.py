import pandas as pd
import kfold as kfold
import kMeansClustering as cluster
import csv


#i=1
#k=5
movingThreshold= 0.0001 #0.001
index = 0


analysisdf = pd.DataFrame( columns=['Series','k','centroidNum','Mean','stdDev','count'])





#for each fold
for i in range(1,11): #11   6,11
    #for each number of clusters
    for k in range(1296,1297): #2,16  1296,1297
        results = cluster.RunClustering(kfold.testSet(i,1), k, movingThreshold )
        #for each centroid    
        fileName = 'Cluster-Results\Cluster_Results' + str(i) + '#ofclusters=' + str(k) + ' theshold= ' + str(movingThreshold) + '.csv'
        with open(fileName,mode='w', newline='') as resultsFile:
            resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment','centroid#','centroid_Health_Expenditure','centroid_GDP_Per_Capita','centroid_Education','centroid_Unemployment'])
            for centroidIndex in range(k):
                he = results.centroidData[centroidIndex].centoid.at[0,'Health_Expenditure']
                gdp = results.centroidData[centroidIndex].centoid.at[0,'GDP_Per_Capita']
                edu = results.centroidData[centroidIndex].centoid.at[0,'Education']
                unem = results.centroidData[centroidIndex].centoid.at[0,'Unemployment']
                for r in results.olsRuns[centroidIndex].results:   
                    resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector[0], r.inputFeatureVector[1],r.inputFeatureVector[2],r.inputFeatureVector[3], str(centroidIndex + 1),float(he),float(gdp),float(edu),float(unem)])
        df = pd.read_csv(fileName)
        for centroidNum in range(1,k+1):
            index =  index +1
            analysisdf.at[index,'Series'] = i
            analysisdf.at[index,'k'] = k 
            analysisdf.at[index,'centroidNum'] = centroidNum
            filtereddf = df.where( df['centroid#'] == centroidNum )
            analysisdf.at[index,'Mean'] = filtereddf['Error'].mean()
            analysisdf.at[index,'stdDev'] = filtereddf['Error'].std()
            analysisdf.at[index,'count'] = filtereddf['Error'].count()
    analysisdf.to_csv('Analysis\Cluster-Analysis-Even-Fold-Dataset' + str(i) + 'theshold' + str(movingThreshold) +'-Run.csv')
    analysisdf.dropna()
l = 0

