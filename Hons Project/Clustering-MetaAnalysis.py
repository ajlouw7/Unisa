import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

analysisdf = pd.DataFrame( columns=['dataset','k','Average Mean Error','Average stdDev'])

index = 0

for dataset in range(1,6):
    fileName = 'Analysis\\Cluster-Analysis-Even-Fold' + str(dataset) + '-Run.csv'
    df = pd.read_csv(fileName)
    index = index + 1
    analysisdf.at[index,'dataset'] = dataset
    analysisdf.at[index,'k'] = df['k'].mean()
    analysisdf.at[index,'Average Mean Error'] = df['Mean'].mean()
    analysisdf.at[index,'Average stdDev'] = df['stdDev'].mean()


analysisdf.to_csv('Analysis\\Clustering-MetaAnalysis.csv')


