# M31 Stability Framework

This repository provides the numerical framework and simulation tools accompanying the study:

**“Integrated Model of Stability in M31: Inner Braking, Resonance Coupling, and Momentum-Flow Pressure”**

The project investigates the long-term dynamical stability of the Andromeda Galaxy (M31) by integrating tracer particle simulations with physically motivated braking and momentum-flow mechanisms.

---

## Scientific Motivation

Classical models of galactic disk stability often rely on static rotation curves and idealized equilibrium assumptions.  
This framework explores an alternative perspective in which **inner braking**, **resonance coupling**, and **radial momentum-flow pressure** jointly regulate disk stability over gigayear timescales.

The simulations are designed to:
- Track tracer particle evolution in an axisymmetric M31 potential
- Examine stability under flat rotation curves
- Illustrate how momentum redistribution suppresses large-scale instabilities

---

## Repository Contents

- Python scripts for tracer particle simulations  
- Reproducible numerical setup used in the accompanying paper  
- Example outputs illustrating long-term orbital coherence  

This repository is intentionally kept minimal and transparent to facilitate reproducibility.

---

## Example Output

Below is an example tracer particle distribution generated under a flat rotation curve  
(\(v_c = 220\,\mathrm{km\,s^{-1}}\), \(N = 500\)):

![M31 Tracer Particle Simulation](example_output.png)

---

## Reproducibility

The simulations are written in standard Python and rely on commonly used scientific libraries  
(e.g., NumPy, SciPy, Matplotlib).

Exact versions and numerical parameters are documented in the code to ensure full reproducibility.

---

## Citation

If you use this code, simulations, or results in your research, please cite the Zenodo archive:

**DOI:** https://doi.org/10.5281/zenodo.18015688

This repository is archived on Zenodo to provide a permanent, citable reference.

---

## Author

**Ahmet Keske**  
ORCID: https://orcid.org/0009-0000-2288-6680

---

## License

This project is released under the MIT License.
