"""Exact checks of the seven-qubit graph state, incidence counts and error budget."""
from fractions import Fraction as F
from itertools import combinations

def masks(n,r):
    return [sum(1<<i for i in subset) for subset in combinations(range(n),r)]

def check():
    triples=masks(7,3); five=masks(7,5)
    allsites=127
    spoils=lambda t,s: (t&s)==t or (t&(allsites^s))==(allsites^s)
    assert all(sum(spoils(t,s) for s in five)==9 for t in triples)
    min_usable=min(sum(not spoils(t,s) and not spoils(u,s) for s in five)
                   for t,u in combinations(triples,2))
    assert min_usable>=3

    edges=[(0,2),(0,4),(0,5),(0,6),(1,2),(1,3),(1,5),(2,3),(2,6),
           (3,4),(4,5),(5,6)]
    adj=[0]*7
    for i,j in edges:
        adj[i]|=1<<j; adj[j]|=1<<i
    defects={t:0 for t in triples}
    for a in range(1,128):
        z=0
        for i in range(7):
            if (a>>i)&1:
                z ^= adj[i]
        support=a|z
        for t in triples:
            defects[t] += ((support&t)==support)
    bad={tuple(i+1 for i in range(7) if (t>>i)&1):v
         for t,v in defects.items() if v}
    assert bad=={(1,5,7):1,(2,3,7):1,(4,6,7):1}
    t=F(1,50)
    assert all(x<=4*y for x,y in zip((16,4,4),(6,3,1)))
    assert 8*6**2>=16**2 and 36**2>=1280
    budget=144*t+2*66*82*t*t
    assert budget<8
    print(f"32 exact triples; excluded defects = {bad}; "
          f"minimum usable five-sets = {min_usable}; budget {budget} < 8.")

if __name__=='__main__':
    check()
