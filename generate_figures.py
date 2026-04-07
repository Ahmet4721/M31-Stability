import numpy as np
import matplotlib.pyplot as plt

def acceleration(x, y, vc=220.0):
    r = np.sqrt(x**2 + y**2) + 1e-6
    a = - (vc**2 / r)
    ax = a * (x / r)
    ay = a * (y / r)
    return ax, ay

def simulate(N=10000, radius=10.0, vc=220.0, dt=0.001, steps=1000):

    theta = np.linspace(0, 2*np.pi, N)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # initial velocities (circular)
    vx = -vc * np.sin(theta)
    vy = vc * np.cos(theta)

    x0, y0 = x.copy(), y.copy()

    # Leapfrog integration
    for _ in range(steps):
        ax, ay = acceleration(x, y, vc)

        vx += ax * dt
        vy += ay * dt

        x += vx * dt
        y += vy * dt

    return x0, y0, x, y

# Run simulation
x0, y0, x1, y1 = simulate()

# Plot
plt.figure(figsize=(6,6))
plt.scatter(x0, y0, s=5, label='t = 0')
plt.scatter(x1, y1, s=5, label='t = final')

plt.xlabel("X [kpc]")
plt.ylabel("Y [kpc]")
plt.legend()
plt.grid(alpha=0.3)
plt.title("Tracer Particle Stability (Dynamic Integration)")

plt.savefig("stability_dynamic.png", dpi=300)
plt.show()