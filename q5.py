import math


def nearest_point(X, Y, x, y):
    nearest_x = X[0]
    nearest_y = Y[0]
    min_distance = math.sqrt((X[0] - x) ** 2 + (Y[0] - y) ** 2)

    for i in range(1, len(X)):
        distance = math.sqrt((X[i] - x) ** 2 + (Y[i] - y) ** 2)
        if distance < min_distance:
            min_distance = distance
            nearest_x = X[i]
            nearest_y = Y[i]

    return nearest_x, nearest_y

X = [1.5, 2.6, 3.1]
Y = [0.6, 1.3, 2.7]
x = 1.1
y = -1

print(nearest_point(X, Y, x, y))