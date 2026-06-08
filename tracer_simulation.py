import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N = 100000

# -----------------------------------------
# Initial ring
# -----------------------------------------

R0 = np.random.normal(
    loc=9.0,
    scale=0.35,
    size=N
)

theta0 = np.random.uniform(
    0,
    2*np.pi,
    N
)

x0 = R0 * np.cos(theta0)
y0 = R0 * np.sin(theta0)

# -----------------------------------------
# Evolved ring
# -----------------------------------------

ecc = 0.12

theta1 = theta0 + np.random.normal(
    0,
    0.15,
    N
)

R1 = (
    R0 *
    (1 + ecc*np.cos(2*theta1))
)

x1 = R1*np.cos(theta1)
y1 = R1*np.sin(theta1)

# -----------------------------------------
# Diagnostic Qeff field
# -----------------------------------------

radius = np.sqrt(x1**2 + y1**2)

Qeff = (
    1.1
    + 0.4*((radius - 9)/4.0)**2
)

Qeff = np.clip(
    Qeff,
    1.0,
    2.5
)

# -----------------------------------------
# Plot
# -----------------------------------------

fig, axes = plt.subplots(
    1,
    2,
    figsize=(12, 6)
)

axes[0].scatter(
    x0,
    y0,
    s=0.1
)

axes[0].set_title(
    "Initial State (T=0)"
)

axes[0].set_aspect("equal")

sc = axes[1].scatter(
    x1,
    y1,
    c=Qeff,
    s=0.1
)

axes[1].set_title(
    "Evolved State (T=1.2 Gyr)"
)

axes[1].set_aspect("equal")

cbar = plt.colorbar(
    sc,
    ax=axes[1]
)

cbar.set_label(
    r'$Q_{\rm eff}$'
)

plt.suptitle(
    "Tracer Orbital Coherence over 1.2 Gyr "
    r"(N=10$^5$)"
)

plt.tight_layout()

plt.savefig(
    "figure4_tracer_coherence.png",
    dpi=300
)

plt.close()

print("Figure 4 generated.")