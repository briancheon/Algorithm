
import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = (self.x, self.y)

def calculate_orientation(p, q, r):
    val = (q.y - p.y) * (r.x - p.x) - (q.x - p.x) * (r.y - p.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def is_point_on_segment(p, q, r):
    return (min(p.x, r.x) <= q.x <= max(p.x, r.x) and 
            min(p.y, r.y) <= q.y <= max(p.y, r.y))

def intersection(p1, q1, p2, q2):
    A1 = q1.y - p1.y
    B1 = p1.x - q1.x
    C1 = A1 * p1.x + B1 * p1.y

    A2 = q2.y - p2.y
    B2 = p2.x - q2.x
    C2 = A2 * p2.x + B2 * p2.y

    D = A1 * B2 - A2 * B1
    if D == 0:
        return None
    
    x = (B2 * C1 - B1 * C2) / D
    y = (A1 * C2 - A2 * C1) / D

    return (x, y)

def check_intersection(p1, q1, p2, q2):
    seg1 = sorted([p1.xy, q1.xy])
    seg2 = sorted([p2.xy, q2.xy])
    
    start = max(seg1[0], seg2[0])
    end = min(seg1[1], seg2[1])
    
    if start > end:
        return 0

    if start == end:
        return 1
    
    return 3

def do_segments_intersect(p1, q1, p2, q2):
    o1 = calculate_orientation(p1, q1, p2)
    o2 = calculate_orientation(p1, q1, q2)
    o3 = calculate_orientation(p2, q2, p1)
    o4 = calculate_orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        intersection_points = intersection(p1, q1, p2, q2)
        if intersection_points:
            endpoints = {p1.xy, q1.xy, p2.xy, q2.xy}
            if any(abs(intersection_points[0] - x) < 1e-9 and abs(intersection_points[1] - y) < 1e-9 for x, y in endpoints):
                return 1
            return 2
        else:
            return 0

    if o1 == 0 and is_point_on_segment(p1, p2, q1):
        return check_intersection(p1, q1, p2, q2)
    
    if o2 == 0 and is_point_on_segment(p1, q2, q1):
        return check_intersection(p1, q1, p2, q2)
    
    if o3 == 0 and is_point_on_segment(p2, p1, q2):
        return check_intersection(p1, q1, p2, q2)
    
    if o4 == 0 and is_point_on_segment(p2, q1, q2):
        return check_intersection(p1, q1, p2, q2)

    return 0

N = int(sys.stdin.readline().rstrip())
segments = [tuple(Point(x, y) for x, y in zip(*[iter(map(int, sys.stdin.readline().split()))]*2)) for _ in range(N)]

info = [[3] * N for _ in range(N)]

for i in range(N):
	for j in range(i + 1):
		info[i][j] = info[j][i] = do_segments_intersect(segments[i][0], segments[i][1], segments[j][0], segments[j][1])

for row in info:
	print(*row, sep='')