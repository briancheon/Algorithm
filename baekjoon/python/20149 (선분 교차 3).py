import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.xy = (x, y)

def onSegment(p, q, r):
	if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
		return True
	
	return False

def orientation(p, q, r): 
	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
	if val > 0: 
		return 1
	
	elif val < 0: 
		return 2
	
	else: 
		return 0


def intersection(p1, q1, p2, q2):
	if p1.xy > q1.xy:
		p1, q1 = q1, p1

	if p2.xy > q2.xy:
		p2, q2 = q2, p2

	if p1.xy < q2.xy and p2.xy == q1.xy:
		return q1.xy
	
	if p2.xy < q1.xy and q2.xy == p1.xy:
		return p1.xy
	
	return None


def doIntersect(p1, q1, p2, q2): 
	o1 = orientation(p1, q1, p2) 
	o2 = orientation(p1, q1, q2) 
	o3 = orientation(p2, q2, p1) 
	o4 = orientation(p2, q2, q1) 

	if o1 != o2 and o3 != o4: 
		if q1.x - p1.x == 0:
			x = p1.x
			a = (q2.y - p2.y) / (q2.x - p2.x)
			y = a * (x - p2.x) + p2.y

		elif q2.x - p2.x == 0:
			x = p2.x
			a = (q1.y - p1.y) / (q1.x - p1.x)
			y = a * (x - p1.x) + p1.y

		else:
			a1 = (q1.y - p1.y) / (q1.x - p1.x)
			a2 = (q2.y - p2.y) / (q2.x - p2.x)
			b1 = p1.y - a1 * p1.x
			b2 = p2.y - a2 * p2.x
			x = (b2 - b1) / (a1 - a2) 
			y = a1 * x + b1

		return True, (x, y)

	if o1 == 0 and onSegment(p1, p2, q1):
		return True, intersection(p1, q1, p2, q2)
	
	if o2 == 0 and onSegment(p1, q2, q1):
		return True, intersection(p1, q1, p2, q2)
	
	if o3 == 0 and onSegment(p2, p1, q2): 
		return True, intersection(p1, q1, p2, q2)
	
	if o4 == 0 and onSegment(p2, q1, q2): 
		return True, intersection(p1, q1, p2, q2)

	return False, None


L1 = map(int, sys.stdin.readline().split())
L2 = map(int, sys.stdin.readline().split())

x1, y1, x2, y2 = L1
x3, y3, x4, y4 = L2

p1 = Point(x1, y1)
q1 = Point(x2, y2)
p2 = Point(x3, y3)
q2 = Point(x4, y4)

intersect, point_of_intersection = doIntersect(p1, q1, p2, q2)

if intersect:
	print(1)
	if point_of_intersection:
		print(*point_of_intersection)

else:
	print(0)