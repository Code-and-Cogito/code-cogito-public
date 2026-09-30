# Article 01 — Quantum Revolution: From Newton to Planck

**How a single equation shattered 200 years of deterministic physics.**

Using Python to visualize blackbody radiation, the photoelectric effect, and the collapse of Newtonian determinism.

## Quick Start

```bash
pip install numpy matplotlib scipy
python quantum_revolution_analysis.py
```

The script writes the three PNG files below into the current directory. On a machine without a display, set the environment variable `MPLBACKEND=Agg` to skip the plot windows.

## Charts

- `blackbody_radiation.png` — Blackbody radiation: classical vs quantum
- `photoelectric_effect.png` — Photoelectric effect: wave vs particle (electron counts are illustrative)
- `determinism_timeline.png` — Timeline of determinism's rise and fall (certainty scores are author-assigned)

## What the script prints (excerpt)

```
[Wien's Displacement Law]
  Temperature T = 5000 K
  Peak wavelength lambda_max = 579.6 nm

[Stefan-Boltzmann Law]
  Total radiated power proportional to T^4 = 3.54e+07 W/m2

Selected: Zinc (Zn)
Work function W0 = 4.31 eV
Cutoff wavelength lambda_0 = 287.7 nm

Wavelength(nm)   Photon E (eV)    Electron KE(eV)  Result
200              6.20             1.89             Electron ejected!
300              4.13             0.00             No ejection
400              3.10             0.00             No ejection
500              2.48             0.00             No ejection
```

## About the numbers

The script mixes textbook physics with a few author-chosen inputs, as described in the "About the data" note at the end of the [article](https://code-cogito.com/en/quantum-revolution-newton-universe-collapse-en/#references).

| Item | What it is |
|------|------------|
| Planck and Rayleigh-Jeans formulas; h, c, k, 1 eV | Textbook physics and CODATA constants (`scipy.constants`) |
| T = 5000 K | A round temperature close to the Sun's effective temperature (about 5,772 K, roughly 5,800 K). It is not the Sun's exact value |
| Work functions (Na 2.28, Al 4.08, Cu 4.70, Zn 4.31, Ag 4.73 eV) | Typical reference values; published values differ slightly by source and surface condition |
| Electron counts in the intensity panel | Illustrative: 100 electrons per unit of relative intensity, by construction |
| Certainty index in the timeline | The author's own narrative yardstick; subjective scores, not measurements of a physical quantity |
| Printed energies and wavelengths | Model outputs computed from the constants above, not historical experimental data |

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-revolution-newton-universe-collapse-en/)
- [Chinese](https://code-cogito.com/quantum-revolution-newton-universe-collapse/)
- [Japanese](https://code-cogito.com/ja/quantum-revolution-newton-universe-collapse-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-01?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-01) for this article includes the complete code, CSV data files, Jupyter Notebook, and PDF cheatsheets.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-01) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
