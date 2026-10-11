**Keywords:** long-range percolation; critical probability; lace
expansion; nonbacktracking paths; small-exponent asymptotics.

# Model and result

For $`0<\sigma<1`$ and $`0\le C\le1`$, declare each unordered pair
$`\{x,y\}`$ of distinct integers open independently with probability
$`C|x-y|^{-1-\sigma}`$. Let $`C_c(\sigma)`$ be the infimum of the
parameters for which the origin belongs to an infinite open cluster with
positive probability. At $`C=1`$ all nearest-neighbor bonds are open, so
this infimum is taken over a nonempty set. Put
``` math
\begin{equation}
\label{eq:kernel}
 Z_\sigma=\zeta(1+\sigma),\qquad
 D_\sigma(0)=0,\qquad
 D_\sigma(x)=\frac{|x|^{-1-\sigma}}{2Z_\sigma}\quad(x\ne0).
\end{equation}
```
Thus $`D_\sigma`$ is an even probability distribution. The normalized
parameter $`p=2Z_\sigma C`$ is the expected degree, and the bond
probabilities become $`pD_\sigma(y-x)`$. Its admissible interval is
$`[0,\|D_\sigma\|_\infty^{-1}]=[0,2Z_\sigma]`$. We write
$`p_c(\sigma)=2Z_\sigma C_c(\sigma)`$.

<div id="thm:main" class="theorem">

**Theorem 1**. *There are constants $`K<\infty`$ and $`\sigma_0>0`$ such
that, for every real $`0<\sigma<\sigma_0`$, the model defined above
satisfies
``` math
\begin{equation}
\label{eq:main}
 \left|p_c(\sigma)-1-S_2(\sigma)\right|\le K\sigma^3,
 \qquad
 S_2(\sigma)=\frac{\zeta(2+2\sigma)}{2\zeta(1+\sigma)^2}.
\end{equation}
```
In particular,
``` math
\begin{equation}
\label{eq:limit}
 \lim_{\sigma\downarrow0}
 \frac{2\zeta(1+\sigma)C_c(\sigma)-1}{\sigma^2}
 =\frac{\pi^2}{12}.
\end{equation}
```*

</div>

In the original bond-amplitude parameter the same result reads
``` math
\begin{equation}
\label{eq:amplitude}
 C_c=\frac{1}{2Z_\sigma}
       +\frac{\zeta(2+2\sigma)}{4Z_\sigma^3}+O(\sigma^4),
 \qquad
 C_c-\frac{1}{2Z_\sigma}
       =\frac{\pi^2}{24}\sigma^3+O(\sigma^4).
\end{equation}
```
Indeed, divide <a href="#eq:main" data-reference-type="eqref"
data-reference="eq:main">[eq:main]</a> by $`2Z_\sigma`$ and use
$`Z_\sigma^{-1}=\sigma+O(\sigma^2)`$. This is an asymptotic improvement
over the branching bound, not an evaluated error guarantee at a
specified positive exponent.

The leading limit $`p_c\to1`$ is raised for this undirected model in .
That paper develops explicit upper bounds using monotone paths, which
also apply to the oriented problem. The correction in
<a href="#eq:main" data-reference-type="eqref"
data-reference="eq:main">[eq:main]</a> concerns the undirected model and
its exact linear Bernoulli bond probabilities.

The term $`D^{*2}(0)`$ is familiar from critical-point expansions. In a
spread-out regime above the upper critical dimension, van der Hofstad
and Sakai obtain
``` math
p_c=1+D^{*2}(0)+\frac12\sum_{n\ge3}(n+1)D^{*n}(0)+O(\beta^2),
 \qquad \beta=L^{-d}.
```
That theorem fixes the profile and takes the spread parameter $`L`$
large; its percolation statement assumes $`d>6`$. It does not directly
cover <a href="#eq:kernel" data-reference-type="eqref"
data-reference="eq:kernel">[eq:kernel]</a> with dimension one and
$`\sigma\downarrow0`$. Furthermore, the general lace-expansion parameter
here must dominate $`\|D_\sigma\|_\infty=\Theta(\sigma)`$, so an error
of its square would be too large to determine
<a href="#eq:limit" data-reference-type="eqref"
data-reference="eq:limit">[eq:limit]</a>.

We use the kernel-general infrared theorem of Heydenreich, van der
Hofstad and Sakai , and the first-coefficient events of Borgs, Chayes,
van der Hofstad, Slade and Spencer . The additional estimates below keep
the dependence on $`\sigma`$ explicit. The two restrictions that matter
are the original first attachment being nonzero, and a terminal vertex
lying outside a deleted-bond cluster. They leave a single main term in
which deletion of the first bond removes one of two apparent two-step
contributions. Only a one-sided bound on this coefficient is required.

Throughout, $`f*g`$ denotes convolution on $`\mathbb Z`$, $`f^{*m}`$ a
convolution power, and $`\delta(x)=\mathbf 1_{\{x=0\}}`$. Fourier
transforms are $`\widehat f(k)=\sum_x f(x)e^{ikx}`$, with normalized
measure $`\mathrm dk/(2\pi)`$ on $`[-\pi,\pi]`$. All constants denoted
by $`c`$ or $`K`$ are finite and may increase from line to line. Unless
additional indices are shown, they are independent of $`\sigma`$ and of
$`p\in[1,p_c(\sigma))`$ on one sufficiently small fixed interval
$`0<\sigma<\sigma_0`$. No claim of uniformity in growing convolution
orders is made.

# Uniform estimates for the power-law kernel

Write $`s=\sigma`$, $`Z=Z_s`$, $`D=D_s`$, and $`d(k)=\widehat D_s(k)`$
within proofs. Integral comparison gives
``` math
\begin{equation}
\label{eq:zeta-bounds}
 s^{-1}\le Z\le1+s^{-1}.
\end{equation}
```
In particular $`\|D\|_\infty\le s/2`$. The following estimates also
control the very small Fourier frequencies, where pointwise convergence
of $`d`$ to zero would not suffice.

<div id="lem:fourier" class="lemma">

**Lemma 2**. *Let $`L_0=\pi+1+\log2`$. For $`0<s\le1/2`$ and
$`0<|k|\le\pi`$,
``` math
\begin{align}
 |d(k)|&\le \min\{1,s[L_0+\log_+(1/|k|)]\},\label{eq:log-bound}\\
 1-d(k)&\ge\frac13\left(\frac{|k|}{2\pi}\right)^s.\label{eq:gap}
\end{align}
```
For fixed integers $`r\ge1`$, $`q\ge1`$, there is a constant $`K_{r,q}`$
such that
``` math
\begin{equation}
\label{eq:J}
 J_{r,q}(s):=\int_{-\pi}^{\pi}\frac{|d(k)|^r}{[1-d(k)]^q}\frac{\mathrm dk}{2\pi}
 \le K_{r,q}s^r
 \quad\left(0<s\le\min\{1/2,1/(2q)\}\right).
\end{equation}
```
The corresponding estimate with $`q=0`$ holds for $`0<s\le1/2`$.*

