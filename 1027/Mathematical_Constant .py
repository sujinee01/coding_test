# 두 숫자를 입력받습니다.
A, B = input().split()

# 각 숫자를 뒤집고 정수로 변환합니다.
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])

# 두 숫자 중 큰 값을 출력합니다.
print(max(reversed_A, reversed_B))
