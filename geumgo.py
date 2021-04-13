import sys
input = sys.stdin.readline
W, N = map(int,input().split())

data = []
for _ in range(N):
        data.append(list(map(int,input().split())))

countdata = [0] * 1000001

for i in range(len(data)):
        countdata[data[i][1]] += data[i][0]

i, price = -1, 0

while(W!=0):
        while 1:
                if countdata[i] == 0:
                        i -= 1
                else:
                        break

        if countdata[i] <= W:
                price += (1000001 + i) * countdata[i]
                W -= countdata[i]

        else:
                price += W * (1000001 + i)
                W = 0
        
        i -= 1

print(price)
