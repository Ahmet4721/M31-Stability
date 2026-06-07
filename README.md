# A Unified Stability Chain for M31
### Inner Kinematic Braking, Bar–Spiral Resonance Locking, and Secular Equilibrium

**Ahmet Keske** — Independent Researcher, Mardin, Türkiye  
ORCID: [0009-0000-2288-6680](https://orcid.org/0009-0000-2288-6680)  
E-mail: ahmetkeske45@gmail.com

[![Zenodo](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.18074218-blue)](https://doi.org/10.5281/zenodo.18074218)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This repository contains all simulation and figure-generation code underlying the paper:

> **Keske, A. (2026).** *A Unified Stability Chain for M31: Inner Kinematic Braking, Bar–Spiral Resonance Locking, and Secular Equilibrium.* Zenodo. https://doi.org/10.5281/zenodo.18074218

We present a unified dynamical framework for the long-term secular stability of the Andromeda Galaxy (M31), built around a radius-dependent **Unified Stability Chain**:

1. **Inner Braking** — high-dispersion bulge (σ_R > 120 km/s) suppresses bar-driven instabilities
2. **Resonance Locking** — bar OLR overlaps spiral CR at R ≈ 9 kpc, enabling regulated angular momentum transfer
3. **Outer Kinematic Support** — maintains coherence in the ~10 kpc star-forming ring

High-resolution tracer simulations (N = 10⁵, RK4, bar + spiral perturbations) demonstrate that the ring survives entirely via orbital resonance trapping over 1.2 Gyr.

---

## Repository Structure

```
M31-Stability/
├── README.md
│
├── simulation/
│   ├── M31_v8.6_resonance_locking.py   # Main simulation (v8.6, RK4, bar+spiral)
│   ├── tracer_simulation.py            # Original tracer simulation
│   └── M31_rebound_v3.py              # REBOUND N-body test
│
├── figures/
│   ├── generate_figures.py             # Fig 1–3 (sigma_R, Q_eff, torque)
│   ├── generate_fig4_v86.py           # Fig 4 (v8.6 simulation output)
│   ├── fig1_profiles.pdf
│   ├── fig2_resonance.pdf
│   ├── fig3_torque.pdf
│   └── fig4_tracers_v86.pdf
│
├── paper/
│   └── main_final.tex                  # MNRAS LaTeX manuscript
│
└── LICENSE
```

---

## Key Results

| Quantity | Value |
|----------|-------|
| Bar pattern speed | Ω_b = 42 ± 5 km/s/kpc |
| Bar OLR radius | R_OLR ≈ 8.95 kpc |
| Spiral CR radius | R_CR ≈ 9 kpc |
| Resonance width | ΔR_res ≈ 2.3 kpc |
| Effective stability | Q_eff ≈ 1.1–1.5 |
| Simulation duration | 1.2 Gyr (RK4, dt = 0.002 Gyr) |
| Tracer particles | N = 10⁵ |

---

## Simulation Details

### v8.6 — Main Simulation (Bar + Spiral Resonance Locking)

The primary simulation uses:

- **Background potential:** Plummer bulge + Miyamoto–Nagai disc + pseudo-isothermal halo
- **Bar perturbation:** Rigid analytical bar, Ω_b = 31.4 km/s/kpc
- **Spiral perturbation:** m=2 logarithmic spiral, Ω_s = 12.0 km/s/kpc
- **Integrator:** Vectorised 4th-order Runge–Kutta (RK4), Δt = 0.002 Gyr
- **Tracers:** N = 10⁵ massless kinematic test particles
- **Self-gravity:** Intentionally neglected (first-order consistency test)

### Observational Predictions

| Instrument | Prediction |
|-----------|-----------|
| **Gaia DR4** | Radial-velocity anomaly ~15 km/s at R ≈ 9 kpc |
| **JWST/NIRSpec** | Dispersion floor σ_R > 75 km/s for R ≲ 3 kpc |

---

## Requirements

```
python >= 3.8
numpy
matplotlib
scipy
```

Install:
```bash
pip install numpy matplotlib scipy
```

For REBOUND simulations (optional):
```bash
pip install rebound
```

---

## Usage

### Generate publication figures (Fig 1–3)

```bash
python figures/generate_figures.py
```

Outputs: `fig1_profiles.pdf`, `fig2_resonance.pdf`, `fig3_torque.pdf`

### Run main simulation and generate Fig 4

```bash
python figures/generate_fig4_v86.py
```

Output: `fig4_tracers_v86.pdf`

> **Note:** N = 10⁵ simulation takes ~100 seconds on a modern CPU.
> For faster testing, reduce N to 10,000 in the script.

### Run on Google Colab

```python
!pip install numpy matplotlib
# Upload generate_fig4_v86.py and run
```

---

## Limitations

The simulations adopt a **rigid background potential** and neglect:
- Self-gravity of tracer particles
- Hydrodynamical effects
- Gas–star coupling
- Live dark matter halo evolution

These simplifications provide a clean, first-order consistency test of orbital coherence. Fully self-consistent N-body simulations are planned for future work.

---

## Future Work (Paper II)

A comparative study across barred spirals (NGC 4321, M81, M51) is planned to test whether the Unified Stability Chain is a generic feature of massive barred spirals, and to investigate the inner–outer velocity dichotomy in the context of angular momentum redistribution.

---

## Citation

If you use this code or results, please cite:

```bibtex
@misc{Keske2026,
  author    = {Keske, Ahmet},
  title     = {A Unified Stability Chain for M31: Inner Kinematic
               Braking, Bar--Spiral Resonance Locking, and
               Secular Equilibrium},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.18074218},
  url       = {https://doi.org/10.5281/zenodo.18074218}
}
```

---

## References

- Athanassoula E., 2003, MNRAS, 341, 1179
- Blaña Díaz M., et al., 2018, MNRAS, 481, 3210
- Dorman C. E., et al., 2015, ApJ, 803, 24
- Feng Z.-X., et al., 2024, ApJ, 963, 22
- Minchev I., Famaey B., 2010, ApJ, 722, 112
- Monari G., et al., 2014, A&A, 569, A69
- Romeo A. B., Wiegert J., 2011, MNRAS, 416, 1191
- Saglia R. P., et al., 2018, A&A, 618, A156
- Sellwood J. A., 2014, Rev. Mod. Phys., 86, 1
- Toomre A., 1964, ApJ, 139, 1217
- Widrow L. M., et al., 2003, ApJ, 588, 311
- Zhang X., et al., 2024, MNRAS, 528, 2653

---

## License

MIT License — see [LICENSE](LICENSE) for details.
