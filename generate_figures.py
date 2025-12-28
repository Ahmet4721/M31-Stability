import numpy as np
import matplotlib.pyplot as plt

def generate_tracer_simulation(N=500, radius=10.0, vc=220.0, t_final=1.0, output_path="m31_tracer_simulation.png"):
    """
    Generates a tracer particle simulation figure for M31 under a flat rotation curve.
    
    Parameters:
        N (int): Number of tracer particles
        radius (float): Initial ring radius in kpc
        vc (float): Circular velocity in km/s
        t_final (float): Final time in Gyr
        output_path (str): Path to save the output figure
    """
    # Constants
    GYR_TO_SEC = 3.154e16  # seconds in a Gyr
    KM_TO_KPC = 3.24078e-17  # conversion factor

    # Initial positions (ring)
    theta = np.linspace(0, 2 * np.pi, N)
    x0 = radius * np.cos(theta)
    y0 = radius * np.sin(theta)

    # Angular velocity: omega = v / r
    omega = vc / radius  # km/s/kpc

    # Time evolution: rotate by omega * t
    delta_theta = omega * t_final * GYR_TO_SEC * KM_TO_KPC  # radians
    x1 = radius * np.cos(theta + delta_theta)
    y1 = radius * np.sin(theta + delta_theta)

    # Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(x0, y0, s=10, c='blue', label='t = 0 Gyr')
    plt.scatter(x1, y1, s=10, c='red', label='t = 1.0 Gyr')
    plt.xlabel('X [kpc]')
    plt.ylabel('Y [kpc]')
    plt.title(f'M31 Tracer Particle Simulation\nFlat Rotation Curve (v₍c₎ = {vc:.1f} km/s), N = {N}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()

if __name__ == "__main__":
    generate_tracer_simulation()