# Article 05 — Child Labour vs Algorithmic Bias

**The moral blind spots of two revolutions: exploiting children then, encoding bias now.**

Using Python to compare an illustrative reconstruction of nineteenth-century child labour with modern algorithmic bias, chart facial recognition error disparities, and draw parallels between two eras of unchecked technological progress.

## Quick Start

```bash
pip install numpy matplotlib
python child_labour_vs_bias_analysis.py
```

On a headless machine, set `MPLBACKEND=Agg` first. Running the script re-creates the three PNG files listed below in the current folder.

## What You'll Get

**Charts (saved by the script):**
- `child_labor.png` — Child labour rates by industry, 1800–1900 (hand-set illustrative reconstruction, not an official dataset)
- `facial_recognition_bias.png` — Facial recognition error rates by group (the 0.8% and 34.7% extremes are reported in the Gender Shades study; the two hatched bars are unverified secondary estimates)
- `historical_comparison.png` — Hand-set illustrative scores (0–10) comparing 1800s child labour with 2020s algorithmic bias

**Console output:** a short summary per chart, for example `Disparity ratio: 43x` (34.7% vs 0.8%) and `Peak of the average illustrative rate: 1830 (26.5%)`.

## About the data

- **Verified:** in the facial recognition chart, only the two extremes — 0.8% (white men) and 34.7% (Black women) — are figures reported by Buolamwini & Gebru (2018), "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification", *Proceedings of Machine Learning Research* 81. The ratio 34.7 / 0.8 is about 43. The study grouped subjects by skin type (Fitzpatrick scale), not by race; the group labels here follow the article's simplified wording.
- **Not verified:** the two middle values (7.1% and 12.0%) are widely repeated secondary estimates that could not be matched to the paper. They are drawn as hatched bars.
- **Illustrative, not an official dataset:** the child labour rates in `child_labor.png` and the 0–10 scores in `historical_comparison.png` are hand-set to demonstrate the mechanism. Do not quote them as historical statistics. The tables shown in the article's code block are illustrative reconstructions too, and are not the same numbers as this script's series. The 5% line in the facial recognition chart is only a reference line, not a standard.
- **Hypothetical scenarios:** the article's "fairness constraint" (92% / 85% ...) and "rebalanced training data" (0.8% → 1.2%) figures are hypothetical illustrations. They are not produced by the code in this folder.

## Files

| File | Description |
|------|-------------|
| `child_labour_vs_bias_analysis.py` | Main script (child labour + bias + comparison) |
| `child_labor.png` | Child labour trends (illustrative data) |
| `facial_recognition_bias.png` | Facial recognition bias chart |
| `historical_comparison.png` | Historical comparison (illustrative scores) |

## Read the Full Article

- [English](https://code-cogito.com/en/child-labor-vs-algorithmic-bias-en/)
- [Chinese](https://code-cogito.com/child-labor-vs-algorithmic-bias/)
- [Japanese](https://code-cogito.com/ja/child-labor-vs-algorithmic-bias-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/industrial-data-05?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=industrial-data-05) includes the complete Python script (about 690 lines; it saves 5 multi-panel figure files containing 12 sub-plots in total), a Jupyter Notebook, and the data file.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=industrial-data-05) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
