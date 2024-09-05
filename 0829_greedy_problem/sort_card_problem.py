import heapq

N = int(input())
cards = []


for _ in range(N):
    heapq.heappush(cards, int(input()))


result = 0


while len(cards) > 1:

    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

 
    sum_value = first + second
    result += sum_value


    heapq.heappush(cards, sum_value)

print(result)