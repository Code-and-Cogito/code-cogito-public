# Article 08 — Entanglement and Dependent Origination

**Bell's theorem and the Twelve Links of Causality: non-locality meets interdependence.**

Using Python to draw the twelve links of dependent origination as a cycle, contrast a separable state with an entangled one, and compute the CHSH value S of Bell's inequality for an idealised entangled pair, next to the local hidden-variable limit and a rounded experimental reference value.

## Quick Start

```bash
pip install numpy matplotlib networkx
python entanglement_dependent_origination_analysis.py
```

## What You'll Get

**Terminal output:**
- The twelve links in words, with the traditional "break any link and the cycle ends" teaching
- Separable vs. entangled state (a schematic, no simulation)
- Bell (CHSH) values: local hidden-variable limit S <= 2.0, quantum prediction S = 2.828 (computed), experiment S ~ 2.7 (hard-coded, rounded reference value)

**Charts:**
- `twelve_links_basic.png` — Twelve links of dependent origination as a cycle
- `entangled_state_basic.png` — Separable vs. entangled state (schematic drawing)
- `bell_inequality_basic.png` — Three bars: local hidden-variable limit (2.0), quantum prediction (2.828), experiment (~2.7)

## Data Notes

| Item | Data status |
|------|-------------|
| Twelve links | The traditional list of twelve links; no data |
| Entangled-state figure | Schematic drawing of the singlet state (\|up,down> - \|down,up>)/sqrt(2); nothing is simulated |
| Local hidden-variable limit S <= 2 | A mathematical bound, not a measurement |
| Quantum prediction S = 2.828 | **Computed** in the script: idealised, noise-free correlation E = -cos(2*delta) with the standard textbook CHSH analyzer angles 0, 22.5, 45 and 67.5 degrees. The angles are illustrative settings, not those of a specific experiment. The result equals 2*sqrt(2), the quantum maximum |
| Experiment S ~ 2.7 | **Hard-coded**, rounded reference value for the early (1982) Aspect photon experiments. It is not produced by any simulation in this script. Real experiments report S with an uncertainty, so use the Aspect et al. (1982) papers listed in the article's references for exact figures |

## How to Read the Parallels

- Violating Bell's inequality rules out **local** hidden-variable theories. Non-local theories (for example Bohmian mechanics) are not excluded.
- The comparisons between quantum entanglement and dependent origination (no svabhava, relations before entities, Nagarjuna's "neither existence nor non-existence" and superposition) are conceptual analogies and philosophical readings. They are not physics results and not scientific equivalences.

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-entanglement-vs-buddhist-dependent-origination-nothing-exists-alone-en/)
- [Chinese](https://code-cogito.com/quantum-entanglement-dependent-origination/)
- [Japanese](https://code-cogito.com/ja/quantum-entanglement-dependent-origination-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-08?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-08) for this article includes the complete code (12 sub-plots), the CSV data files, a Jupyter Notebook, and PDF cheatsheets.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-08) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
