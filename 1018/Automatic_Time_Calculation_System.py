# oven clock
# Automatic Time Calculation System

h, m = map(int, input().split());
time = int(input());

m += time;

if m < 60:
    print(h, m);
    if h < 23:
        print(h+int(m/60), m-int(60*int(m/60)));
    else:
        print(0, m-int(60*int(m/60)));