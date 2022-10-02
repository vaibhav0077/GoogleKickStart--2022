
def speed_typing():
    I = input().strip()
    P = input().strip()
    j = 0
    mis = 0
    for i in range(len(P)):
        if j < len(I) and P[i] == I[j]:
            j+=1
        else:
            mis+=1

    if j == len(I):
        return mis
    else:
        return 'IMPOSSIBLE'

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, speed_typing()))