</div>

<div class="proof">

*Proof.* By symmetry it is enough to consider $`0<k\le\pi`$. Partial
sums of $`e^{ink}`$ over an interval have modulus at most
$`1/\sin(k/2)`$. Abel summation against the decreasing sequence
$`n^{-1-s}`$ therefore gives
``` math
\begin{equation}
\label{eq:abel}
 \left|\sum_{n=N}^\infty n^{-1-s}e^{ink}\right|
 \le\frac{N^{-1-s}}{\sin(k/2)}
 \le\frac{\pi}{k}N^{-1-s}\qquad(N\ge1).
\end{equation}
```
For $`k\le1`$, split the series defining $`Zd(k)`$ at
$`N=\lceil1/k\rceil`$. The head is at most
$`1+\log N\le1+\log2+\log(1/k)`$ in absolute value, and
<a href="#eq:abel" data-reference-type="eqref"
data-reference="eq:abel">[eq:abel]</a> bounds the tail by $`\pi`$. For
$`k\ge1`$, use <a href="#eq:abel" data-reference-type="eqref"
data-reference="eq:abel">[eq:abel]</a> with $`N=1`$. Division by
$`Z\ge1/s`$ gives the second bound in
<a href="#eq:log-bound" data-reference-type="eqref"
data-reference="eq:log-bound">[eq:log-bound]</a>; the bound by one
follows because $`d`$ is a characteristic function.

For the spectral gap, take $`N=\lceil\pi/k\rceil`$, so that
$`\pi/k\le N\le2\pi/k`$. Positivity of $`1-\cos(nk)`$ and the tail
integral give
``` math
\begin{align*}
 Z[1-d(k)]
 &\ge\sum_{n=N}^\infty n^{-1-s}[1-\cos(nk)]\\
 &\ge \frac{N^{-s}}s-\frac{\pi}{k}N^{-1-s}
 \ge N^{-s}(s^{-1}-1).
\end{align*}
```
Since $`(1-s)/(sZ)\ge(1-s)/(1+s)\ge1/3`$, this proves
<a href="#eq:gap" data-reference-type="eqref"
data-reference="eq:gap">[eq:gap]</a>. Retaining the entire tail is what
avoids a loss of a factor $`s`$ in this estimate.

Combining the two bounds shows that
``` math
J_{r,q}(s)\le
 \frac{3^q(2\pi)^{qs}}{\pi}s^r
 \int_0^\pi[L_0+\log_+(1/k)]^r k^{-qs}\,\mathrm dk.
```
On $`(0,1)`$, the substitution $`t=-\log k`$ bounds the last integral by
$`\int_0^\infty(L_0+t)^r e^{-t/2}\,\mathrm dt`$ when $`qs\le1/2`$. On
$`[1,\pi]`$ it is at most $`\pi L_0^r`$. Also
$`(2\pi)^{qs}\le(2\pi)^{1/2}`$. These bounds provide an explicit finite
choice of $`K_{r,q}`$. For $`q=0`$ the same calculation omits the gap
factor. ◻

</div>

We shall need the following immediate consequences:
``` math
\begin{align}
 S_2=D^{*2}(0)=\int_{-\pi}^{\pi}d(k)^2\frac{\mathrm dk}{2\pi}
 &=\frac{\zeta(2+2s)}{2Z^2}
   =\frac{\pi^2}{12}s^2+O(s^3),\label{eq:S2}\\
 I_{2,1}:=\int_{-\pi}^{\pi}\frac{d(k)^2}{1-d(k)}\frac{\mathrm dk}{2\pi}
 &=S_2+O(s^3),\label{eq:I21}\\
 J_{2,3}&=O(s^2),\qquad J_{3,2}=O(s^3).\label{eq:needed-J}
\end{align}
```
For <a href="#eq:S2" data-reference-type="eqref"
data-reference="eq:S2">[eq:S2]</a>,
<a href="#eq:zeta-bounds" data-reference-type="eqref"
data-reference="eq:zeta-bounds">[eq:zeta-bounds]</a> implies
$`Z^{-1}=s+O(s^2)`$, and the convergent series
$`\sum_{n\ge1}(\log n)n^{-2}`$ gives $`\zeta(2+2s)=\zeta(2)+O(s)`$. For
<a href="#eq:I21" data-reference-type="eqref"
data-reference="eq:I21">[eq:I21]</a>, use
``` math
I_{2,1}-S_2=\int_{-\pi}^{\pi}\frac{d(k)^3}{1-d(k)}\frac{\mathrm dk}{2\pi},
 \qquad |I_{2,1}-S_2|\le2J_{3,2},
```
since $`1-d(k)\le2`$. None of these estimates assumes $`d(k)\ge0`$.

# A nonbacktracking lower bound

For this section define the pointwise moments
``` math
S_m=\sum_{x\ne0}D(x)^m
 =2^{1-m}\frac{\zeta(m(1+s))}{Z^m}\qquad(m\ge2).
```
Only $`S_2`$ is identified here with a convolution return probability;
in particular, $`S_3=\sum_xD(x)^3`$ is not $`D^{*3}(0)`$.

<div id="prop:NB" class="proposition">

**Proposition 3**. *For sufficiently small $`s>0`$, the equation
``` math
\begin{equation}
\label{eq:NB-root}
 F_s(p):=\sum_{x\ne0}\frac{pD(x)}{1+pD(x)}=1
\end{equation}
```
has a unique solution $`p_\mathrm{NB}\in(1,2)`$. Moreover,
``` math
\begin{equation}
\label{eq:NB-result}
 p_c\ge p_\mathrm{NB}=1+S_2+O(S_3+S_2^2)
              =1+S_2+O(s^3).
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Fix $`p>0`$ with $`F:=F_s(p)<1`$, and put $`q_x=pD(x)`$ and
$`f(x)=(1+q_x)^{-1}`$ for $`x\ne0`$. On bounded nonnegative functions of
a previous displacement define the positive operator
``` math
(Bh)(x)=\sum_{y\ne0,\,y\ne-x}q_yh(y).
```
It is bounded in the supremum norm by $`p`$. Symmetry gives
``` math
Bf(x)=F-\frac{q_x}{1+q_x}=f(x)-(1-F)\le Ff(x),
```
where the last inequality uses $`f(x)\le1`$. Writing
$`q_{\max}=\sup_xq_x`$, we have $`1\le(1+q_{\max})f`$, so positivity and
induction imply
``` math
B^{n-1}1\le(1+q_{\max})F^{n-1}f.
```
The total product weight $`W_n`$ of nonbacktracking walks of length
$`n`$ starting at zero consequently satisfies
``` math
\begin{equation}
\label{eq:walk-weight}
 W_n=\sum_xq_x(B^{n-1}1)(x)
 \le(1+q_{\max})F^n\qquad(n\ge1).
