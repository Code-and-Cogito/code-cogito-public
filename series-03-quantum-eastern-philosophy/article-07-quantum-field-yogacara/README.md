# Article 07 — Quantum Field Theory and Yogacara Buddhism

**The quantum vacuum is not empty; the alaya-vijnana stores all seeds. A philosophical analogy between two very different traditions, drawn with Python.**

Using Python to visualize a toy picture of quantum field excitations, virtual particle-antiparticle pairs, and the Yogacara eight consciousnesses model.

> **About the numbers.** Nothing in this script is measured data. The wave packets, the number of virtual-pair events, their energies and lifetimes, and the 30 "seeds" in the diagram are **hand-set, illustrative toy inputs** in arbitrary units, chosen to draw a picture; they are not derived from quantum field theory or taken from experiments. The only real-world facts the script prints are historical: the Casimir effect was **predicted in 1948** (H. B. G. Casimir) and **first measured with good precision in 1997** (S. K. Lamoreaux). The "≈" lines comparing quantum field theory with Yogacara are the author's **philosophical analogies**, not equivalences established in physics or Buddhist scholarship. The one-line summary "Particles are just field excitations" is a plain statement of the field-theory picture; it is **not** a quotation from Feynman's 1965 Nobel lecture.

## Quick Start

```bash
pip install numpy matplotlib
python quantum_field_yogacara_analysis.py
```

The script saves three PNG files to the current directory and also calls `plt.show()`, so run it in an environment that can open plot windows (or set `MPLBACKEND=Agg` to skip the windows).

## What You'll Get

**Terminal output** (excerpt of what the script prints today):

```text
[Visualization 1] Quantum Field: Particle as Excitation
  (Illustrative toy wave packets: amplitudes and widths are hand-set)

[Visualization 2] Vacuum Fluctuations - Virtual Particles
  BUT: Virtual particles constantly pop in and out
  (Toy picture: event counts and lifetimes are hand-set, arbitrary units)

  Casimir effect (predicted 1948, experimentally confirmed 1997):
  Two metal plates attract even in vacuum
  Predicted by H. Casimir (1948); first precise measurement by S. K. Lamoreaux (1997)

[Visualization 3] Eight Consciousnesses (Yogacara Buddhism)
  PARALLEL to quantum field (the author's analogy, not an established equivalence):
  Alaya ≈ Quantum vacuum (both contain potential)
  Seeds ≈ Virtual particles (both can manifest)
  Manifestation ≈ Field excitation (both create reality)

[Key Points]
  - QFT: 'Particles are just field excitations'
  - Yogacara: 'All phenomena are consciousness manifestations'
  - Analogies drawn by the author (philosophical, not established equivalences):
    Field ≈ Alaya consciousness (both fundamental)
    Particles ≈ Manifested dharmas (both temporary)
    Vacuum not empty ≈ Alaya contains seeds
    Virtual particles ≈ Karmic seeds manifesting
```

Things to keep in mind when you read the charts and the output:

- **The plots are conceptual sketches.** The two wave packets, the random virtual pairs (fixed seed, so the picture is reproducible) and the eight-consciousnesses circles show an idea; the numbers on them carry no physical or textual meaning.
- **The dated facts are historical.** Casimir predicted the effect in 1948; Lamoreaux's 1997 experiment was the first precise measurement (see Sources).
- **"≈" means analogy.** The correspondences between the vacuum and the alaya-vijnana, or between virtual particles and karmic seeds, are a way of thinking, not a proven correspondence.
- **Windows consoles.** The output contains "≈"; if you redirect it to a file on a Windows console with a legacy code page, run Python with `PYTHONIOENCODING=utf-8`.

## Charts

- `quantum_field_basic.png` — toy wave packets: vacuum vs. excited field (illustrative amplitudes)
- `vacuum_fluctuations_basic.png` — toy picture of virtual particle-antiparticle pairs (hand-set energies and lifetimes)
- `eight_consciousnesses_basic.png` — simplified Yogacara eight consciousnesses diagram (illustrative layout; the gold dots are decorative)

## Files

| File | Description |
|------|-------------|
| `quantum_field_yogacara_analysis.py` | Main script (field excitation + virtual pairs + eight consciousnesses) |
| `quantum_field_basic.png` | Field excitation chart |
| `vacuum_fluctuations_basic.png` | Virtual particle-antiparticle chart |
| `eight_consciousnesses_basic.png` | Eight consciousnesses diagram |

## Sources

- Casimir, H. B. G. (1948). "On the Attraction Between Two Perfectly Conducting Plates". *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen*, 51, 793-795.
- Lamoreaux, S. K. (1997). "Demonstration of the Casimir Force in the 0.6 to 6 μm Range". *Physical Review Letters*, 78(1), 5-8. doi:10.1103/PhysRevLett.78.5
- Feynman, R. P. (1965). ["The Development of the Space-Time View of Quantum Electrodynamics"](https://www.nobelprize.org/prizes/physics/1965/feynman/lecture/) (Nobel Lecture, December 11, 1965). The article explains why the "field excitations" sentence is not taken from this lecture.

## Read the Full Article

- [English](https://code-cogito.com/en/quantum-field-theory-yogacara-en/)
- [Chinese](https://code-cogito.com/quantum-field-theory-yogacara/)
- [Japanese](https://code-cogito.com/ja/quantum-field-theory-yogacara-ja/)

## Want More?

The [Deep Dive Pack](https://codecogito.gumroad.com/l/quantum-eastern-07?utm_source=github&utm_medium=readme&utm_campaign=article_pack&utm_content=quantum-eastern-07) for this article includes the complete code, six CSV data files, a Jupyter Notebook, and PDF cheatsheets in three languages.

New to this kind of analysis? The free [Starter Notebook](https://codecogito.gumroad.com/l/starter-notebook?utm_source=github&utm_medium=readme&utm_campaign=starter&utm_content=quantum-eastern-07) takes one real dataset (Maddison Project GDP, 1500–2022) from download to three figures in about 30 minutes.

---

**Code & Cogito** — [code-cogito.com](https://code-cogito.com)
