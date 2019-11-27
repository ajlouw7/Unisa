import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv

k=9
i=5


results = kNN.kNNRunDataset(k,kfold.testSet(i))
fileName = 'kNN_Results' + str(i) + 'k=' + str(k) + '.csv'
with open(fileName,mode='w', newline='') as resultsFile:
    resultsWriter = csv.writer( resultsFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    resultsWriter.writerow(['LE','Predicted LE', 'Error','Health_Expenditure','GDP_Per_Capita','Education','Unemployment'])
    for r in results.results:   
        resultsWriter.writerow([float(r.lifeExpectancy), float(r.predictedLifeExpectancy), float(r.error), r.inputFeatureVector.Health_Expenditure, r.inputFeatureVector.GDP_Per_Capita,r.inputFeatureVector.Education,r.inputFeatureVector.Unemployment])

i =1