\end{equation}
```
All these sums are nonnegative and finite; for example $`W_n\le p^n`$.

Every self-avoiding path is nonbacktracking, and its bond-open
probability is the product of its bond probabilities because its
unordered bonds are distinct. A union bound therefore bounds the
probability of an open self-avoiding path of length $`n`$ from zero by
$`W_n`$. We do not assign product probabilities to the nonbacktracking
walks that repeat bonds; their weights only enlarge the numerical upper
bound. Each vertex has finite open degree almost surely, since its
expected degree is $`p<\infty`$. By countability the random graph is
locally finite almost surely. An infinite component then has
self-avoiding paths of every finite length from each of its vertices.
Equation <a href="#eq:walk-weight" data-reference-type="eqref"
data-reference="eq:walk-weight">[eq:walk-weight]</a> proves absence of
an infinite cluster whenever $`F_s(p)<1`$. The case $`p=0`$ is
immediate.

The function $`F_s`$ is continuous and strictly increasing, by
domination by $`pD(x)`$ on bounded intervals. The exact expansion
``` math
\begin{equation}
\label{eq:NB-expansion}
 F_s(p)=p-p^2S_2+p^3T_3(p),\qquad
 T_3(p)=\sum_x\frac{D(x)^3}{1+pD(x)},\quad0\le T_3(p)\le S_3,
\end{equation}
```
shows $`F_s(1)<1`$. If $`a=S_2\le1/8`$, then
``` math
F_s(1+2a)\ge1+2a-(1+2a)^2a
 =1+a(1-4a-4a^2)>1.
```
There is thus exactly one root in $`(1,1+2a)`$, and
$`p_c\ge p_\mathrm{NB}`$. The interval lies below $`2<2Z`$, so all
parameters used are admissible. For instance $`0<s\le1/4`$ ensures
$`S_2\le\zeta(2)s^2/2<1/8`$.

Set $`x=p_\mathrm{NB}-1\in(0,2a)`$.
Equation <a href="#eq:NB-expansion" data-reference-type="eqref"
data-reference="eq:NB-expansion">[eq:NB-expansion]</a> yields
``` math
x=p_\mathrm{NB}^2a-p_\mathrm{NB}^3T_3(p_\mathrm{NB}),\qquad
 |x-a|\le(4a+4a^2)a+8S_3.
```
Since $`S_3\le\zeta(3)s^3/4`$, the asserted uniform expansion follows. ◻

</div>

# The infrared input and the required diagram estimates

For fixed $`s`$, write $`\tau_p(x)=\mathbb P_p(0\leftrightarrow x)`$ and
$`\chi(p)=\sum_x\tau_p(x)`$. We use the standard equality of the
susceptibility threshold and the percolation threshold, in the form
stated for this long-range model in . Consequently $`\chi(p)<\infty`$
for every $`p<p_c`$. This sharpness input is distinct from a definition
of $`p_c`$ by susceptibility.

For percolation, Assumption 2.1 of requires a symmetric probability
kernel with $`D(0)=0`$, together with
``` math
\begin{equation}
\label{eq:HHS-assumptions}
 \|D\|_\infty\le\beta,\qquad
 \int_{-\pi}^{\pi}\frac{d(k)^2}{[1-d(k)]^3}\frac{\mathrm dk}{2\pi}\le\beta,
\end{equation}
```
for sufficiently small $`\beta`$. The kernel
<a href="#eq:kernel" data-reference-type="eqref"
data-reference="eq:kernel">[eq:kernel]</a> has full support off zero, in
particular it contains the nearest neighbors.
Lemma <a href="#lem:fourier" data-reference-type="ref"
data-reference="lem:fourier">2</a> verifies
<a href="#eq:HHS-assumptions" data-reference-type="eqref"
data-reference="eq:HHS-assumptions">[eq:HHS-assumptions]</a> with
$`\beta=B_0s`$ for a fixed $`B_0`$ and all sufficiently small $`s`$.
Here $`B_0`$ is independent of $`s`$; it is chosen before reducing the
interval of $`s`$. Theorem 2.3, equation (1.35), and the threshold
bound (2.6) of then give constants $`K_0,K_1`$ such that
``` math
\begin{align}
 1\le p_c&\le1+K_0s,\label{eq:coarse-pc}\\
 0\le\widehat\tau_p(k)&\le
 \frac{1+K_1s}{\chi(p)^{-1}+p[1-d(k)]},\qquad p<p_c.
 \label{eq:IR}
\end{align}
```
The constants in this use of the theorem are fixed by its smallness
threshold and the dimension $`d=1`$, not by an additional spread
parameter. The parameter $`s=3`$ in its percolation assumption is a
diagram exponent; it is unrelated to our variable $`s=\sigma`$.

For completeness, the Fourier nonnegativity in
<a href="#eq:IR" data-reference-type="eqref"
data-reference="eq:IR">[eq:IR]</a> is a property of percolation
connections. For every finitely supported complex sequence $`(a_x)`$,
``` math
\sum_{x,y}a_x\overline{a_y}\tau_p(y-x)
 =\mathbb E_p\sum_{\mathcal C}
       \left|\sum_{x\in\mathcal C}a_x\right|^2\ge0,
```
where the sum is over the open clusters. Thus $`\tau_p`$ is positive
definite; since it is in $`\ell^1`$ subcritically, its continuous
Fourier transform is nonnegative. This does not assert nonnegativity of
$`d(k)`$. For the rest of the proof we restrict to $`1\le p<p_c`$, where
``` math
\begin{equation}
\label{eq:IR-simplified}
 \widehat\tau_p(k)\le\frac{b_s}{p[1-d(k)]},\qquad b_s=1+K_1s,
 \quad k\ne0.
\end{equation}
```
The single point $`k=0`$ has no effect on the integrals used below.

Suppress $`p`$ from $`\tau_p`$ and put $`q=pD`$. Define
``` math
\begin{equation}
\label{eq:diagram-defs}
 T(x)=(q*\tau^{*3})(x),\quad T_* =\sup_xT(x),\quad
 T_0=T(0),\quad A=\tau^{*3}(0),\quad B=\tau^{*2}(0).
\end{equation}
```
All these quantities are finite at a fixed subcritical parameter.

<div id="lem:budget" class="lemma">

**Lemma 4**. *Uniformly for $`1\le p<p_c`$ and sufficiently small
$`s>0`$,
``` math
\begin{equation}
\label{eq:budget}
 T_*=O(s),\qquad T_0=O(s^2),\qquad
 0\le A-1\le3T_0,\qquad0\le A-B\le3T_0,
 \qquad B=1+O(s^2).
\end{equation}
```*

</div>

<div class="proof">

*Proof.* Set $`h=\tau-\delta\ge0`$. The first-edge connection bound
gives $`h\le q*\tau`$: for a nonzero endpoint choose the first bond of a
simple open path, remove that bond, and use independence and a union
bound. Since $`\tau\ge\delta`$,
``` math
\begin{equation}
\label{eq:triple-positive}
 \tau^{*3}-\delta
 =h*(\tau^{*2}+\tau+\delta)
 \le3h*\tau^{*2}\le3q*\tau^{*3}=3T.
