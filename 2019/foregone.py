T = int(input().strip())

def processed(N:int)->tuple:
    """
    At least one 4 is there in N.
    1 < N < 10^100
    """
    l1= str(N)
    a,b = '',''
    for i in range(len(l1)):
        if l1[i] == '4':
            a+='2'
            b+='2'
        else:
            a+=str(l1[i])
            b+='0'
    return int(a), int(b)

for count in range(T):
    N = int(input().strip())
    a,b = processed(N)
    print("Case #{}: {} {}".format(count+1, a, b))
