import math
points = [(0, 0), (3, 4), (6, 8), (12, 8), (12, 16)]
longest = 0
segment = 0
for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Segment", i + 1, "Distance:", distance)
    if distance > longest:
        longest = distance
        segment = i + 1
print("Longest Route Segment:", segment)
print("Longest Distance:", longest)