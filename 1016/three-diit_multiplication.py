# three-digit multiplication
x = int(input())
y = int(input())

a = int(x*(y%10))
b = int(x*(int(y/10)%10))
c = int(x*int(y/100))

print(a)
print(b)
print(c)
print(a+b*10+c*100)