import sys

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, sys.stdin.readline().split())

distance = float('inf')

while True:
    mx, my, mz = (Ax + Bx) / 2, (Ay + By) / 2, (Az + Bz) / 2
    l = ((Ax - Cx) ** 2 + (Ay - Cy) ** 2 + (Az - Cz) ** 2) ** 0.5
    m = ((mx - Cx) ** 2 + (my - Cy) ** 2 + (mz - Cz) ** 2) ** 0.5
    r = ((Bx - Cx) ** 2 + (By - Cy) ** 2 + (Bz - Cz) ** 2) ** 0.5
    
    if abs(distance - m) < 1e-11:
        print(f'{distance:.10f}')
        break
    if m < distance:
        distance = m
    
    if l > r:
        Ax, Ay, Az = mx, my, mz
    else:
        Bx, By, Bz = mx, my, mz