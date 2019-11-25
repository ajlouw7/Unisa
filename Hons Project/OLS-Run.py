import pandas as pd
import numpy as np 
import Utils as utils
import OLS as ols
import kfold as kfold




ts = kfold.testSet(1)

trainingX = kfold.getX(ts.trainingDF).to_numpy()
trainingY = kfold.getY(ts.trainingDF).to_numpy()
testingX = kfold.getX(ts.testingDF).to_numpy()
testingY = kfold.getY(ts.testingDF).to_numpy()


results = ols.RunDataset( trainingY, trainingX, testingY, testingX)

i = 0

