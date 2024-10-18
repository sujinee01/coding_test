# oven clock
# Automatic Time Calculation System

h, m = map(int, input().split());
time = int(input());

m += time;

if m < 60:
    print(h, m);
else:
    print(h+int(m/60)-(int((h+int(m/60))/24)*24), m-int(60*int(m/60)));