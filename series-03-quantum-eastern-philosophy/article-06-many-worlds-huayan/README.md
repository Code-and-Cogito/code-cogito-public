# Article 06 — Many-Worlds and Huayan Buddhism

**Everett's branching universes and the Huayan vision of mutually-containing worlds, explored with a toy branching model, a "parallel yous" calculation and a fractal analogy.**

Using Python to visualize a universe splitting tree, a count of parallel versions of "you", and a Sierpinski fractal as a picture for Huayan's "one contains all".

> **About the numbers.** Nothing in this script is measured data. The world counts (2^n, or 3 x 5 x 2 x 2 x 2 = 120) are plain arithmetic inside a **toy model** that counts every measurement or decision as one clean split; they are not physical predictions. The "~10^50 quantum events per second" line and the "35,000 decisions per day" figure are **hand-set, illustrative inputs** (the second is a widely repeated but poorly sourced pop-psychology number), and "2^35000, about 10^10536" is only what that assumption computes to. The Huayan / fractal comparisons are the author's **conceptual analogies**, not equivalences established in physics or Buddhist scholarship.

## Quick Start

```bash
pip install numpy matplotlib
python many_worlds_huayan_analysis.py
```

## What You'll Get

**Terminal output** (excerpt of what the script prints today):

```text
After n measurements: 2^n worlds (toy model: binary outcomes, one split per measurement)

Examples:
  * 10 measurements = 1,024 worlds
  * 20 measurements = 1,048,576 worlds
  * 30 measurements = 1,073,741,824 worlds
  * 100 measurements = 1.27e+30 worlds

Illustrative only: suppose ~10^50 quantum events happened per second
(an unsourced, hand-set figure, not a measured or published value)...

Example decisions (hand-set, illustrative):
  1. What to eat for breakfast? (3 choices)
  2. Which major in college? (5 choices)
  3. Accept this job offer? (2 choices)
  4. Confess your feelings? (2 choices)
  5. Move to a new city? (2 choices)

Result:
  * In this toy model these decisions create 120 parallel versions of 'you'

Illustrative extrapolation (assumptions, not measured statistics):
  * Assume 35,000 decisions per day (a widely repeated but poorly sourced pop-psychology figure)
  * Assume 2 options per decision (simplest hand-set choice)
  * One day in this model: 2^35000 worlds, about 10^10536

Sierpinski Triangle properties:
  * The plot draws order 5: 243 small triangles, a finite approximation
```

Things to keep in mind when you read these numbers:

- **2^n is a modelling choice.** Every measurement is treated as one binary split, so the counts follow from the assumption, not from experiment. The script says so in its printed text.
- **The example decisions are made up.** The five decisions and their option counts (3, 5, 2, 2, 2) are hand-set for illustration, not survey data.
- **"Analogy" means analogy.** The script prints the fractal and Many-Worlds comparisons with Huayan as a conceptual parallel (`~`), not as an established equivalence. The Sierpinski figure is a finite approximation (order 5) of a fractal that is only self-similar at every scale in the infinite limit.

## Charts

- `universe_splitting_tree.png` — universe branching at each measurement (toy model, 2^n)
- `parallel_yous.png` — parallel versions of "you" from five hand-set example decisions
- `huayan_fractal.png` — Sierpinski triangle (order 5) as a picture for Huayan's "one contains all"

## Files

| File | Description |
|------|-------------|
| `many_worlds_huayan_analysis.py` | Main script (branching tree + parallel "yous" + Sierpinski fractal) |
| `universe_splitting_tree.png` | Branching tree and exponential growth chart |
| `parallel_yous.png` | Life-decision tree and parallel-life count |
| `huayan_fractal.png` | Sierpinski fractal |

## Read the Full Article

- [English](https://code-cogito.com/en/many-worlds-interpretation-huayan-en/)
- [Chinese](https://code-cogito.com/many-worlds-interpretation-huayan/)
- [Japanese](https://code-cogito.com/ja/many-worlds-interpretation-huayan-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-06?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-06) for this article includes the complete code, the data files, a Jupyter Notebook, and PDF cheatsheets.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-06) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
