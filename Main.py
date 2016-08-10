from math import sqrt

file_name = "src/complex_input.txt"
"""epsilon: all distances must be greater than epsilon to terminate simplification"""
epsilon = 3


"""TODO: multi line support"""
def readFileToCoordinates():
    with open(file_name) as input_file:
        content = input_file.readlines()
        content = [x.strip('\n') for x in content]
    for line in content:
        file_list = line.split(';')
        coordinates = []
        for item in file_list:
            coordinates.append(item.split(','))
        print "Read %s coordinates: %s from file %s" % (str(len(coordinates)), str(coordinates), file_name)
        return coordinates


def distance(p1, p2):
    dx = int(p2[0]) - int(p1[0])
    dy = int(p2[1]) - int(p1[1])
    return sqrt((dx**2)+(dy**2))


def findShortestDistance(coords):
    dmin = 0.0
    index = 0
    for i in range(len(coords)-1):
        if i == 0:
            dmin = distance(coords[i], coords[i+1])
        else:
            d = distance(coords[i], coords[i+1])
            if d < dmin:
                dmin = d
                index = i
    c = distance(coords[-1], coords[0])

    """Sonderfall: Distanz Letzer und Erster"""
    if c < dmin:
        dmin = c
        index = len(coords)
    if dmin > epsilon:
        print "shortest distance exceeded epsilon: terminate"
        return []
    print "Found shortest distance at index %s with distance %s" % (str(index), str(dmin))

    re = [[index, dmin]]
    c = index + 2
    if index == len(coords) - 1:
        c = 0
    preDist = distance(coords[index-1], coords[index])
    posDist = distance(coords[index+1], coords[c])
    if preDist < posDist:
        re.insert(0, [index-1, preDist])
    else:
        re.append([c, posDist])

    return re

def simplify(coords):
    distances = findShortestDistance(coords)
    if len(distances) > 0:
        if len(coords) <= 4:
            """delete complete object as it has only four coordinates and must not be simplified any more"""
            del coords
        index_a = distances[0][0]
        a = coords[index_a]
        index_c = distances[1][0]
        c = coords[index_c]

        dx = int(coords[index_a-1][0]) - int(coords[index_a][0])
        dy = int(coords[index_a-1][1]) - int(coords[index_a][1])

        """Delete Points a, b, c in reverse order to maintain indices positions"""
        del coords[index_c]
        del coords[index_a+1]
        del coords[index_a]

        if dx < dy:
            """Insert new Point (d) with x-coordinate from point a and y-coordinate from point c"""
            d = [a[0], c[1]]
        else:
            """Insert new Point (d) with x-coordinate from point c and y-coordinate from point a"""
            d = [c[0], a[1]]
        coords.insert(index_a, d)
        """End simplification round. Call new round"""
        print u"round: {0:s}".format(coords)
        simplify(coords)
    else:
        print "terminated"
        print coords


if __name__ == "__main__":
    coordinates = readFileToCoordinates()
    simplify(coordinates)