\end{equation}
```
Convolving once with $`q`$ shows
``` math
T(x)\le q(x)+3(q^{*2}*\tau^{*3})(x).
```
The Fourier integrand $`p^2d(k)^2\widehat\tau(k)^3`$ is nonnegative.
Fourier inversion therefore bounds the last convolution at every $`x`$
by its value at zero. By
<a href="#eq:IR-simplified" data-reference-type="eqref"
data-reference="eq:IR-simplified">[eq:IR-simplified]</a>,
``` math
\begin{equation}
\label{eq:U}
 U:=(q^{*2}*\tau^{*3})(0)
 \le\frac{b_s^3}{p}J_{2,3}=O(s^2).
\end{equation}
```
Thus $`T_*\le p\|D\|_\infty+3U=O(s)`$ by
<a href="#eq:coarse-pc" data-reference-type="eqref"
data-reference="eq:coarse-pc">[eq:coarse-pc]</a>, while $`T_0\le3U`$
because $`D(0)=0`$.
Equation <a href="#eq:triple-positive" data-reference-type="eqref"
data-reference="eq:triple-positive">[eq:triple-positive]</a> at zero
gives $`A-1\le3T_0`$. Finally $`1\le B\le A`$, so both remaining
assertions follow. ◻

</div>

In particular, the closed value $`T_0`$ is smaller than the spatial
supremum $`T_*`$. Keeping that distinction will turn the error terms
below into $`O(s^3)`$, whereas a bound by $`T_*^2`$ alone would give
only $`O(s^2)`$.

# A uniform upper bound on the first lace coefficient

The decomposition below follows van der Hofstad and Sakai : nonzero
first attachment, terminal membership in a deleted-bond cluster, and
deletion of the first bond. The additional estimate is the separation
$`T_*=O(s)`$ from $`T_0,A-1,A-B=O(s^2)`$. It improves the remainder to
$`O(s^3)`$ in this changing-exponent regime. The reusable bound to keep
in view is
<a href="#eq:exact-positive-bound" data-reference-type="eqref"
data-reference="eq:exact-positive-bound">[eq:exact-positive-bound]</a>:
an exact subtraction $`p^2S_2`$ and nonnegative errors each carrying an
extra small factor.

We specify the source events before estimating them. This also records
which restrictions survive the diagram bounds. Write
$`x\Leftrightarrow y`$ if $`x=y`$ or there are two bond-disjoint open
paths from $`x`$ to $`y`$. For a set $`\mathcal A`$, the event
$`\{x\xleftrightarrow{\,\mathcal A\,}y\}`$ means that $`x`$ and $`y`$
are connected and every open path between them has a bond with an
endpoint in $`\mathcal A`$, or that $`x=y\in\mathcal A`$. This is the
“through” convention of . Let $`\widetilde{\mathcal C}^{\{u,v\}}(x)`$ be
the cluster of $`x`$ when bond $`\{u,v\}`$ is forced vacant.

A directed bond $`(a,b)`$ is pivotal for $`v\leftrightarrow x`$ if its
removal disconnects $`v`$ from $`x`$, with $`a`$ on the $`v`$ side and
$`b`$ on the $`x`$ side. Let $`\mathcal P(v,x)`$ be the set of these
directed pivotal bonds. Define
``` math
\begin{equation}
\label{eq:Eprime}
 E'(v,x;\mathcal A)=\{v\xleftrightarrow{\,\mathcal A\,}x\}
 \cap\left\{\nexists(a,b)\in\mathcal P(v,x):
                    \{v\xleftrightarrow{\,\mathcal A\,}a\}\right\}.
\end{equation}
```
On the connection event in this definition the pivotal bonds are open.
The event $`E'`$ itself need not be increasing. We use the van den
Berg–Kesten (BK) inequality only on the increasing connection events in
its cited diagrammatic upper bounds.

Use subscripts $`0,1,2`$ for independent percolation configurations at
the same parameter. With the set from level 0 held fixed in the level 1
probability, the first coefficient is
``` math
\begin{equation}
\label{eq:pi1-definition}
 \pi_p^{(1)}(x)=\sum_{u,v}q(v-u)\,
 \mathbb E_0\left[\mathbf 1_{\{0\Leftrightarrow u\}}
  \mathbb P_1\left(E'(v,x;
    \widetilde{\mathcal C}_0^{\{u,v\}}(0))\right)\right].
\end{equation}
```
This is , also used in , with each bond weight replaced by its
probability $`q(v-u)`$. Set
$`\overline\pi_p^{(1)}=\sum_x\pi_p^{(1)}(x)`$.

<div id="prop:pi1" class="proposition">

**Proposition 5**. *There is a constant $`K_2`$ such that, uniformly for
$`1\le p<p_c`$ and $`0<s<\sigma_0`$,
``` math
\begin{equation}
\label{eq:pi1-bound}
 0\le\overline\pi_p^{(1)}
 \le(2p-p^2)S_2+K_2s^3\le S_2+K_2s^3.
\end{equation}
```*

</div>

## The two restricted error terms

For $`u=0`$ abbreviate
$`\mathcal C_v=\widetilde{\mathcal C}_0^{\{0,v\}}(0)`$ and
$`\tau_v^{\mathrm{del}}(x)=\mathbb P_p(x\in\mathcal C_v)`$. Split the
sum in <a href="#eq:pi1-definition" data-reference-type="eqref"
data-reference="eq:pi1-definition">[eq:pi1-definition]</a> into the
three disjoint cases
``` math
\begin{equation}
\label{eq:split}
 u\ne0;\qquad u=0,\ x\notin\mathcal C_v;\qquad
 u=0,\ x\in\mathcal C_v.
\end{equation}
```
The last part is at most
``` math
\begin{equation}
\label{eq:M}
 M_p=\sum_{v,x}q(v)\tau_v^{\mathrm{del}}(x)\tau(x-v),
\end{equation}
```
by dropping the no-pivotal requirement, retaining only the connection
$`v\leftrightarrow x`$ at level 1, and using independence of the two
levels.

To bound the first two parts, let $`\circ`$ denote disjoint occurrence
with disjoint open-bond witnesses. The source events for $`N=1`$ are
``` math
\begin{align*}
 F_0(0,u,w,z)&=\{0\leftrightarrow u\}\circ\{0\leftrightarrow w\}
   \circ\{w\leftrightarrow u\}\circ\{w\leftrightarrow z\},\\
 F_1(v,t,z,x)&=\{v\leftrightarrow t\}\circ\{t\leftrightarrow z\}
   \circ\{t\leftrightarrow x\}\circ\{z\leftrightarrow x\}.
\end{align*}
```
Their terminal inclusion is
``` math
\begin{equation}
\label{eq:terminal-inclusion}
 E'(v,x;\mathcal C)\subseteq
 \bigcup_{z\in\mathcal C}\ \bigcup_t F_1(v,t,z,x).
\end{equation}
```
In the joint event of
<a href="#eq:pi1-definition" data-reference-type="eqref"
data-reference="eq:pi1-definition">[eq:pi1-definition]</a>, the initial
double connection and the cluster membership in this inclusion are
bounded by $`F_0`$ at level 0, as in . In particular the vertex $`u`$ in
$`F_0(0,u,w,z)`$ is the original $`u`$ of
<a href="#eq:pi1-definition" data-reference-type="eqref"
data-reference="eq:pi1-definition">[eq:pi1-definition]</a>; it has not
been summed out or renamed. In words, the terminal inclusion retains a
vertex in the specified cluster. If the endpoint lies outside that
cluster, these two vertices cannot coincide; this strict exclusion must
survive the later upper bounds.

