# Part XXIII — Phase Transition Kinetics and Topological Event Horizons at Extreme ω

*Volume II of the Arithmetic Geodynamics programme on the 6N skeleton.*

This paper returns to the **vertical** depth axis and models the extreme-ω "wind
tunnel" of Volume I as **phase-transition kinetics**. A high-pressure centre N is
idealized as a subset of the first 15 primes > 3 (the primorial pool reaching
ω=15 at S20). For a tuple B with dimension m_B and **killer-prime set** K_B (primes
dividing a member offset), the per-factor modifier is

> modifier_q = q/(q − m_B)  for non-killers,  and  **0** for q ∈ K_B (an *absorbing state*: q∣N kills a member).

Killer sets: triplet {5}, quadruplet {5,7}, quintuplet {5,7,11}. The ensemble
enrichment `⟨E_B(ω)⟩ = P(avoid all killers) × (geometric enrichment)` is evaluated
**exactly** over all C(15,ω) factor subsets.

### Results

| tuple | killers | ω\* (peak) | interior horizon? | peak ⟨E⟩ |
|---|---|---|---|---|
| twin | — | 15 (boundary) | no — monotone to **×7.03** | 7.0299 |
| triplet | {5} | **9** | yes | 1.7703 |
| quadruplet | {5,7} | **4** | yes | 1.1028 |
| quintuplet | {5,7,11} | 1 (boundary) | **no** — decays from ω=1 | 0.9880 |

- **Twin:** finite enrichment ×7.03 at ω=15 (diverges only as ω→∞).
- **Event Horizon is conditional.** An interior peak ω\* (where d⟨E⟩/dω = 0) exists
  **iff** the marginal log-enrichment is positive at ω=1. It holds for the triplet
  (ω\*=9) and quadruplet (ω\*=4) — peak then collapse to zero — but **not** for the
  quintuplet, whose three killers make ⟨E⟩ decline from ω=1. This corrects the
  naive "G↑, S↓ ⟹ unique peak" argument: monotonicity alone does not force an
  interior maximum.

The horizontal annihilation of Part XXI and this vertical collapse are distinct
axes; here the collapse is single-centre killer-prime absorption.

## Layout

```
.
├── paper/    Chen_6N_Paper23.{tex,pdf} + figure
├── figures/  fig_event_horizon.{pdf,png}
├── data/     enrichment_table.csv (⟨E_B(ω)⟩, ω=1..15) · event_horizons.csv (ω*, interior flag)
├── code/
│   ├── fig_event_horizon_make.py   # ⟨E_B(ω)⟩ curves + marginal-log-growth figure
│   └── verify_event_horizon.py     # exact enumeration; locates ω*; writes data/
├── CITATION.cff · .zenodo.json · LICENSE (MIT)
```

## Reproducing

```bash
pip install numpy matplotlib
python code/verify_event_horizon.py   # exact ⟨E_B(ω)⟩; ω* table; writes data/
python code/fig_event_horizon_make.py # regenerates the figure
```

Expected: twin ×7.0299 at ω=15; triplet ω\*=9, quad ω\*=4 (interior); quintuplet no
interior horizon.

## Scope

Closed-form extrapolation to ω=15 (N > 4.7×10¹⁸), far beyond any sieve, assuming
the local-factor multiplicativity validated only to ω≈5–6 persists. It is a
hypothesis-generating self-portrait of the model, **not** an observation of primes,
and claims no infinitude. Continues Part XXII (doi:10.5281/zenodo.20585074).

## License

MIT — see `LICENSE`.
