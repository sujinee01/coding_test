T = int(input())

A = T // (5 * 60)  
T %= (5 * 60) 

B = T // (1 * 60)  
T %= (1 * 60)      

C = T // 10   
T %= 10         

if T != 0:
    print(-1)  
else:
    print(A, B, C)
