import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv

index = 0


analysisdf = pd.DataFrame( columns=['Series','k','Mean','stdDev'])

for dataset in range(2,11):
    for k in range(1,107): 
        for i in range(1,11):
            #results = kNN.kNNRunDataset(k,kfold.testSet(i))
            results = kNN.weightedkNNRunDataset(k,kfold.testSet(i, dataset))
            fileName = 'kNN-Results-Weighted\\kNN-Results-Weighted-Run' + str(dataset) + '\\kNN_Results-Weighted' + str(i) + 'k=' + str(k) + '.csv'
            with open(fileName,mode='w', newline='') as resultsFile:
                resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment'])
                for r in results.results:   
                    resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector.Health_Expenditure, r.inputFeatureVector.GDP_Per_Capita,r.inputFeatureVector.Education,r.inputFeatureVector.Unemployment])
            df = pd.read_csv(fileName)
            index =  index +1
            analysisdf.at[index,'Series'] = i
            analysisdf.at[index,'k'] = k 
            analysisdf.at[index,'Mean'] = df['Error'].mean()
            analysisdf.at[index,'stdDev'] = df['Error'].std()


    analysisdf.to_csv('Analysis\\kNN-Analysis-Weighted-Run' + str(dataset) + '.csv')