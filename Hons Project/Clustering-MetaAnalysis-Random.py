import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

analysisdf = pd.DataFrame( columns=['dataset','k','Average Mean Error','Average stdDev'])

index = 0
li = []
for dataset in range(1,5):
    fileName = 'Analysis\\Cluster-Analysis-Run' + str(dataset) + '.csv'
    li.append( pd.read_csv(fileName))

df = pd.concat(li, axis=0, ignore_index=True)

df.to_csv('Analysis\\Clustering-MetaAnalysis-Random-Itermediate.csv')


for k in range(1,16):
    #create new dataframe of just this k
    perKDF = df.loc[df['k'] == k]
    index = index + 1
    analysisdf.at[index,'dataset'] = dataset
    analysisdf.at[index,'k'] = perKDF['k'].mean()
    analysisdf.at[index,'Average Mean Error'] = perKDF['Mean'].mean()
    analysisdf.at[index,'Average stdDev'] = perKDF['stdDev'].mean()


analysisdf.to_csv('Analysis\\Clustering-MetaAnalysis-Random.csv')


