from math import sqrt

file_name = "src/complex_input.txt"


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


def simplify(coords):
    dmin = 0.0
    index = 0
    """Use magic power here -> Methode schreiben"""
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


if __name__ == "__main__":
    coordinates = readFileToCoordinates()
    simplify(coordinates)