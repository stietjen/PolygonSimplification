from math import sqrt
from os import remove


"""Input and output file paths. The coordinates must be provided in
following format. Example:
x1,y1;x2,y2;x3,y3;x4,y4;..."""
input_file = "src/complex_input.txt"
output_file = "src/output.txt"

"""List of polygons to simplify. Will be filled via input file parsing."""
polygons = []
"""The polygon that is currently being optimized."""
coordinates = []

"""Number of simplification rounds. Each round will delete one point
from the given polygon unless the minimum of four points is reached."""
numberOfRounds = 10


def read_file_to_coordinates():
    """Reads and parses the input file. Each line is treated as individual
    polygon and therefore will be processed individually"""
    with open(input_file) as temp_file:
        content = temp_file.readlines()
        content = [x.strip('\n') for x in content]
    for i in range(len(content)):
        temp_coordinates = []
        split_coordinates = content[i].split(';')
        for coordinate in split_coordinates:
            temp_coordinates.append(coordinate.split(','))
        polygons.append(temp_coordinates)
        print 'Read {0} coordinates: {1} from file {2} line {3}' \
            .format(str(len(temp_coordinates)), str(temp_coordinates), input_file, i + 1)
    temp_file.close()


def write_coordinates_to_file():
    """Writes the currently simplified polygon to the output file.
    The output file will be deleted at the begin of the script.
    The output format is equal to the input format.
    Example: [[1,2],[3,4]] -> 1,2;3,4"""
    output = ""
    for coordinate in coordinates:
        for item in coordinate:
            output += "{0},".format(item)
        output = output[:-1]
        output += ";"
    output = output[:-1]

    temp_file = open(output_file, 'a')
    temp_file.write(output + "\n")
    temp_file.close()


def clean_old_output_file():
    """Deletes the output file if it already exists."""
    try:
        remove(output_file)
    except OSError:
        # File does not exist. Do nothing
        pass


def perpendicular_distance(point, start, stop):
    """Calculates the perpendicular distance. (Distance from a point to a line between two other points)

    PARAMETERS
    ==========
        point >> The distant point (must be (x,y) tuple)
        start, stop >> These two points define the line (both must be (x,y) tuples)
    """
    x1, y1 = map(int, start)
    x2, y2 = map(int, stop)
    px, py = map(int, point)
    # In case of the x-coordinates from the start and the stop point being the same
    if x1 == x2:
        return abs(x1 - px)
    m = float(y2 - y1)/float(x2 - x1)
    b = y1 - m * x1
    return abs(m * px - py + b)/sqrt(m * m + 1)


def simplification():
    """Simplification loop. Repeats as often as the global variable 'numberOfRounds' but
    stops if the polygon has only four points left."""
    for i in range(numberOfRounds):
        # In case of the polygon having only four points no further simplification is done.
        if len(coordinates) <= 4:
            print "Reached maximal optimization. Exit."
            return
        print "Start round %s: %s" % (i + 1, coordinates)
        simplification_round()
        print "End round   %s: %s" % (i + 1, coordinates)


def simplification_round():
    """One round of simplification of the currently processed polygon.
    The point with the shortest perpendicular distance will be removed
    as this means the shape of the polygon will be altered the least."""
    coordinates.extend(coordinates[0:2])
    min_dist = None
    index = 0
    for i in range(len(coordinates)-3):
        temp_dist = perpendicular_distance(coordinates[i + 1], coordinates[i], coordinates[i + 2])
        if temp_dist < min_dist or min_dist is None:
            min_dist = temp_dist
            index = i+1
    del coordinates[index]
    del coordinates[-2:]
    print "Removed index %s" % index


if __name__ == "__main__":
    read_file_to_coordinates()
    clean_old_output_file()
    for polygon in polygons:
        if len(polygon) <= 4:
            print "The amount of points is already reduced to a minimum of four. Further reduction is not necessary."
        else:
            print "\n\n\n"
            coordinates = polygon
            simplification()
            write_coordinates_to_file()
