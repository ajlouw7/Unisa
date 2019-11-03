import pandas as pd
import numpy as np 

def GetEuclideanDistanceBetweenFeatureVectors( vecA,vecB):
    return np.linalg.norm(vecA-vecB)

def GetMeanPointOfDataset(featureVectors):
    return np.mean(featureVectors, axis=0)

def GetMeanAbsoluteDeviationOfFeatureSet(featureVectors):
    mean = GetMeanPointOfDataset(featureVectors)
    deviationSum = 0
    for vec in featureVectors:
        deviationSum += abs(GetEuclideanDistanceBetweenFeatureVectors(vec,mean))
    return deviationSum/len(featureVectors)