N = int(input())
inside = 0
out = 0
while N > 0:
    X = int(input())
    if X >= 10 and X <= 20:
        inside += 1
    else:
        out += 1
    N = N - 1
print(f'{inside} in')
print(f'{out} out')