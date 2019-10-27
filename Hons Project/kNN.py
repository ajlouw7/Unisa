import math

class Result:
    distance = 0.0
    lifeExpectancy = 0.0

def distance(p1,p2):
    squareDistance = 0
    squareDistance += math.pow(p1.Health_Expenditure - p2.Health_Expenditure,2)
    squareDistance += math.pow(p1.GDP_Per_Capita - p2.GDP_Per_Capita,2)
    squareDistance += math.pow(p1.Primary_School_Enrollment - p2.Primary_School_Enrollment,2)
    squareDistance += math.pow(p1.Secondary_School_Enrollment - p2.Secondary_School_Enrollment,2)
    squareDistance += math.pow(p1.Tertiary_School_Enrollment - p2.Tertiary_School_Enrollment,2)
    squareDistance += math.pow(p1.Unemployment - p2.Unemployment,2)
    
    return math.sqrt(squareDistance)



def getKNN(df, target, k):
    results = list()
    for p2 in df.itertuples():
        r = Result()
        r.distance = distance(target,p2 )
        r.lifeExpectancy = p2.Life_Expectancy
        results.append(r)  
    results.sort(key=lambda x:x.distance)
    return results[0:k]

def avgOfKNN(df,target,k):
    results = getKNN(df,target,k)
    sumLifeExpectancy = 0.0
    for r in results:
        sumLifeExpectancy+=r.lifeExpectancy
    return sumLifeExpectancy/k
