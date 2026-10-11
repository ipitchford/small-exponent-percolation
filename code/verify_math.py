"""Finite exact diagnostics. These do not prove the analytic percolation theorem."""
import json
from fractions import Fraction as F

checks = 0
negative_controls = 0

def require(condition, label):
    global checks
    if not condition:
        raise RuntimeError(label)
    checks += 1

def reject(condition, label):
    global negative_controls
    try:
        require(condition, label)
    except RuntimeError:
        negative_controls += 1
    else:
        raise RuntimeError("Negative control was not rejected: " + label)

D = {-2:F(1,4), -1:F(1,4), 1:F(1,4), 2:F(1,4)}
require(sum(D.values()) == 1, "probability normalization")
require(all(D[x] == D[-x] for x in D), "even kernel")
S2 = sum(v*v for v in D.values())
S3 = sum(v**3 for v in D.values())
return3 = sum(a*b*D.get(-x-y, 0) for x,a in D.items() for y,b in D.items())
reject(S3 == return3, "pointwise cube is not three-step return")
reject(sum(v/2 for v in D.values()) == 1, "missing two-sided normalization")
for p in (F(1,2), F(1), F(3,2), F(2)):
    lhs = sum(p*v/(1+p*v) for v in D.values())
    T3 = sum(v**3/(1+p*v) for v in D.values())
    require(lhs == p-p*p*S2+p**3*T3, "nonbacktracking exact expansion")
    require(2*p-p*p == 1-(p-1)**2, "quadratic identity")
    require(2*p-p*p <= 1, "quadratic upper bound")
    reject(lhs == p-p*p*S2, "discarded exact cubic term")
for q in (F(1,7), F(1,3), F(2,3)):
    r = F(2,5)
    t = q+(1-q)*r
    require(q*(t-r) == q*q*(1-r), "deleted-bond identity")
    require(q*r == q*t-q*q+q*q*r, "subtraction and remainder")
    reject(q*r == q*t-q*q, "deleted-bond remainder cannot be discarded")
c1,c2,w = F(1),F(3),F(1,2)
mean = w*c1+(1-w)*c2
pair = w*w*c1*c1+2*w*(1-w)*c1*c2+(1-w)**2*c2*c2
require(pair == mean**2, "mixture pair moment")
reject(pair == w*c1*c1+(1-w)*c2*c2, "mean square is not square mean")
for lam in (F(0),F(1,2),F(2)):
    require((2*lam+lam*lam)/2 == lam+lam*lam/2, "local addition coefficient")
require(S3 <= max(D.values())*S2, "pointwise third moment bound")
require(negative_controls == 10, "negative-control count")
print(json.dumps({"passed":checks,"negative_controls_rejected":negative_controls,
                  "scope":"Finite exact algebra only; not an analytic theorem replay"}, sort_keys=True))
