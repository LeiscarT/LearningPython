import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)


minOfAxisOne = numpy.amin(sampleArray, 1) 
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = numpy.amax(sampleArray, 0) 
print("Printing amax Of Axis 0")
print(maxOfAxisOne)