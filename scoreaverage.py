import sys
input = sys.stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))

datasum = [data[0]]
for i in range(1,N):
        datasum.append(datasum[i-1] + data[i])

for _ in range(K):
        A, B = map(int, input().split())
        if A==1:
                result = datasum[B-1]/B
        else:
                result = (datasum[B-1] - datasum[A-2])/(B-A+1)
        print("{:.2f}".format(round(result,2)))
