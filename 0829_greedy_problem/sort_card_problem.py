n = map(int, input.split())

result = 0

data = list(map(int, input().split()))
sorted(data)

k = 2
a = data[n-1]
b = data[n-k]
result = a+b
k=k+1

while n >= k:
    c = data[n-k]
    result += c
    k=k+1

print(result)