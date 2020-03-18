#Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230.

import ephem

jupiter  = ephem.Jupiter()
jupiter.compute('1230/1/1')
dist_au = jupiter.sun_distance
dist_km = dist_au * 149597870.691
print(dist_km)