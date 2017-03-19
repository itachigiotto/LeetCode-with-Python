class Solution(object):
	def reverseStr(self, s, k):
		p = []
		for i in range(len(s)):
			p.append(s[i])
		print(p)
		n = len(p)//(2*k)
		print(n)
		left = len(p) - 2*k*n
		print(left)
		for i in range(n):
			print(p[2*i*k:(2*i*k+k)])
			print(p[-1-len(p)+(2*i*k+k):-1-len(p)+2*i*k:-1])
			p[2*i*k:(2*i*k+k)] = p[-1-len(p)+(2*i*k+k):-1-len(p)+2*i*k:-1]
		if left > 0:
			if left < k:
				if 2*n*k != len(p)-1:
					print(p[2*n*k:])
					print(2*n*k-len(p))
					print(p[-1:2*n*k-len(p):-1])
					p[2*n*k:] = p[-1:-1+2*n*k-len(p):-1]
				else:
					p[-1] = p[-1]
			else:
				print(p[2*n*k:(2*n*k+k)])
				print(p[-1-len(p)+(2*n*k+k):-1-len(p)+2*n*k:-1])
				p[2*n*k:(2*n*k+k)] = p[-1-len(p)+(2*n*k+k):-1-len(p)+2*n*k:-1]
		return ''.join(p)

s = input('string is:')
print(s)
k = int(input('k = '))
print(k)
sol = Solution()
rstr = sol.reverseStr(s, k)
print(rstr)