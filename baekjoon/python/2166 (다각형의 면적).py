# 다각형의 면적
import sys

N = int(sys.stdin.readline().rstrip())
x_plot, y_plot = [], []

for c in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_plot.append(x)
    y_plot.append(y)

x_plot.append(x_plot[0])
y_plot.append(y_plot[0])

A = 0
for c in range(N):
    A += x_plot[c] * y_plot[c + 1] - y_plot[c] * x_plot[c + 1]

print(round(abs(A) / 2, 1))
