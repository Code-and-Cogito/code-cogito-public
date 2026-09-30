# Article 04 — Perspective Projection

**The Magic of Vanishing Points: How Perspective Turned 2D Canvas into 3D Worlds**

Using Python to demonstrate the mathematics behind Renaissance perspective — from 3D-to-2D projection to a simple, illustrative picture of how spatial representation changed in art.

## Quick Start

```bash
pip install numpy matplotlib
python perspective_analysis.py
```

## What You'll Get

**Terminal output:**
- Projection scale at two depths (z = 5 and z = 10)
- The change in the illustrative depth score from the medieval icon to the Last Supper (15 → 95)

**Charts:**
- `perspective_cube_projection.png` — 3D cube projected onto 2D canvas with vanishing point
- `one_point_perspective.png` — One-point perspective: schematic drawing of lines converging to a single point
- `depth_comparison.png` — Illustrative spatial-quality scores: Medieval Icon vs Giotto vs Brunelleschi vs Last Supper

## Key Findings

The core math of perspective projection:
- **x' = (f * x) / z** — divide by depth = "closer means bigger"
- Doubling the distance halves the projected size: with f = 5 the scale f / z is 1.00 at z = 5 and 0.50 at z = 10
- In the author's illustrative scores, the depth score rises from 15 (medieval icon, 1200) to 95 (Last Supper, 1498). The scores are subjective judgements meant to show a trend, not measurements
- Brunelleschi's mirror experiment (c. 1413–1420; the exact date is not recorded) demonstrated perspective visually

## Notes on the Numbers

- The depth / proportion / spatial scores in `depth_comparison.png` are illustrative values assigned by the author, with no scoring rubric. Please label them as illustrative if you reuse the chart.
- The cube in the script is centred on the viewing axis (x and y from -1 to 1) so the vanishing point sits in the middle of the drawing. The article's snippet uses a cube from 0 to 1; the scale f / z depends only on z, so both give 1.00 at z = 5 and 0.50 at z = 10.
- `one_point_perspective.png` is a schematic drawing. The converging lines are drawn, not computed from a painting.

## Files

| File | Description |
|------|-------------|
| `perspective_analysis.py` | Main script (3D projection + one-point perspective sketch + illustrative depth comparison) |
| `perspective_cube_projection.png` | 3D cube projection chart |
| `one_point_perspective.png` | Converging lines demonstration (schematic) |
| `depth_comparison.png` | Medieval vs Renaissance spatial quality (illustrative scores) |

## Read the Full Article

- [English](https://code-cogito.com/en/perspective-math-changed-art-en/)
- [Chinese](https://code-cogito.com/perspective-math-changed-art/)
- [Japanese](https://code-cogito.com/ja/perspective-math-changed-art-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/renaissance-04?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=renaissance-04) includes:
- Projection matrix demo (4x4 perspective matrix in homogeneous coordinates, checked against simple f / z scaling) and a focal-length comparison
- Schematic one-, two- and three-point perspective diagrams
- Monte Carlo simulation of vanishing-point error on synthetic points
- Jupyter Notebook + a 20-row CSV data file (7 works, illustrative scores)

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=renaissance-04) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
