# Article 04 — Perspective Projection

**The Magic of Vanishing Points: How Perspective Turned 2D Canvas into 3D Worlds**

Using Python to demonstrate the mathematics behind Renaissance perspective — from 3D-to-2D projection to the evolution of spatial representation in art.

## Quick Start

```bash
pip install numpy matplotlib
python perspective_analysis.py
```

## What You'll Get

**Terminal output:**
- Projection scale comparison at different depths
- Depth improvement statistics (Medieval to Renaissance)
- Perspective type usage breakdown

**Charts:**
- `perspective_cube_projection.png` — 3D cube projected onto 2D canvas with vanishing point
- `one_point_perspective.png` — One-point perspective: all lines converge to a single point
- `depth_comparison.png` — Spatial quality scores: Medieval Icon vs Giotto vs Brunelleschi vs Da Vinci

## Key Findings

The core math of perspective projection:
- **x' = (f * x) / z** — divide by depth = "closer means bigger"
- Depth perception improved **533%** from Medieval (1200) to Da Vinci (1498)
- One-point perspective was the most common type (62% of Renaissance works)
- Brunelleschi's 1413 mirror experiment proved perspective mathematically

## Files

| File | Description |
|------|-------------|
| `perspective_analysis.py` | Main script (3D projection + one-point perspective + depth comparison) |
| `perspective_cube_projection.png` | 3D cube projection chart |
| `one_point_perspective.png` | Converging lines demonstration |
| `depth_comparison.png` | Medieval vs Renaissance spatial quality |

## Read the Full Article

- [English](https://code-cogito.com/en/perspective-math-changed-art-en/)
- [Chinese](https://code-cogito.com/perspective-math-changed-art/)
- [Japanese](https://code-cogito.com/ja/perspective-math-changed-art-ja/)

## Want More?

The [Deep Dive Pack](https://code-cogito.com/products/) includes:
- Two-point and three-point perspective visualizations
- 100-painting dataset analysis
- Vanishing point auto-detection algorithm
- Projection matrix derivation
- Jupyter Notebook + full dataset

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
