# Mathematical_Constant
A, B = input().split()

# 각 숫자를 뒤집고 정수로 변환
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])

print(max(reversed_A, reversed_B))
