from math import sqrt

fileName = "src/complex_input.txt"

coordinates = []

numberOfRounds = 10

#TODO: multi line support

#change Fileinput to Coordinates
def readFileToCoordinates():
    with open(fileName) as input_file:
        content = input_file.readlines()
        content = [x.strip('\n') for x in content]
    for line in content:
        file_list = line.split(';')
        for item in file_list:
            coordinates.append(item.split(','))
        print "Read %s coordinates: %s from file %s" % (str(len(coordinates)), str(coordinates), fileName)


def writeCoordinatesToFile():
    output = ""
    for coordinate in coordinates:
        for item in coordinate:
            output += item + ","
        output = output[:-1]
        output += ";"
    output = output[:-1]

    file = open('src/output.txt', 'w')
    file.write(output)
    file.close()

#Define perpendicular distance from point to line
def perpendicularDistance(point, start, stop):
    x1, y1 = start
    x2, y2 = stop
    px, py = point
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    px = int(px)
    py = int(py)
    #To avoid having start and stop point as one
    if x1 == x2:
        return abs(x1-px)
    m = float(y2 - y1)/float(x2 - x1)
    b = y1 - m * x1
    return abs(m * px - py + b)/sqrt(m * m + 1)

def simplification():
    for i in range(numberOfRounds):
        if len(coordinates) <= 4:
            print "Reached maximal optimization. Exit."
            return
        print "Start round %s: %s" %(i+1, coordinates)
        simplificationRound()
        print "End round   %s: %s" %(i+1, coordinates)

def simplificationRound():
    coordinates.extend(coordinates[0:2])
    minDist = None
    index = 0
    for i in range(len(coordinates)-3):
        tempDist = perpendicularDistance(coordinates[i+1], coordinates[i], coordinates[i+2])
        if tempDist < minDist or minDist is None:
            minDist = tempDist
            index = i+1
    del coordinates[index]
    del coordinates[-2:]
    print "Removed index %s" % index


if __name__ == "__main__":
    readFileToCoordinates()
    if len(coordinates) <= 4:
        print "The amount of points is already reduced to a minimum of four. Further reduction would be unnecessary."
    else:
        simplification()
        writeCoordinatesToFile()