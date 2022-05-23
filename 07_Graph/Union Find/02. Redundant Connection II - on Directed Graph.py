# https://leetcode.com/problems/redundant-connection-ii/


def findRedundantDirectedConnection(edges):
	n, p1, p2, c = len(edges), None, None, None
	p = [0] * (n+1)
	for i, (u,v) in enumerate(edges):
		if p[v]: p1, p2, c, edges[i][0] = p[v], u, v, 0
		else: p[v] = u
	p = list(range(n+1))
	def find(x):
		if p[x] != x: p[x] = find(p[x])
		return p[x]
	for u, v in edges:
		if u:
			pu, pv = find(u), find(v)
			if pu == pv: return p1 and [p1, c] or [u, v]
			else: p[pv] = pu
	return [p2, c]


