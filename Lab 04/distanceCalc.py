# write a function called findEucliDistance
# that returns Euclidean distance between any two coordinates.
import math
x1 = 312088
y1 = 60271
x2 = 312606
y2 = 59468
def findEucliDistance(x1, y1, x2, y2):
    distance = math.sqrt(
    ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    )
    return distance

distance = findEucliDistance(x1, y1, x2, y2)
print(distance)

def findGreatDistance(lat1, long1, lat2, long2):
    # convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    #calculate the differences between lats and longs
    dlat = lat2 - lat1
    dlong = long2 - long1
    #calculate the great circle distance using haversine formula
    a = math.sin(dlat/ 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    #radius of earth in kilometers
    r = 6373
    distance = c * r
    return distance
