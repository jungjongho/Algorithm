import sys

N = int(input())

matrix = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

print(matrix)