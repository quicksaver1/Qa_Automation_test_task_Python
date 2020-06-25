import sys

def parseConfigLine(nextLine):
    equalityIndex=nextLine.find('=')
    if equalityIndex <0:
        raise Exception(f"Config File Error: equality sign is missing at line {lineCounter!r}")
    if nextLine.find('=',equalityIndex+1) >=0:
        raise Exception(f"Config File Error: there are more than one equality signs at line {lineCounter!r}")
    leftValue=nextLine[:equalityIndex].strip()
    rightValue=nextLine[equalityIndex+1:].strip()
    if len(leftValue)==0 or len(rightValue)==0:
        raise Exception(f"Config File Error: empty value at line {lineCounter!r}")
    valuesTable[leftValue]=rightValue
    
argsLength=len(sys.argv)
#print(sys.argv)
if not argsLength == 3:
    raise Exception(f"Wrong amount of arguments: {argsLength-1!r} instead of 2")

configFile = open(sys.argv[1],'r')
textFile = open(sys.argv[2],'r')
valuesTable={}
lineCounter=1
for line in configFile:
    parseConfigLine(line)
    lineCounter+=1;
configFile.close()
textLines=[]
for line in textFile:
    textLines.insert(0,line)
textFile.close()
print(valuesTable)#Debug
for line in textLines:
    for key in valuesTable:  
        line=line.replace(key,valuesTable[key])
    print(line)

