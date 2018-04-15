import math

class AttributeValue:
    name = ""
    p = 0
    n = 0


def Entropy(num,denom):
    if( num == 0):
        return 0
    return -num/denom*math.log2(num/denom)

def CalcI(p,n):
    p=int(p)
    n=int(n)
    return  Entropy(p,p+n) + Entropy(n,n+p)


numberOValuesOfAttribute = input("Number of values of attribute")

totalp = input("Get total number of p\n")
totaln = input("Get total number of n\n")

attributeValues = []
for i in range(0, int(numberOValuesOfAttribute) ):
    question = "Attribute value " + str(i+1) + ": "
    name = input(question)
    av = AttributeValue()
    av.name = name
    attributeValues.append( av )

for i in range(0, int(numberOValuesOfAttribute) ):
    av = attributeValues[i]
    print("For " + av.name)
    av.p = input("Value of p\n")
    av.n = input("Value of n\n")

IofPN = CalcI(totalp,totaln)

totalCount = int(totalp) + int(totaln)
E = 0

for av in attributeValues:
    E= E + (int(av.p)+int(av.n))/totalCount*CalcI(int(av.p),int(av.n))

gain = IofPN - E
print("I = " + str(IofPN))
print("E = " + str(E))
print("gain = " + str(gain))