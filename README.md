# PolygonSimplification

Simple program to generalize polygons with a round-based algorithm. 

The algorithm calculates the perpendicular distance for each point to a line between its neighboring points. The point with the shortest perpendicular distance will then be removed. This will be repeated until either one of the following termination conditions is met:

-	Number of points in polygon is smaller as or equal to 4
-	A user defined number of repetitions is reached
