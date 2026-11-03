# Article 09 — Quantum Consciousness and Eastern Philosophy

**Does consciousness collapse the wave function? Von Neumann, Penrose, and Wang Yangming all had something to say.**

Using Python to visualize quantum measurement models, Orch OR hypothesis, and Zen enlightenment as measurement metaphor.

## Quick Start

```bash
pip install numpy matplotlib
python quantum_consciousness_analysis.py
```

The script prints its summary and re-saves the three PNGs below in the current folder. On a machine without a display, run it as `MPLBACKEND=Agg python quantum_consciousness_analysis.py`.

## Charts

- `quantum_measurement_basic.png` — Quantum measurement and collapse (the von Neumann–Wigner reading)
- `orch_or_basic.png` — Penrose-Hameroff Orch OR concept sketch (schematic, not to scale)
- `zen_enlightenment_metaphor.png` — Zen enlightenment next to quantum collapse (a descriptive analogy, not an equivalence)

## What the Orch OR numbers mean

The script prints two very different timescales side by side, on purpose:

```
Simplified demo formula (NOT Penrose's E_G): tau = h-bar / (Delta_M * c^2)
Illustrative Delta_M = 1e-08 kg -> tau = 1.17e-43 s
Literature timescale (set from gamma rhythms): tau ~ 25 ms -> ~40 Hz
Gap: the demo value is ~10^41 times shorter than 25 ms;
```

- **~25 ms / ~40 Hz** is the timescale Orch OR proponents take from gamma-band brain rhythms; they then work backwards to how many tubulins would have to be in superposition (Hameroff & Penrose 2014, [doi:10.1016/j.plrev.2013.08.002](https://doi.org/10.1016/j.plrev.2013.08.002)). It is a set value, not something the script derives.
- **Penrose's own estimate** is tau ≈ ℏ/E_G, where E_G is the gravitational self-energy of the difference between the two superposed mass distributions (Penrose 1996, [doi:10.1007/BF02105068](https://doi.org/10.1007/BF02105068)).
- **The demo formula** tau = ℏ/(ΔM·c²) is only a simplified stand-in that shows the scaling idea (larger mass difference, faster collapse). ΔM = 10⁻⁸ kg is a hand-set illustrative input, not a measured brain value and not a number from Penrose's or Hameroff's papers. Because ΔM·c² is far larger than E_G, the result is more than 40 orders of magnitude shorter than 25 ms. The gap comes from the simplification, not from the theory.
- Orch OR is speculative and highly controversial. Penrose's 2020 Nobel Prize in Physics was for his black-hole work, not for Orch OR.
- Von Neumann himself did not explicitly claim that consciousness causes collapse; that reading comes mainly from later interpreters such as Wigner (Laudisa 2025, [arXiv:2508.15871](https://arxiv.org/abs/2508.15871)).

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-consciousness-eastern-philosophy-en/)
- [Chinese](https://code-cogito.com/quantum-consciousness-eastern-philosophy/)
- [Japanese](https://code-cogito.com/ja/quantum-consciousness-eastern-philosophy-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-09?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-09) for this article includes the complete code, the data files, Jupyter Notebook, and a PDF cheatsheet.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-09) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
