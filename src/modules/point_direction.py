import math

def get_point_direction(origin, destination):
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    magnitude = math.sqrt((x_dist ** 2) + (y_dist ** 2))
    vector_normalize = ((x_dist / magnitude), (y_dist / magnitude))
    return vector_normalize

def get_point_radius(origin, destination, radius = 0.5):
    pos = get_point_direction(origin, destination)
    pos = get_point_direction(origin, destination)
        #print(self.rect.centerx + 2 * math.sin(math.degrees(pos[0])))
    x = origin[0] + radius * math.degrees(pos[0])
    y = origin[1] + radius * math.degrees(pos[1])
    return (x, y)


def get_angle(origin, destination):
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    magnitude = math.atan2((x_dist),(y_dist))
    return math.degrees(magnitude)
