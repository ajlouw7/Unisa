import pandas as pd
import numpy as np 
import Utils as utils
import OLS as ols
import kfold as kfold

trainingData = kfold.create_df1()
testingData = kfold.create_df10()

trainingX = kfold.getX( trainingData ).to_numpy()
trainingY = kfold.getY( trainingData ).to_numpy()
testingX = kfold.getX( testingData ).to_numpy()
testingY = kfold.getY( testingData ).to_numpy()





results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

i = 0

