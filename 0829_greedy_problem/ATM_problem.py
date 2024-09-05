n = int(input())

data = list(map(int, input().split()))
data.sort()

time = 0
sum = 0

for p in data:
    time += p
    sum += time

print(sum)