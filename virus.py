K, P, N = map(int, input().split())

result = K

for _ in range(N):
        result = (result * P) % 1000000007

print(result)
