''' As after different checks; we lastly get our target code and the capacity of the robot. Now we know that since there is a combination that would protect the defense system in the minumum swaps; and since last 'S' were the highest weighing swaps; thus we started from last.
'''
v = int(input())

def power(rcode):
	shoot, cap_incr = 0, 1
	for i in rcode:
		if i == 'S': shoot += cap_incr
		elif i == 'C': cap_incr *= 2
	return shoot

#reverse = lambda strr: ''.join([strr[-i] for i in range(1,len(strr)+1)])

def swap(strr):
	strr = ''.join(reversed(strr))
	if 'SC' in strr:
		tup = strr.partition('SC')
		return ''.join(reversed(''.join([tup[0], 'CS', tup[2]])))
			


for i in range(v):
	s = input().rstrip().split(" ")
	cap, code = int(s[0]), s[1]
	v1= code.count('S')
	if v1 > cap:
		print('Case #{}: IMPOSSIBLE'.format(i+1))
		continue
	times = 0
	while power(code) > cap:
		code = swap(code) 
		times += 1
	print('Case #{}: {}'.format(i+1,times))
	
# cheat.py:- 
'''
T = int(input())
for case in range(1, T+1):
    D, P = input().split()
    D = int(D)
    damages = list()
    charge = 1
    for x in P:
        if x == "C":
            charge *= 2
        elif x == "S":
            damages.append(charge)

    hacks = 0
    while sum(damages) > D and max(damages) > 1:
        d = damages[-1]
        #print(d, damages,' d, dama')
        damages[-1] = d//2
        #print(damages,'dama')
        damages.sort()
        #print(type(damages))
        hacks += 1

    solution = hacks if sum(damages) <= D else "IMPOSSIBLE"
    print("Case #{}: {}".format(case, solution))
'''
