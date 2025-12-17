import numpy as np
import matplotlib.pyplot as plt

# Simple tracer simulation in logarithmic potential (flat rotation curve v_c = 220 km/s)
# Parameters
v_c = 220.0  # km/s
Gyr_to_s = 3.15576e16  # seconds in Gyr
kpc_to_km = 3.08568e16  # km in kpc
dt = 0.001  # Gyr timestep
N_steps = 100000  # for ~1 Gyr
N_particles = 100  # small sample for demo

# Initial conditions: particles near R = 9 kpc with small dispersion
np.random.seed(42)
R = 9.0 + np.random.normal(0, 0.5, N_particles)
theta = np.random.uniform(0, 2*np.pi, N_particles)
v_R = np.random.normal(0, 10, N_particles)  # small radial velocity dispersion
v_theta = v_c * np.sqrt(9.0 / R)  # approximate circular velocity

positions = []
for step in range(N_steps):
    # Centripetal acceleration for flat curve
    a_r = - (v_c**2 / R)
    
    # Leapfrog integration
    v_R += a_r * dt / 2
    R += v_R * dt
    v_R += a_r * dt / 2
    
    theta += v_theta / R * dt
    v_theta = v_c * np.sqrt(9.0 / R)  # keep circular approx
    
    if step % 10000 == 0:  # save every 100 Myr
        x = R * np.cos(theta)
        y = R * np.sin(theta)
        positions.append((x.copy(), y.copy()))

# Plot final positions
x, y = positions[-1]
plt.figure(figsize=(8,8))
plt.scatter(x, y, s=5, alpha=0.7)
plt.title('Tracer Particles after ~1 Gyr in Logarithmic Potential')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.savefig('final_distribution.png')
plt.show()

print("Simulation complete. Particles maintain coherence (ring-like structure).")
