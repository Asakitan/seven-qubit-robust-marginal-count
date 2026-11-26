# A positive stability radius for the seven-qubit extremal marginal count

**Byline:** Chain.Ren · Independent research  
**Version:** [proof-v1.0.1](https://github.com/Asakitan/seven-qubit-robust-marginal-count/releases/tag/proof-v1.0.1) · 2026-11-27 (Australia/Sydney). OpenAI Codex contributed to the derivation, exposition and verification.

For a pure seven-qubit state $|\psi\rangle$, let $\rho_A$ be the reduction to a subset $A$ and $D_A=2^{|A|}\operatorname{Tr}\rho_A^2-1$. A triple is $\varepsilon$-good when $D_A\le\varepsilon$. **Theorem.** For every $0\le\varepsilon\le1/2500$, the maximum possible number of good triples is exactly **32 of 35**. This supplies an explicit, not necessarily optimal, positive radius for the seven-qubit case of [Zhang, Han and Zhang's robust extremal problem](https://arxiv.org/html/2608.13907v1).

The underlying zero-error Pauli parity contradiction is due to [Huber, Gühne and Siewert](https://arxiv.org/abs/1608.06228). Below we keep all low-weight error terms and estimate the resulting approximate anticommutator. All norms without subscripts are operator norms, except that the norm of a vector is Euclidean. When a subsystem operator acts on $|\psi\rangle$ we implicitly extend it by identities.

## 1. Extract a five-site window

Suppose there are at most two bad triples. We need a five-site set $F$ for which all triples in $F$ and all triples $F^c\cup\{j\}$ for $j\in F$ are good. A bad triple spoils six choices of $F$ containing it, and three choices whose complementary pair lies in it. These choices are disjoint, so two bad triples spoil at most 18 of the 21 five-sets. Fix an unspoiled $F$. The pair $F^c$ is good as well: $D_A=\sum_{P\ne I:\operatorname{supp}(P)\subseteq A}\langle P\rangle_\psi^2$ by Pauli orthogonality, hence defects are nondecreasing under inclusion. Set $t=\sqrt\varepsilon\le1/50$.

## 2. Approximate projector relations and Pauli weights

Write $D=32\rho_F=I+\sum_{\ell=1}^5 P_\ell$; $P_\ell$ is the sum of the weight-$\ell$ Hermitian Pauli strings on $F$ with coefficients $\langle P\rangle_\psi$. The scalar defect $D_A$ and the operator $D$ are distinct. Set $X=P_2+P_4$ and $Y=P_1+P_3+P_5$, so $D=I+X+Y$.

If a complementary subsystem of dimension $d$ has defect at most $t^2$, its reduced operator differs from $I/d$ by Hilbert–Schmidt norm at most $t/\sqrt d$. Thus every nonzero Schmidt weight (eigenvalue of the density matrix) lies within $t/\sqrt d$ of $1/d$. The Schmidt decomposition across $F|F^c$ now gives
$$
\|(D-8I)\psi\|\le16t,\qquad
\|D^2-8D\|\le(8+16t)16t\le144t.
$$
The second bound holds also on the nullspace, where its left side is zero. Likewise each $C_j=16\rho_{F\setminus\{j\}}$, extended by the identity on $j$, satisfies $\|(C_j-2I)\psi\|\le16t/\sqrt8\le6t$ by goodness of $F^c\cup\{j\}$.

Each Pauli term of weight $\ell$ in $F$ appears in exactly $5-\ell$ of the $C_j$. Consequently
$$
X-5I=\sum_{j\in F}(C_j-2I)-E,\qquad E=4P_1+2P_2+2P_3.
$$
If $w_\ell$ denotes the sum of the squared Pauli coefficients of weight $\ell$ inside $F$, the sum of the ten triple defects there is $6w_1+3w_2+w_3\le10t^2$. Thus
$$
\|E\|^2\le\operatorname{Tr}_F E^2=32(16w_1+4w_2+4w_3)\le1280t^2.
$$
Altogether,
$$
\|(X-5I)\psi\|\le66t,\qquad
\|(Y-2I)\psi\|\le82t ,
$$
the latter by $Y-2I=(D-8I)-(X-5I)$.

## 3. The robust parity contradiction

Let $\Theta$ be conjugation by the five-site spin-flip antiunitary $\sigma_y^{\otimes5}K$ ($K$ is computational-basis complex conjugation). It acts by $(-1)^\ell$ on a weight-$\ell$ Hermitian Pauli string, and preserves products and operator norms. The odd part $(Z-\Theta Z)/2$ of any Hermitian operator has norm at most $\|Z\|$. Applied to $D^2-8D$, the odd part is exactly $\{X,Y\}-6Y$, where $\{X,Y\}=XY+YX$. In particular $\|\{X,Y\}-6Y\|\le144t$.

Put $U=X-5I$, $V=Y-2I$. On taking expectation in $|\psi\rangle$,
$$
\langle\{X,Y\}-6Y\rangle
=8+4\langle U+V\rangle+2\operatorname{Re}\langle U\psi,V\psi\rangle .
$$
But $\langle U+V\rangle=\langle D-8I\rangle=32\operatorname{Tr}\rho_F^2-8=8D_{F^c}\ge0$. Combining this favorable sign, Cauchy–Schwarz and the preceding norm bounds forces
$$
8\ \le\ 144t+2(66)(82)t^2
\ \le\ 144/50+10824/2500<8 .
$$
So at least three triples are bad.

## 4. Attainment

The exact ceiling 32 and states attaining it were known before the robust question. For a stand-alone example, use the graph state on seven vertices with edges
$$
13,\ 15,\ 16,\ 17,\ 23,\ 24,\ 26,\ 34,\ 37,\ 45,\ 56,\ 67
$$
(1-based labels). Its stabilizer generators are $K_i=X_i\prod_{j\sim i}Z_j$. For binary $a$ the product of generators specified by $a$ has support $\operatorname{supp}(a)\cup\operatorname{supp}(\Gamma a)$, where $\Gamma$ is the adjacency matrix over $\mathbb F_2$. The state projector is the normalized sum of stabilizers, so its Pauli coefficients have absolute value one on these strings and zero elsewhere. Enumerating the 127 nonidentity products gives exactly one supported on each of the triples $\{1,5,7\}$, $\{2,3,7\}$, $\{4,6,7\}$, and none supported on any other triple. The other 32 have defect zero. This meets the upper bound throughout the stated interval. ∎

[verify.py](verify.py) exhausts these stabilizers, checks the combinatorial window choice for every pair of bad triples, and checks the final rational error budget.
