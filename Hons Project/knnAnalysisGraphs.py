import math
import pandas as pd
import Utils as utils
import kNN as kNN
import kfold as kfold
import csv
import seaborn as sns

df = pd.read_csv('Analysis\\kNN-Analysis.csv')

k=2
#for k in range(1,11):
seriesData = df.loc[df['Series'] == k]

fileName = "kNNErrorPlot\kNNErrorPlot" + str(k) + ".png"
sns.lineplot( x='k', y='Mean', data=seriesData).get_figure().savefig(fileName)

l=0
