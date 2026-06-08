#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifier + data generation for Part XXIII: extreme-omega kinetics.

Closed-form extrapolation (NOT prime data): idealizes a high-pressure centre N as
a subset of the first K=15 primes > 3 (the primorial pool reaching omega=15 at
S20). For a tuple B with dimension m_B and killer-prime set K_B (primes dividing a
member offset), the per-factor modifier is

    modifier_q = 0            if q in K_B   (absorbing state: q | N kills a member)
               = q/(q - m_B)  otherwise     (geometric enrichment).

The ensemble enrichment <E_B(omega)> is the exact average of the product of these
modifiers over all C(15,omega) factor subsets. This script:
  (1) tabulates <E_B(omega)> for twin/triplet/quad/quint,
  (2) locates the Event Horizon omega* (interior peak) and flags its existence,
  (3) confirms the twin primorial value x7.03 at omega=15,
  (4) writes data/enrichment_table.csv and data/event_horizons.csv.
Standard library only.
"""
import math, os, csv
from itertools import combinations

POOL = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59]
PATS = {"twin":(2,set()), "triplet":(3,{5}),
        "quadruplet":(4,{5,7}), "quintuplet":(5,{5,7,11})}

def E(m, K, omega):
    tot = 0.0; cnt = 0
    for S in combinations(POOL, omega):
        p = 1.0
        for q in S:
            p = 0.0 if q in K else p * q / (q - m)
        tot += p; cnt += 1
    return tot / cnt

def main():
    print("Exact ensemble enrichment <E_B(omega)> over the 15-prime primorial pool")
    print(" om | " + " ".join(f"{n:>10}" for n in PATS))
    curves = {n: [E(m,K,o) for o in range(1,16)] for n,(m,K) in PATS.items()}
    for i,om in enumerate(range(1,16)):
        print(f"  {om:<2} | " + " ".join(f"{curves[n][i]:>10.4f}" for n in PATS))

    print("\nEvent Horizon (interior peak) per tuple:")
    horizons = {}
    for n in PATS:
        v = curves[n]; peak = max(range(15), key=lambda i: v[i])
        interior = 0 < peak < 14
        horizons[n] = (peak+1, interior, v[peak])
        kind = f"omega*={peak+1}" if interior else f"boundary (omega={peak+1})"
        print(f"  {n:<11}: {kind:<22} peak<E>={v[peak]:.4f}  interior={interior}")
    print(f"\n  twin at omega=15 (full primorial product) = {curves['twin'][-1]:.4f}  [expected 7.030]")

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(os.path.dirname(here), "data"); os.makedirs(out, exist_ok=True)
    with open(os.path.join(out,"enrichment_table.csv"),"w",newline="") as f:
        w=csv.writer(f); w.writerow(["omega"]+list(PATS))
        for i,om in enumerate(range(1,16)):
            w.writerow([om]+[f"{curves[n][i]:.6f}" for n in PATS])
    with open(os.path.join(out,"event_horizons.csv"),"w",newline="") as f:
        w=csv.writer(f); w.writerow(["tuple","killer_primes","omega_star","interior_horizon","peak_E"])
        for n,(m,K) in PATS.items():
            os_, interior, pk = horizons[n]
            w.writerow([n, "{"+",".join(map(str,sorted(K)))+"}", os_, interior, f"{pk:.6f}"])
    print(f"\nwrote data/enrichment_table.csv, data/event_horizons.csv")

if __name__ == "__main__":
    main()
