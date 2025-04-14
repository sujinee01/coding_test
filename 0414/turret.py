import math

def main():
    T = int(input())
    EPS = 1e-6  # 부동소수점 오차 허용 범위

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        dx = x1 - x2
        dy = y1 - y2
        dist = math.hypot(dx, dy)

        if abs(dist) < EPS:
            if r1 == r2:
                print(-1)
            else:
                print(0)   # 중심 같고 반지름 다름
        else:
            if abs(dist - (r1 + r2)) < EPS or abs(dist - abs(r1 - r2)) < EPS:
                print(1)  # 외접 or 내접
            elif abs(r1 - r2) < dist < r1 + r2:
                print(2)  # 두 점에서 만남
            else:
                print(0)  # 만나지 않음

if __name__ == "__main__":
    main()
