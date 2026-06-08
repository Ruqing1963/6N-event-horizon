#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figure for Part XXIII: ensemble enrichment <E_B(omega)> and the Event Horizon."""
import math, numpy as np
from itertools import combinations
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt

POOL=[5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
PATS={'twin':(2,set(),"#1f4e79","o"),'triplet':(3,{5},"#b4341f","s"),
      'quadruplet':(4,{5,7},"#2e7d32","^"),'quintuplet':(5,{5,7,11},"#6a1b9a","D")}
def E(m,K,om):
    tot=0.0; cnt=0
    for S in combinations(POOL,om):
        p=1.0
        for q in S: p = 0.0 if q in K else p*q/(q-m)
        tot+=p; cnt+=1
    return tot/cnt
oms=list(range(1,16))
curves={n:[E(m,K,o) for o in oms] for n,(m,K,c,mk) in PATS.items()}

fig,ax=plt.subplots(1,2,figsize=(13.5,5.4))
fig.suptitle("Extreme-$\\omega$ kinetics (closed-form extrapolation, not prime data): "
             "twin enriches to $\\times7.03$; cross-centre tuples peak then collapse",
             fontsize=12, fontweight="bold")
a=ax[0]
for n,(m,K,c,mk) in PATS.items():
    a.plot(oms,curves[n],mk+"-",c=c,ms=5,lw=1,label=n)
a.axhline(1,color="k",ls="--",lw=.8)
# mark interior event horizons
for n,star in (("triplet",9),("quadruplet",4)):
    a.axvline(star,color=PATS[n][2],ls=":",lw=.9)
    a.annotate(f"$\\omega^\\star={star}$",(star,max(curves[n])),color=PATS[n][2],
               fontsize=8,xytext=(star+0.2,max(curves[n])+0.15))
a.annotate("twin: $\\times7.03$ at $\\omega=15$\n(diverges only as $\\omega\\to\\infty$)",
           (15,7.03),fontsize=8,ha="right",va="top",color="#1f4e79")
a.annotate("quintuplet: no interior\nhorizon (3 killers)",(1,0.99),fontsize=8,
           color="#6a1b9a",xytext=(2.5,0.55),
           arrowprops=dict(arrowstyle="->",color="#6a1b9a",lw=.8))
a.set_xlabel(r"$\omega$ (prime factors $>3$ of centre $N$)")
a.set_ylabel(r"ensemble enrichment $\langle E_B(\omega)\rangle$")
a.set_title("(A) enrichment vs pressure; $\\omega^\\star$ = Event Horizon")
a.set_yscale("log"); a.legend(fontsize=8); a.grid(alpha=.3,which="both")

# panel B: discrete d ln E / d omega -> zero crossing = horizon
b=ax[1]
for n,(m,K,c,mk) in PATS.items():
    if n=="twin": continue
    v=curves[n]; dln=[ (math.log(v[i+1])-math.log(v[i])) if v[i+1]>0 and v[i]>0 else np.nan
                       for i in range(len(v)-1)]
    b.plot([o+0.5 for o in oms[:-1]], dln, mk+"-", c=c, ms=4, lw=1, label=n)
b.axhline(0,color="k",ls="--",lw=.8)
b.set_xlabel(r"$\omega$"); b.set_ylabel(r"$\Delta\ln\langle E_B\rangle$ (marginal log-growth)")
b.set_title("(B) horizon = sign change; quintuplet never positive")
b.legend(fontsize=8); b.grid(alpha=.3)
fig.tight_layout(rect=[0,0,1,0.93])
fig.savefig("fig_event_horizon.png",dpi=200); fig.savefig("fig_event_horizon.pdf")
print("wrote fig_event_horizon.{png,pdf}")
print("twin omega=15:",round(curves['twin'][-1],4),
      "| triplet peak om*=9:",round(max(curves['triplet']),4),
      "| quad peak om*=4:",round(max(curves['quadruplet']),4))