Put $`\widetilde\tau=q*\tau`$ and
``` math
A_3(a,b,c)=\tau(c-a)\tau(b-a)\tau(c-b).
```
The union bound, BK for $`F_0,F_1`$, and summation over $`v`$ give for
the $`u\ne0`$ part
``` math
\begin{equation}
\label{eq:first-error-raw}
 \sum_{u\ne0,w} A_3(0,u,w)
 \sum_{z,t,x}\widetilde\tau(t-u)\tau(z-w)A_3(z,t,x).
\end{equation}
```
For each $`u,w`$, Cauchy–Schwarz gives $`(\tau*\tau)(r)\le B`$, and
therefore
``` math
\begin{align*}
 \sum_{z,t,x}\widetilde\tau(t-u)\tau(z-w)A_3(z,t,x)
 &=\sum_{z,t}\widetilde\tau(t-u)\tau(z-w)
     \tau(t-z)(\tau*\tau)(t-z)\\
 &\le B T(w-u)\le BT_*.
\end{align*}
```
Also $`\sum_{u,w}A_3(0,u,w)=A`$. The restriction $`u\ne0`$ excludes the
entire $`u=0`$ slice, whose sum is $`\sum_w\tau(w)^2=B`$. Consequently
``` math
\begin{equation}
\label{eq:first-error}
 \text{the first part of \eqref{eq:split}}
 \le BT_*(A-B)=O(s^3).
\end{equation}
```

For the second part,
<a href="#eq:terminal-inclusion" data-reference-type="eqref"
data-reference="eq:terminal-inclusion">[eq:terminal-inclusion]</a>
supplies a vertex $`z\in\mathcal C_v`$. The condition
$`x\notin\mathcal C_v`$ therefore forces the precise restriction
$`z\ne x`$. Retain it before dropping $`x\notin\mathcal C_v`$. Since
$`\mathbb P_p(z\in\mathcal C_v)\le\tau(z)`$, BK bounds this part by
``` math
\begin{equation}
\label{eq:second-error-raw}
 \sum_{v,z,t,x:\,z\ne x}q(v)\tau(z)\tau(t-v)
          \tau(t-z)\tau(t-x)\tau(z-x).
\end{equation}
```
For $`r=t-z`$, the strict terminal sum is
``` math
\begin{equation}
\label{eq:hbad}
 H(r)=\tau(r)\big[(\tau*\tau)(r)-\tau(r)\big]\ge0,
 \qquad \sum_rH(r)=A-B.
\end{equation}
```
Indeed, the removed $`x=z`$ term has value $`\tau(r)^2`$. Summing
$`v,z`$ in <a href="#eq:second-error-raw" data-reference-type="eqref"
data-reference="eq:second-error-raw">[eq:second-error-raw]</a> now gives
``` math
\begin{equation}
\label{eq:second-error}
 \sum_r H(r)(q*\tau^{*2})(r)
 \le T_*(A-B)=O(s^3),
\end{equation}
```
where $`q*\tau^{*2}\le q*\tau^{*3}`$ follows from $`\tau\ge\delta`$.
Together with <a href="#eq:M" data-reference-type="eqref"
data-reference="eq:M">[eq:M]</a>, this proves the uniform reduction
``` math
\begin{equation}
\label{eq:pi1-M}
 \overline\pi_p^{(1)}\le M_p+O(s^3).
\end{equation}
```
All error constants in this reduction follow from
Lemma <a href="#lem:budget" data-reference-type="ref"
data-reference="lem:budget">4</a>; no estimate on a critical coefficient
is used.

## The deleted bond and the main convolution

Let $`F_p=(q*\tau^{*2})(0)`$. Deletion reduces connection probabilities,
so $`M_p\le F_p`$. A necessary improvement comes just from the terms
$`x=v`$. Conditioning on bond $`\{0,v\}`$ gives the exact identity
``` math
\begin{equation}
\label{eq:bond-conditioning}
 \tau(v)=q(v)+[1-q(v)]\tau_v^{\mathrm{del}}(v)\qquad(v\ne0).
\end{equation}
```
The parameter range in use has $`\|q\|_\infty=O(s)<1`$. Retaining the
improvement at $`x=v`$, where $`\tau(x-v)=1`$, yields
``` math
\begin{align}
 M_p&\le F_p-\sum_vq(v)[\tau(v)-\tau_v^{\mathrm{del}}(v)]\notag\\
 &=F_p-p^2S_2+R_p,\qquad
 R_p=\sum_vq(v)^2\tau_v^{\mathrm{del}}(v).\label{eq:deleted-subtraction}
\end{align}
```
The nonnegative remainder is cubic:
``` math
\begin{equation}
\label{eq:deleted-error}
 0\le R_p\le\|q\|_\infty\sum_vq(v)\tau(v)
 =\|q\|_\infty(q*\tau)(0)
 \le\|q\|_\infty T_0=O(s^3).
\end{equation}
```
This is an exact deleted-bond subtraction; expanding an inverse vacancy
probability is unnecessary.

Before making asymptotic estimates, the preceding event bounds give the
single explicit inequality
``` math
\begin{equation}
\label{eq:exact-positive-bound}
 \boxed{\quad
 \overline\pi_p^{(1)}\le F_p-p^2S_2
  +\|q\|_\infty T_0+(B+1)T_*(A-B).
 \quad}
\end{equation}
```
The two terms after the subtraction are nonnegative and each is
$`O(s^3)`$ by Lemma <a href="#lem:budget" data-reference-type="ref"
data-reference="lem:budget">4</a>. Both strict restrictions leave the
factor $`A-B`$. More sharply, the positive first-edge inequality gives
$`A-B=(h*\tau^{*2})(0)\le T_0`$ and $`B-1\le2(q*\tau^{*2})(0)\le2T_0`$.

To estimate $`F_p`$, use $`h=\tau-\delta\le q*\tau`$ and $`D(0)=0`$:
``` math
\begin{align}
 F_p&=2p(D*h)(0)+p(D*h*h)(0)\notag\\
 &\le2p^2(D^{*2}*\tau)(0)
      +p^3(D^{*3}*\tau^{*2})(0).\label{eq:F-decomposition}
\end{align}
```
The first Fourier integrand below is nonnegative. Applying
<a href="#eq:IR-simplified" data-reference-type="eqref"
data-reference="eq:IR-simplified">[eq:IR-simplified]</a> with its factor
$`p`$ retained gives
``` math
\begin{align}
 p^2(D^{*2}*\tau)(0)
 &\le p b_s I_{2,1},\label{eq:V2}\\
 0\le p^3(D^{*3}*\tau^{*2})(0)
 &\le p b_s^2 J_{3,2}.\label{eq:V3}
\end{align}
```
For <a href="#eq:V3" data-reference-type="eqref"
data-reference="eq:V3">[eq:V3]</a> the convolution is nonnegative in
real space, but its Fourier integrand $`p^3d(k)^3\widehat\tau(k)^2`$ can
have either sign. Taking its absolute value before using
<a href="#eq:IR-simplified" data-reference-type="eqref"
data-reference="eq:IR-simplified">[eq:IR-simplified]</a> is what
justifies the bound.

