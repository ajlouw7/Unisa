import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns




df = pd.read_csv('Analysis\\Clustering-MetaAnalysis-Random.csv')

k=10

#for k in range(1,11):

#seriesData = df.loc[df['Series'] == k]
seriesData = df

seriesData = seriesData.rename(columns={"k": "# of clusters"})

fileName = "Cluster-Plot\clusteringRandomPlot.png"

#fileName = "kNNErrorPlot\kNNErrorPlot.png"

sns.lineplot( x='# of clusters', y='Average Mean Error',ci="sd", data=seriesData).get_figure().savefig(fileName)

l=0
