# Article 03 — Da Vinci's Vitruvian Man

**Da Vinci's Anatomical Revolution: Body Proportions and the Golden Ratio**

Using Python to model the Vitruvian Man's body proportions, and to show that the popular "golden-ratio navel" is a model assumption, not something Vitruvius or Leonardo wrote.

## Quick Start

```bash
pip install numpy matplotlib
python vitruvian_man_analysis.py
```

## What You'll Get

**Terminal output:**
- Body proportion table (in head-length units)
- Golden ratio check at the navel (it equals phi by construction, because the script places the navel at height / phi)
- Key findings summary

**Charts:**
- `vitruvian_man_basic.png` — Simplified Vitruvian Man: circle (navel center) + square (arm span = height). The navel height (height / phi, about 0.62 of the height above the soles) is a model assumption, labelled as such on the chart.

## Key Findings

Body-proportion rules used in the model (simple fractions of height, following Vitruvius; Leonardo's annotations change some numbers):
- **Height = 8 head-lengths** (head = 1/8 of height)
- **Face length and hand length = 1/10 of height** (0.8 head-lengths); **foot = 1/7 of height** (Vitruvius gives 1/6, Leonardo wrote 1/7)
- **Arm span = Height** (body fits in a square)
- **Circle centered on the navel** when arms and legs are spread

About the golden ratio:
- The script places the navel at height / phi (phi = 1.618...) above the soles. This is an assumption for illustration, not a measurement.
- So the navel ratio comes out as 1.618034 with an error of 0.000000 **by construction**. It recovers the input; it is not a verification.
- Neither Vitruvius nor Leonardo links the navel to the golden ratio. That idea became popular only from the 19th century on.

## Files

| File | Description |
|------|-------------|
| `vitruvian_man_analysis.py` | Main analysis script (proportions + golden-ratio check + visualization) |
| `vitruvian_man_basic.png` | Output chart |

## Read the Full Article

- [English](https://code-cogito.com/en/da-vinci-anatomy-revolution-en/)
- [Chinese](https://code-cogito.com/da-vinci-anatomy-revolution/)
- [Japanese](https://code-cogito.com/ja/da-vinci-anatomy-revolution-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-03?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-03) includes:
- 3D skeleton (joints and bones) model built with matplotlib
- Da Vinci vs Galen body-proportion comparison, with illustrative accuracy scores (author-set estimates for teaching, not measurements)
- Golden-ratio multi-segment analysis
- Accuracy timeline from antiquity to modern imaging (illustrative scores)
- 25-row proportion dataset (CSV)
- About 560 lines of commented Python + Jupyter Notebook, 5 charts (300 dpi PNG)
- English / Japanese / Chinese cheat sheets, Notion templates and getting-started guides

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-03) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