Equations <a href="#eq:I21" data-reference-type="eqref"
data-reference="eq:I21">[eq:I21]</a>,
<a href="#eq:needed-J" data-reference-type="eqref"
data-reference="eq:needed-J">[eq:needed-J]</a>, and
<a href="#eq:coarse-pc" data-reference-type="eqref"
data-reference="eq:coarse-pc">[eq:coarse-pc]</a> now imply
``` math
F_p\le2p b_s I_{2,1}+p b_s^2J_{3,2}
      =2pS_2+O(s^3).
```
Combining this with <a href="#eq:pi1-M" data-reference-type="eqref"
data-reference="eq:pi1-M">[eq:pi1-M]</a>–<a href="#eq:deleted-error" data-reference-type="eqref"
data-reference="eq:deleted-error">[eq:deleted-error]</a> proves
``` math
\overline\pi_p^{(1)}\le(2p-p^2)S_2+O(s^3).
```
Finally $`2p-p^2=1-(p-1)^2\le1`$. This proves
Proposition <a href="#prop:pi1" data-reference-type="ref"
data-reference="prop:pi1">5</a>, including its uniformity over the full
subcritical interval $`[1,p_c)`$.

# The positive finite-order remainder and the threshold

We use the finite-order lace identity, rather than an infinite signed
series. Let
``` math
\pi_p^{(0)}(x)=\mathbb P_p(0\Leftrightarrow x)-\delta(x),\qquad
 \Pi_1=\pi_p^{(0)}-\pi_p^{(1)}.
```
The identity at truncation order $`M=1`$ is
``` math
\begin{equation}
\label{eq:finite-lace}
 \tau=\delta+q*\tau+\Pi_1*q*\tau+\Pi_1+\mathcal R_1,
 \qquad \mathcal R_1(x)\ge0.
\end{equation}
```
This is ; the weighted infinite-lattice version is . For clarity, its
positive remainder has the form
``` math
\begin{align}
\label{eq:remainder-positive}
 \mathcal R_1(x)
 =\sum_{u,v,a,b}&q(v-u)q(b-a)\,
 \mathbb E_0\Big[\mathbf 1_{\{0\Leftrightarrow u\}}
 \mathbb E_1\Big[\mathbf 1_{E'(v,a;\widetilde{\mathcal C}_0^{\{u,v\}}(0))}
 \notag\\[-2pt]
 &\hspace{39mm}\times
 \mathbb P_2\big(\{b\xleftrightarrow{\,\widetilde{\mathcal C}_1^{\{a,b\}}(v)\,}x\}\big)
 \Big]\Big].
\end{align}
```
Dropping the through-cluster constraint at level 2 gives the pointwise
bound from :
``` math
\begin{equation}
\label{eq:remainder-bound}
 0\le\mathcal R_1\le\pi_p^{(1)}*q*\tau.
\end{equation}
```

The cited construction applies to subcritical infinite graphs, where
clusters are almost surely finite, and its probability identities allow
inhomogeneous independent bond weights. We use HHS’s weighted
infinite-volume identity directly. Connection-event BK bounds on the
countable bond set can equivalently be obtained by finite witness
approximation. No monotone convergence assertion for the nonmonotone
event $`E'`$ is needed. For each fixed $`p<p_c`$, all sums in
<a href="#eq:finite-lace" data-reference-type="eqref"
data-reference="eq:finite-lace">[eq:finite-lace]</a> are absolutely
convergent: $`\pi_p^{(0)}\ge0`$ and
``` math
\sum_x\pi_p^{(0)}(x)\le\chi(p)-1<\infty,
```
Proposition <a href="#prop:pi1" data-reference-type="ref"
data-reference="prop:pi1">5</a> bounds the sum of $`\pi_p^{(1)}`$, and
<a href="#eq:remainder-bound" data-reference-type="eqref"
data-reference="eq:remainder-bound">[eq:remainder-bound]</a> gives
$`\sum_x\mathcal R_1(x)\le p\overline\pi_p^{(1)}\chi(p)<\infty`$. The
signed convolution is absolutely summable by these same bounds.

Set
``` math
U_s=S_2+K_2s^3,\qquad
 a_p=1+\sum_x\pi_p^{(0)}(x)-\overline\pi_p^{(1)}.
```
Reduce $`\sigma_0`$ so that $`U_s<1/2`$. Nonnegativity of
$`\pi_p^{(0)}`$ and
Proposition <a href="#prop:pi1" data-reference-type="ref"
data-reference="prop:pi1">5</a> imply $`a_p\ge1-U_s>0`$. Summing
<a href="#eq:finite-lace" data-reference-type="eqref"
data-reference="eq:finite-lace">[eq:finite-lace]</a> gives the exact
scalar identity
``` math
\begin{equation}
\label{eq:scalar}
 \chi(p)[1-pa_p]=a_p+\sum_x\mathcal R_1(x)>0.
\end{equation}
```
Since $`\chi(p)`$ is positive and finite, for every $`1\le p<p_c`$,
``` math
\begin{equation}
\label{eq:subcrit-upper}
 p<\frac1{a_p}\le\frac1{1-U_s}.
\end{equation}
```
If $`p_c=1`$ the same upper bound is automatic; otherwise take the
supremum over the scalar parameters $`p\in[1,p_c)`$. This yields
``` math
\begin{equation}
\label{eq:pc-upper}
 p_c\le\frac1{1-S_2-K_2s^3}=1+S_2+O(s^3),
\end{equation}
```
because $`S_2=O(s^2)`$ and hence $`U_s^2=O(s^4)`$. There is no passage
to a critical Fourier transform, susceptibility divergence, or a
critical limit of a lace coefficient in this argument. Avoidance of
coefficient continuity is not a new general goal: Liu gives a different
argument at criticality through a convolution identity and
nonsummability. Here the positive finite truncation gives a scalar
inequality at every subcritical parameter. The saving is in the
additional correction calculation, not a replacement for the
lace-expansion work underpinning the imported infrared theorem.

