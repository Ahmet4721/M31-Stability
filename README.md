# M31-Stability

**A Unified Stability Chain for M31: Inner Kinematic Braking, Bar–Spiral Resonance Locking, and Secular Equilibrium**

This repository contains the simulation code, analytical calculations, and figure-generation scripts accompanying the study:

> **Keske, A. (2026)**  
> *A Unified Stability Chain for M31: Inner Kinematic Braking, Bar–Spiral Resonance Locking, and Secular Equilibrium*

---

## Overview

This project investigates the long-term dynamical stability of the Andromeda Galaxy (M31) through a unified framework connecting:

1. **Inner Kinematic Braking**
   - Elevated central velocity dispersion suppresses large-scale dynamical instabilities.

2. **Bar–Spiral Resonance Locking**
   - The bar Outer Lindblad Resonance (OLR) overlaps the spiral Corotation Radius (CR) near 9 kpc.

3. **Outer Ring Coherence**
   - Resonant coupling may help maintain the observed star-forming ring.

The framework combines analytical stability arguments, resonance theory, angular momentum transport, and tracer-particle simulations.

---

## Scientific Goals

This repository explores whether:

- High inner velocity dispersion contributes to disk stability.
- Resonance overlap between bar and spiral structures produces a dynamically preferred configuration.
- Orbital resonance trapping can maintain ring coherence over gigayear timescales.
- Observable signatures of resonance locking exist in M31.

---

## Features

### Analytical Components

- Velocity dispersion model
- Effective Toomre stability parameter (`Q_eff`)
- Resonance-locking criterion
- Angular momentum flux density formalism
- Sensitivity analysis for pattern speed and velocity dispersion

### Numerical Components

- Tracer particle simulations
- Analytical bar perturbation model
- Logarithmic spiral perturbation model
- Fourth-order Runge–Kutta integration
- Orbital coherence diagnostics

### Visualization

Generation of:

- Velocity dispersion profiles
- `Q_eff` stability maps
- Resonance overlap diagrams
- Torque balance plots
- Orbital evolution figures

---

## Repository Structure

```text
M31-Stability/
│
├── simulations/
│   ├── tracer_simulation.py
│   ├── potentials.py
│   └── integrator.py
│
├── analysis/
│   ├── stability.py
│   ├── resonance.py
│   └── torque_balance.py
│
├── figures/
│   ├── figure1_dispersion_Qeff.py
│   ├── figure2_resonance.py
│   ├── figure3_torque.py
│   └── figure4_orbits.py
│
├── data/
│   └── observational_profiles/
│
├── paper/
│   └── manuscript.tex
│
├── LICENSE
├── README.md
│
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ahmet4721/M31-Stability.git

cd M31-Stability
```

Install required packages:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install numpy scipy matplotlib pandas astropy
```

---

## Running the Simulation

Example:

```bash
python simulations/tracer_simulation.py
```

Default configuration:

```text
Particles        : 100,000
Integration Time : 1.2 Gyr
Integrator       : RK4
Bar Perturbation : Enabled
Spiral Pattern   : Enabled
```

Outputs are written to:

```text
output/
```

---

## Important Limitations

This project uses **massless tracer particles** evolving in a **rigid background potential**.

The simulations:

- investigate orbital coherence
- explore resonance-supported structures
- provide a proof-of-concept for resonance trapping

The simulations do **not**:

- include self-gravity
- model gas dynamics
- reproduce full disk evolution
- constitute a fully self-consistent N-body model

Consequently, results should be interpreted as a first-order dynamical consistency test rather than a definitive demonstration of galactic stability.

---

## Main Predictions

### Gaia DR4

A possible radial-velocity anomaly near:

```text
R ≈ 9 kpc
v_rad ≈ 15 km s⁻¹
```

associated with resonance locking.

### JWST / NIRSpec

A minimum inner velocity dispersion:

```text
σ_R > 75 km s⁻¹
```

required to maintain marginal stability.

---

## Data Sources

The analysis uses publicly available observational data compiled from:

- Saglia et al. (2018)
- Dorman et al. (2015)
- Widrow, Perrett & Suyu (2003)
- Blaña Díaz et al. (2018)
- Zhang et al. (2024)

Please consult the original publications for data licensing and attribution requirements.

---

## Reproducibility

All figures presented in the manuscript can be regenerated from the scripts contained in:

```text
figures/
```

Example:

```bash
python figures/figure1_dispersion_Qeff.py
python figures/figure2_resonance.py
python figures/figure3_torque.py
python figures/figure4_orbits.py
```

---

## Citation

If you use this code or build upon this work, please cite:

```bibtex
@article{Keske2026,
  author  = {Keske, Ahmet},
  title   = {A Unified Stability Chain for M31:
             Inner Kinematic Braking,
             Bar--Spiral Resonance Locking,
             and Secular Equilibrium},
  journal = {MNRAS Preprint},
  year    = {2026}
}
```

---

## License

MIT License

Copyright (c) 2026 Ahmet Keske

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.

---

## Author

**Ahmet Keske**

Independent Researcher  
Mardin, Türkiye

ORCID: 0009-0000-2288-6680

GitHub:

https://github.com/Ahmet4721

---

## Disclaimer

This repository presents an exploratory dynamical framework motivated by observational properties of M31.

The proposed resonance-locking mechanism remains a testable hypothesis and should be evaluated through future self-consistent N-body and hydrodynamical simulations.

The code is released to promote transparency, reproducibility, and further investigation of galactic dynamical processes.