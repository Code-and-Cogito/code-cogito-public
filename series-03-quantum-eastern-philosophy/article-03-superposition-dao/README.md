# Article 03 — Quantum Superposition and Taoism

**Schrödinger's cat and Zhuangzi's butterfly dream: a thought experiment and a parable about the nature of reality.**

Using Python to visualize a simplified Schrödinger's cat model, a taiji (yin-yang) drawing for the Taoist idea of you/wu (being/non-being), and a two-state "butterfly dream" illustration, with quantum superposition as the common thread.

## Quick Start

```bash
pip install numpy matplotlib
python superposition_dao_analysis.py
```

On a headless machine, set `MPLBACKEND=Agg` first. Running the script re-creates the three PNG files listed below in the current folder.

## What You'll Get

**Charts (saved by the script):**
- `schrodinger_cat_basic.png` — Probability that the cat is alive or dead over three hours, for an atom with an illustrative 1-hour half-life (idealised model, no decoherence)
- `butterfly_dream_basic.png` — Zhuangzi's butterfly dream as a two-state illustration: equal 50/50 weights before "waking", one outcome after
- `taiji_you_wu_basic.png` — A schematic taiji: Yang (Being) in white, Yin (Non-being) in black, with the quantum parallel written underneath

**Console output:** the three sections above, including a simulated box-opening for each of three sample times (100 trials each, fixed random seed 42, so the counts are the same on every run):

```
t = 0.5h | Theory: P(alive)=70.71%, P(dead)=29.29%
         | Experiment (100 trials): alive=71, dead=29
t = 1.0h | Theory: P(alive)=50.00%, P(dead)=50.00%
         | Experiment (100 trials): alive=49, dead=51
t = 2.0h | Theory: P(alive)=25.00%, P(dead)=75.00%
         | Experiment (100 trials): alive=24, dead=76
```

## About the data

- **Nothing here is measured data.** Every input is a hand-set illustrative value: the 1-hour half-life (the usual textbook telling of the cat thought experiment, a modelling choice), the three sample times, the 100 trials per time, and the equal 50/50 weights in the butterfly panel.
- **Analogies, not physics:** the mappings between Daoist ideas and quantum states (Yang = Being, Yin = Non-being, Zhuangzi and butterfly as two basis states) are illustrative analogies drawn in the article. The "genuinely both dead and alive" reading of the cat is the Copenhagen interpretation, which the article follows.
- **Quotations:** the two Dao De Jing lines are printed in English translation (chapter 1 and chapter 2). The butterfly-dream question is a paraphrase of the Qiwulun chapter of the Zhuangzi, which does not date the dream.
- **Not in this folder:** the article's decoherence simulation. Its inputs are illustrative too: an electron coherence time of 10^10 seconds (about 300 years) and a cat coherence time of 10^-40 seconds are values chosen to show the size of the gap, not measurements, and the decoherence rate is simply the number of particles divided by 10^9.

## Files

| File | Description |
|------|-------------|
| `superposition_dao_analysis.py` | Main script (cat model + taiji + butterfly dream) |
| `schrodinger_cat_basic.png` | Cat probabilities over time (illustrative model) |
| `taiji_you_wu_basic.png` | Taiji: Being and Non-being |
| `butterfly_dream_basic.png` | Butterfly dream as a two-state illustration |

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-superposition-taoism-dao-en/)
- [Chinese](https://code-cogito.com/quantum-superposition-taoism-dao/)
- [Japanese](https://code-cogito.com/ja/quantum-superposition-taoism-dao-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-03?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-03) includes the complete Python script (4 multi-panel figure files with 12 sub-plots, including the decoherence timescale comparison), a Jupyter Notebook, 6 CSV data files, and PDF cheatsheets in English, Traditional Chinese and Japanese.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-03) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
