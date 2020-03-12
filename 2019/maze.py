T = int(input())

def processStr(S):
    ans = ''
    for s in S:
        ans += 'S' if s == 'E' else 'E'
    return ans
    
for i in range(T):
    N = int(input())
    S = input().strip()
    print("Case #{}: {}".format(i+1, processStr(S)))
