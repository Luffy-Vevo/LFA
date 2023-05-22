V = [{} for i in range(5000)]
M = int(input())
for i in range(M):
    a, s, b = input().split()
    a = int(a); b = int(b)
    V[a][s] = b
T = map(int, input().split())
N = int(input())
S = ''
def F(v, d = 0):
    if d == N:
        if v in T:
            print(S)
    for s in V[v]:
        S += s; F(V[v][s], d + 1); S = S[:-1]