The lower bound in
Proposition <a href="#prop:NB" data-reference-type="ref"
data-reference="prop:NB">3</a> and
<a href="#eq:pc-upper" data-reference-type="eqref"
data-reference="eq:pc-upper">[eq:pc-upper]</a> prove
<a href="#eq:main" data-reference-type="eqref"
data-reference="eq:main">[eq:main]</a>.
Formula <a href="#eq:S2" data-reference-type="eqref"
data-reference="eq:S2">[eq:S2]</a> then proves
<a href="#eq:limit" data-reference-type="eqref"
data-reference="eq:limit">[eq:limit]</a>. To make the uniform
quantifiers explicit, choose $`\sigma_0`$ smaller than $`1/6`$, the
fixed smallness threshold needed for
<a href="#eq:HHS-assumptions" data-reference-type="eqref"
data-reference="eq:HHS-assumptions">[eq:HHS-assumptions]</a>, and the
fixed thresholds used for $`\|q\|_\infty<1`$ and $`U_s<1/2`$. Every
estimate above then holds for every real $`0<s<\sigma_0`$ and every
$`p\in[1,p_c(s))`$, with common constants. This completes the proof of
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>.

# A two-scale criterion and additional kernel families

The proof separates two scales rather than requiring a specific zeta
kernel. The following consequence makes that distinction reusable. All
kernels in this section define independent undirected bonds with the
exact linear law $`pD(x)`$.

<div id="thm:criterion" class="theorem">

**Theorem 6** (Two-scale kernel criterion). *Let $`D_\epsilon`$ be even
probability kernels on $`\mathbb Z`$, with $`D_\epsilon(0)=0`$, positive
nearest-neighbor weights, and $`d_\epsilon(k)=\widehat D_\epsilon(k)<1`$
for $`0<|k|\le\pi`$. Suppose the admissible percolating set is nonempty
and, with common constants as $`\epsilon\downarrow0`$,
``` math
\|D_\epsilon\|_\infty=O(\epsilon),\qquad
 \int_{-\pi}^{\pi}\frac{|d_\epsilon|^2}{(1-d_\epsilon)^3}\frac{\mathrm dk}{2\pi}=O(\epsilon^2),
 \qquad
 \int_{-\pi}^{\pi}\frac{|d_\epsilon|^3}{(1-d_\epsilon)^2}\frac{\mathrm dk}{2\pi}=O(\epsilon^3).
```
Then
``` math
p_c(D_\epsilon)=1+\sum_xD_\epsilon(x)^2+O(\epsilon^3).
```
The implicit constant is uniform over families with common hypothesis
constants and a common sufficiently small parameter interval.*

</div>

<div class="proof">

*Proof.* Write $`a=J_{2,3}`$, $`b=J_{3,2}`$ and
$`m=\|D_\epsilon\|_\infty`$. Since $`0\le1-d\le2`$,
$`S_2=\int d^2\frac{\mathrm dk}{2\pi}\le8a=O(\epsilon^2)`$, and the
pointwise third moment is at most $`mS_2=O(\epsilon^3)`$. The proof of
Proposition <a href="#prop:NB" data-reference-type="ref"
data-reference="prop:NB">3</a> uses only evenness, summability and these
moment bounds. It supplies the lower bound with the stated error. Its
test parameters are admissible because $`m\to0`$.

Assumption 2.1 of holds with $`\beta=O(\epsilon)`$. The same theorem
used in Section <a href="#sec:diagrams" data-reference-type="ref"
data-reference="sec:diagrams">4</a> gives $`p_c=1+O(\epsilon)`$ and
<a href="#eq:IR-simplified" data-reference-type="eqref"
data-reference="eq:IR-simplified">[eq:IR-simplified]</a> with
$`b_\epsilon=1+O(\epsilon)`$. Its dimension remains fixed at one. The
proof of Lemma <a href="#lem:budget" data-reference-type="ref"
data-reference="lem:budget">4</a> consequently gives
$`T_*=O(\epsilon)`$, $`T_0=O(\epsilon^2)`$ and
$`A-1,A-B,B-1=O(\epsilon^2)`$. Moreover,
``` math
|I_{2,1}-S_2|\le2J_{3,2}=O(\epsilon^3).
```
The event bounds in Section <a href="#sec:pi1" data-reference-type="ref"
data-reference="sec:pi1">5</a> use neither the power-law formula nor
positivity of its Fourier transform. With these new bounds their exact
deleted-bond inequality gives
$`\overline\pi_p^{(1)}\le(2p-p^2)S_2+O(\epsilon^3)`$ uniformly
subcritically.
Section <a href="#sec:threshold" data-reference-type="ref"
data-reference="sec:threshold">6</a> then gives
$`p_c\le(1-S_2-O(\epsilon^3))^{-1}=1+S_2+O(\epsilon^3)`$. All imported
results, and the inherited event decomposition, are the same as for the
original theorem; no new lace expansion is claimed. ◻

</div>

<div id="thm:additions" class="theorem">

**Theorem 7** (Summable positive additions). *Fix $`B_0<\infty`$. For
any sequence $`b_n\ge0`$ with $`B=\sum_{n\ge1}b_n\le B_0`$, define
``` math
D_s(\pm n)=\frac{n^{-1-s}+b_n}{2(Z_s+B)},\qquad n\ge1,\qquad D_s(0)=0.
```
Uniformly over these sequences, for sufficiently small $`s>0`$,
``` math
\begin{align*}
 p_c&=1+\frac{\zeta(2+2s)+2\sum_{n\ge1}b_nn^{-1-s}
                    +\sum_{n\ge1}b_n^2}{2(Z_s+B)^2}+O_{B_0}(s^3)\\
 &=1+\frac{s^2}{2}\left(\zeta(2)+2\sum_{n\ge1}\frac{b_n}{n}
                                      +\sum_{n\ge1}b_n^2\right)
                                      +O_{B_0}(s^3).
\end{align*}
```
No moment assumption beyond summability is imposed on the additions.*

</div>

<div class="proof">

*Proof.* Let $`d_s^0`$ denote the original power-law characteristic
function. The new kernel is a mixture with original-kernel weight
$`w_s=Z_s/(Z_s+B)`$. Thus
``` math
|d_s(k)|\le |d_s^0(k)|+B/Z_s
 \le s[L_0+B_0+\log_+(1/|k|)],
 \qquad 1-d_s(k)\ge w_s(1-d_s^0(k)).
```
For small $`s`$ uniformly in $`B\le B_0`$, $`w_s\ge1/2`$, so the latter
is at least $`\tfrac16(|k|/(2\pi))^s`$. The integral proof of
Lemma <a href="#lem:fourier" data-reference-type="ref"
data-reference="lem:fourier">2</a> applies with these modified
constants, giving $`J_{r,q}=O_{B_0}(s^r)`$ for fixed $`r,q`$ and
$`qs\le1/2`$. Also $`\|D_s\|_\infty\le(1+B_0)s/2`$. Full support off
zero gives the structural hypotheses. To check that admissible
percolation exists, at $`p=3`$ the model dominates the original kernel
at parameter $`3w_s>2`$ for small $`s`$;
Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a> places that model above its threshold.
The parameter $`3`$ is admissible since $`3\|D_s\|_\infty<1`$
eventually. Theorem <a href="#thm:criterion" data-reference-type="ref"
data-reference="thm:criterion">6</a> proves the first formula.

