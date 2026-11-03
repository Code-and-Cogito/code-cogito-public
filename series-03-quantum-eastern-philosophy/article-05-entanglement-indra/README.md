# Article 05 — Quantum Entanglement vs Indra's Net

**Einstein wrote of "spooky actions at a distance." Huayan Buddhism described Indra's Net more than 1,300 years earlier.**

Using Python to simulate EPR correlations, run the CHSH form of the Bell inequality, and draw Indra's Net as a network model.

## Quick Start

```bash
pip install numpy matplotlib networkx
python entanglement_indra_analysis.py
```

The script writes the three PNG files below into the current directory. On a machine without a display, set the environment variable `MPLBACKEND=Agg` to skip the plot windows.

## Charts

- `epr_correlations.png` — EPR pair correlations: the quantum curve E(theta) = -cos(theta), simulated points, and an illustrative classical curve
- `bell_inequality_test.png` — CHSH parameter |S|: classical limit, computed quantum value, and three published measurements
- `indras_net_network.png` — Indra's Net: every jewel reflects every other (an illustrative 12-jewel graph)

## What the script prints (excerpt)

```
  Simulated points vs -cos(theta): max |deviation| = 0.058

  Key angles:
    theta=0:   E = -1.00 (perfect anti-correlation)
    theta=45:  E = -0.71
    theta=90:  E = +0.00 (no correlation)
    theta=135: E = +0.71
    theta=180: E = +1.00 (perfect correlation)

  Quantum prediction:   S = -2.8284, |S| = 2.8284
  Aspect (1982):        S = 2.697 +/- 0.015 (measured)
  Zeilinger (1998):     S ~ 2.73 +/- 0.02
  Micius 1200km (2017): S ~ 2.37 +/- 0.09

  Conclusion: Bell inequality VIOLATED (|S| = 2.8284 > 2)

  Illustrative model: complete graph of 12 jewels, 66 mutual reflections
```

The sign of S depends on the angle convention, so the script tests |S| > 2.

## About the numbers

Some of the numbers are computed, some are reported measurements, and some are illustrative. This table mirrors the "About the data" note at the end of the [article](https://code-cogito.com/en/quantum-entanglement-vs-indra-s-net-the-universe-as-an-indivisible-whole-en/#references).

| Item | What it is |
|------|------------|
| Red points in the EPR chart | **Simulated**, not experimental: 1,000 pairs per angle, 50 angles, seed 42. Alice's result is a fair 50/50 coin flip; Bob's result is drawn from the quantum joint probability for the angle difference. This reproduces the quantum statistics on a computer (a sampling shortcut). It is not a signal sent from Alice to Bob, and the points follow the quantum curve by construction |
| Quantum curve E(theta) = -cos(theta) and the quantum CHSH value | Computed from the formula. With a = 0, a' = 90, b = 45, b' = 135 degrees the script gets S = -2.8284, i.e. \|S\| = 2*sqrt(2) = 2.828 |
| Green dashed "classical" curve | **Illustrative**: a piecewise-linear shape drawn for teaching. It is not computed from a specific local hidden-variable model |
| Aspect S = 2.697 +/- 0.015 | Reported in Aspect, Grangier & Roger (1982), *Physical Review Letters* 49, 91 |
| Zeilinger S = 2.73 +/- 0.02 | Reported in Weihs et al. (Zeilinger group, 1998), *Physical Review Letters* 81, 5039 |
| Micius S = 2.37 +/- 0.09 | Reported in Yin et al. (Pan group, 2017), *Science* 356, 1140 |
| Indra's Net graph | **Illustrative**: 12 jewels, 66 mutual reflections. The net in the texts is infinite |
| Fazang's mirror room | Ten mirrors around a Buddha statue, lit by a single torch, as told in the *Song Gaoseng zhuan* (fascicle 5). The version with Empress Wu is a later, popular retelling |

## Files

| File | Description |
|------|-------------|
| `entanglement_indra_analysis.py` | Main script (EPR correlations + CHSH test + Indra's Net) |
| `epr_correlations.png` | Simulated EPR correlations vs the quantum curve |
| `bell_inequality_test.png` | CHSH parameter: classical limit, quantum value, measurements |
| `indras_net_network.png` | Indra's Net as a complete graph |

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-entanglement-vs-indra-s-net-the-universe-as-an-indivisible-whole-en/)
- [Chinese](https://code-cogito.com/quantum-entanglement-indras-net/)
- [Japanese](https://code-cogito.com/ja/quantum-entanglement-indras-net-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-05?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-05) for this article includes the complete code, CSV data files, Jupyter Notebook, and PDF cheatsheets.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-05) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
