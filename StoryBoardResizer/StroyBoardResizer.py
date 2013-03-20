'''
Created on 28/02/2013

@author: jgoenetxea
'''
import sys
import re

def scaleLine(criteria, line, scaleValue):
    #dataPattern = re.compile(r"width=\"[\d+]\"")
    findNumbers = re.compile(r"\d+")
    matchTag = criteria.findall(line)
    for l in matchTag: # secuencia entera
        newTag = l
        matchNumbers = findNumbers.findall(l)
        for n in matchNumbers:  # numero dentro de la secuencia
            newValue = str(int(n)/scaleValue)
            newTag = newTag.replace(n, newValue)
        # replace the full secuence
        line = line.replace(l, newTag, 1)
    return line

# Read the attributes
attrSize = len(sys.argv)-1
if (attrSize < 1): 
    print "Error: No se ha especificado fichero alguno. Usage: command storyboardfilename" 
    exit(0)
attrList = sys.argv[1:]

filename = attrList[0]
f = open( filename, "r" )
fileLines = f.readlines()
f.close()

scaleValue = 2

of = open( filename+"_temp", "w" )
findWidth = re.compile(r"width=\"\d+\"")
findHeight = re.compile(r"height=\"\d+\"")
findX = re.compile(r"x=\"\d+\.?\d+\"")
findY = re.compile(r"y=\"\d+\.?\d+\"")
for line in fileLines:
    newLine = line
    newLine = scaleLine(findWidth   , newLine, scaleValue)
    newLine = scaleLine(findHeight  , newLine, scaleValue)
    newLine = scaleLine(findX       , newLine, scaleValue)
    newLine = scaleLine(findY       , newLine, scaleValue)
    of.write(newLine)
    
of.close()
print "End"

