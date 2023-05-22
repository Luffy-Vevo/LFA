V = [{} for i in range(5000)]
M = int(input('Nr. sageti = '))
for i in range(M):
    a, s, b = input().split()
    a = int(a[1:]); b = int(b[1:])
    V[a][s] = b
T = [int(t[1:]) for t in input().split()]
S = input('S = ')
Q = 0
P = ['q0']
for c in S:
    if c in V[Q]:
        Q = V[Q][c]
    P.append(f'q{Q}')
if Q in T:
    print('Acceptat!', ', '.join(P))
else:
    print('Neacceptat!')
