# Article 02 — Copenhagen Interpretation vs Kyoto School

**Bohr's complementarity and Zen Buddhism echo each other — a parallel this series explores as interpretation, not as physics.**

Using Python to draw a toy double-slit model, compare the observed and unobserved patterns, and set the taijitu beside a schematic of Bohr's complementarity. The curves are hand-set illustrative models, not measurements or a physical simulation (see [About the Data](#about-the-data)).

## Quick Start

```bash
pip install numpy matplotlib
python copenhagen_kyoto_analysis.py
```

## What You'll Get

**Terminal output:**
- The toy-model inputs: slits at -1.0 and +1.0, wavelength 0.5, peak width 0.5 (all hand-set)
- `Left panel:  40 evenly spaced interference peaks` and `Right panel: 2 peaks (one per slit), no interference` — the counts are computed from the curves
- The taijitu and motto lines, a short list of interpretive mappings, and a closing list of Copenhagen–Kyoto parallels (labelled as this series' framing)

**Charts:**
- `double_slit_observer_effect.png` — Toy double-slit model: unobserved (interference peaks) vs observed (two peaks)
- `taiji_complementarity.png` — Taijitu (Ming-dynasty form) beside a schematic wave/particle diagram
- `observer_effect_comparison.png` — Toy comparison of "without observer" and "with observer" curves

## About the Data

- **Illustrative inputs:** slit positions, wavelength and peak widths are hand-set to draw the charts. Nothing here is measured data or a physical simulation. The interference curve leaves out the broad single-slit envelope of a real pattern, and the two-peak curve is a schematic, not a computed which-path distribution. The y-axes are normalised (peak = 1), not photon counts.
- **"Observation":** in the double-slit panels it means a measurement that records which slit was used, not a conscious observer.
- **Real-world facts in the comments and printed text:**
  - Bohr received Denmark's Order of the Elephant in 1947, and his coat of arms carries a taijitu with the motto *Contraria sunt complementa* (Wikipedia, "[Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr)"). The script draws the symbol itself; it is not a copy of the coat-of-arms artwork.
  - The swirl-and-dots form drawn here is the Ming-dynasty taijitu (Zhao Huiqian, 1370s; dotted standard form by Lai Zhide, 1525–1604). Zhou Dunyi's 11th-century diagram is a different design (Wikipedia, "[Taijitu](https://en.wikipedia.org/wiki/Taijitu)").
  - Complementarity: N. Bohr, "The Quantum Postulate and the Recent Development of Atomic Theory", *Nature* 121 (1928), 580–590, based on his 1927 Como lecture.
  - The flag-and-wind story of Huineng comes from the *Platform Sutra*.
- **Interpretive parallels:** the mappings between Copenhagen ideas and Kyoto/Zen ideas (and the yin-yang to |0>, |1> mapping) are this series' framing, not scientific findings. That the taijitu "precisely expresses" the mathematical structure of complementarity is the article's reading, not something Bohr said.
- **The article's opening scene** ("An Afternoon in Copenhagen") is fictional: no record of a meeting between Bohr and D. T. Suzuki has been found.

## Read the Full Article

- [English](https://code-cogito.com/en/copenhagen-interpretation-vs-kyoto-school-en/)
- [Chinese](https://code-cogito.com/copenhagen-interpretation-vs-kyoto-school/)
- [Japanese](https://code-cogito.com/ja/copenhagen-interpretation-vs-kyoto-school-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-02?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-02) for this article includes the complete code, CSV data files, a Jupyter Notebook, and PDF cheatsheets (EN/ZH/JA).

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-02) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