For the second, $`\sum b_n^2\le B_0^2`$ and
``` math
\left|\sum b_nn^{-1-s}-\sum b_n/n\right|
 \le s\sum b_n\frac{\log n}{n}=O(B_0s).
```
Together with $`\zeta(2+2s)=\zeta(2)+O(s)`$ and
$`(Z_s+B)^{-2}=s^2+O_{B_0}(s^3)`$, this proves the assertion. ◻

</div>

For example, $`b_1=\lambda\ge0`$ and $`b_n=0`$ for $`n>1`$ changes the
coefficient from $`\pi^2/12`$ to $`\pi^2/12+\lambda+\lambda^2/2`$. Thus
the coefficient is sensitive to local connection weights even though the
long-distance exponent is unchanged.

<div id="thm:mixtures" class="theorem">

**Theorem 8** (Compact mixtures of exponents). *Fix
$`0<c_-\le c_+<\infty`$. For any probability measure $`\nu`$ on
$`[c_-,c_+]`$, let $`D_s=\int D^0_{cs}\,\nu(\mathrm dc)`$, where
$`D^0_t`$ is the power-law
kernel <a href="#eq:kernel" data-reference-type="eqref"
data-reference="eq:kernel">[eq:kernel]</a>. Uniformly over $`\nu`$,
``` math
p_c(D_s)=1+\frac{\pi^2}{12}\left(\int c\,\nu(\mathrm dc)\right)^2s^2
           +O_{c_-,c_+}(s^3).
```*

</div>

<div class="proof">

*Proof.* For $`c_+s\le1/2`$, integration of
Lemma <a href="#lem:fourier" data-reference-type="ref"
data-reference="lem:fourier">2</a> gives
``` math
|d_s(k)|\le c_+s[L_0+\log_+(1/|k|)],\qquad
 1-d_s(k)\ge\tfrac13(|k|/(2\pi))^{c_+s}.
```
Thus $`J_{r,q}=O(s^r)`$ when $`qc_+s\le1/2`$, and
$`\|D_s\|_\infty\le c_+s/2`$. Full support again gives the structural
conditions. For admissible percolation, integral comparison yields
``` math
\frac{D^0_{cs}(n)}{D^0_{c_+s}(n)}
 =\frac{Z_{c_+s}}{Z_{cs}}n^{(c_+-c)s}
 \ge\frac{c_-}{c_+(1+c_+s)}\ge\frac{c_-}{2c_+}
```
for small $`s`$. The fixed parameter $`p=6c_+/c_-`$ is eventually
admissible and dominates an original-kernel model at parameter at least
$`3`$. Apply Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a>, then
Theorem <a href="#thm:criterion" data-reference-type="ref"
data-reference="thm:criterion">6</a>. Finally Tonelli’s theorem gives
``` math
S_2=\iint\frac{\zeta(2+(c+d)s)}{2Z_{cs}Z_{ds}}
                  \,\nu(\mathrm dc)\nu(\mathrm dd).
```
Uniformly on the compact parameter square, $`Z_{cs}^{-1}=cs+O(s^2)`$ and
$`\zeta(2+(c+d)s)=\zeta(2)+O(s)`$. This proves the formula. ◻

</div>

# Scope and further questions

The correction in Theorem <a href="#thm:main" data-reference-type="ref"
data-reference="thm:main">1</a> is the two-step return weight of the
exact normalized kernel. The proof requires both the uniform
small-exponent Fourier bounds and the percolation event restrictions;
evaluating random-walk return probabilities alone would not identify the
lace coefficient. The positive odd-truncation remainder is enough for an
upper bound on the threshold, so a matching asymptotic formula for
$`\overline\pi_p^{(1)}`$ and a bound on every higher coefficient are not
part of the argument.

The result fixes dimension one and lets only $`\sigma`$ tend to zero.
The error constant is not evaluated numerically, and the proof gives
neither a third-order coefficient nor a useful quantitative estimate
throughout $`0<\sigma<1`$. Other bond laws, including exponential
connection probabilities, may differ at the correction scale and are not
covered by the theorem. The argument also does not determine the
oriented critical correction. The uniform kernel estimates and the
one-sided lace estimate yield the sufficient criterion and the two
additional families in
Section <a href="#sec:extensions" data-reference-type="ref"
data-reference="sec:extensions">7</a>. Signed additions, unbounded
exponent ratios and useful numerical error constants remain outside
those statements.

# Declarations

#### Data and reproducibility.

This is an analytic study. No numerical experiment or empirical data is
used in the proof. The model, estimates, and imported results are
specified in the text; the manuscript source and bibliography form the
associated research materials.

#### Ethics.

The work involves no human participants, animals, personal data, or
experimental intervention.

#### Contributions and AI disclosure.

OpenAI Codex was used to develop the arguments, compare the cited
sources, perform internal mathematical checks, and prepare this draft.
The scholarly attribution is Anonymous. Evidence Press is the publisher;
account ownership is not a claim of human mathematical contribution. The
supplied review and current checks are AI-assisted scrutiny, not
external human peer review or formal verification.

#### Funding and competing interests.

No external funding or competing interests have been reported in the
materials supplied for this work. No institutional affiliation or
funding award is claimed. This reports the available record, not
independent verification of an anonymous creator’s circumstances.

#### Archive boundary.

The original submission contains internal file-hash bindings but omits
four historically cached external-source files and its original
packaging test suite. Those historical bytes and executions cannot be
reconstructed from that ZIP. Current source checking and any new
diagnostics are recorded separately; neither is a replacement for the
missing historical records.

<div class="thebibliography">

9

G. Amit, *Explicit upper bounds on the threshold of one-dimensional
long-range percolation*, arXiv:2610.11872v1 \[cond-mat.stat-mech\],
2026. <https://arxiv.org/abs/2610.11872v1>.

C. Borgs, J. T. Chayes, R. van der Hofstad, G. Slade, and J. Spencer,
*Random subgraphs of finite graphs. II. The lace expansion and the
triangle condition*, Annals of Probability **33** (2005), no. 5,
1886–1944.
[doi:10.1214/009117905000000260](https://doi.org/10.1214/009117905000000260).
arXiv:math/0401070.

M. Heydenreich, R. van der Hofstad, and A. Sakai, *Mean-field behavior
for long- and finite range Ising model, percolation and self-avoiding
walk*, Journal of Statistical Physics **132** (2008), no. 6, 1001–1049.
[doi:10.1007/s10955-008-9580-5](https://doi.org/10.1007/s10955-008-9580-5).
arXiv:0712.0312v2.

R. van der Hofstad and A. Sakai, *Critical points for spread-out
self-avoiding walk, percolation and the contact process above the upper
critical dimensions*, Probability Theory and Related Fields **132**
(2005), no. 3, 438–470.
[doi:10.1007/s00440-004-0405-4](https://doi.org/10.1007/s00440-004-0405-4).
arXiv:math/0402050v2.

Y. Liu, *High-dimensional long-range statistical mechanical models have
random walk correlation functions*, arXiv:2502.12104v3, 2025.
<https://arxiv.org/abs/2502.12104v3>.

</div>
