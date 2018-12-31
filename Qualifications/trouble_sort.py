T = int(input())

for i in range(T):
	s1 = int(input().rstrip())
	s2 = input().rstrip().split(' ')
	l1, l2 = [], []
	for j in range(s1):
		if j%2 == 0: l1.append(int(s2[j]))
		# s2's even indexed are in l1 Ex: 0 , 2, 4 ...
		else: l2.append(int(s2[j]))
		# and odd ones are in l2: Ex: 1, 3, 5 ...
	l1 , l2, bool = sorted(l1), sorted(l2), 0
	for k in range(s1):
		try:
			if l1[k] > l2[k]:
				print('Case #{}: {}'.format(i+1,2*k))
				bool = 1
				break
			if l2[k] > l1[k+1]:
				print('Case #{}: {}'.format(i+1,2*k+1))
				bool = 1
				break
		except: break

	if not bool: print('Case #{}: {}'.format(i+1,'OK'))
