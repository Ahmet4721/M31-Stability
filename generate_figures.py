"""
generate_figures.py
===================
M31 Stability Framework — Figure Generation Script
---------------------------------------------------
Keske, A. (2026). Integrated Model of Stability in M31:
Inner Braking, Resonance Coupling, and Observational Predictions.

Produces four publication-quality PDF figures:
  fig1_profiles.pdf  — sigma_R(R) and Q_eff(R) profiles
  fig2_resonance.pdf — Resonance overlap frequency diagram
  fig3_torque.pdf    — Torque balance and angular momentum flux
  fig4_tracers.pdf   — Tracer distributions at T=0 and T=1 Gyr

Requirements:
  numpy, matplotlib, scipy

Usage:
  python generate_figures.py

Output files are saved in the current working directory.

Repository: https://github.com/Ahmet4721/M31-Stability
Author: Ahmet Keske <ahmetkeske45@gmail.com>
ORCID: 0009-0000-2288-6680
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Global plot style ────────────────────────────────────────
plt.rcParams.update({
    # MNRAS font standartları
    'font.family'        : 'serif',
    'font.serif'         : ['Times New Roman', 'DejaVu Serif', 'serif'],
    'font.size'          : 9,        # MNRAS temel font boyutu
    'axes.labelsize'     : 9,        # Eksen etiketleri min 8pt, 9pt güvenli
    'axes.titlesize'     : 9,
    'legend.fontsize'    : 8,        # Legend min 8pt
    'xtick.labelsize'    : 8,
    'ytick.labelsize'    : 8,
    'axes.linewidth'     : 0.8,
    'xtick.major.width'  : 0.8,
    'ytick.major.width'  : 0.8,
    'xtick.minor.width'  : 0.6,
    'ytick.minor.width'  : 0.6,
    'xtick.major.size'   : 4,
    'ytick.major.size'   : 4,
    'xtick.minor.size'   : 2,
    'ytick.minor.size'   : 2,
    'xtick.direction'    : 'in',
    'ytick.direction'    : 'in',
    'xtick.top'          : True,
    'ytick.right'        : True,
    'lines.linewidth'    : 1.5,
    'figure.dpi'         : 300,      # Yayın kalitesi
    'savefig.dpi'        : 300,
    'savefig.bbox'       : 'tight',
    'savefig.pad_inches' : 0.05,
})

# ── Unit conversion ──────────────────────────────────────────
KMS_TO_KPC_PER_GYR = 1.022712165   # 1 km/s = 1.0227 kpc/Gyr
G_UNITS            = 4.498e-6      # G in kpc^3 / (M_sun * Gyr^2)


# ════════════════════════════════════════════════════════════
# KINEMATIC FUNCTIONS
# ════════════════════════════════════════════════════════════

def sigma_R(R, sigma_bulge=140., sigma_disk=70., R_p=2., R_d=5.):
    """
    Two-component radial velocity dispersion profile (Equation 1).

    Parameters
    ----------
    R            : array-like, radius [kpc]
    sigma_bulge  : float, central bulge dispersion [km/s]
    sigma_disk   : float, outer disk dispersion [km/s]
    R_p          : float, bulge pressure scale length [kpc]
    R_d          : float, disk transition scale [kpc]

    Returns
    -------
    sigma_R : array-like [km/s]
    """
    return sigma_bulge * np.exp(-R / R_p) + sigma_disk * (1. - np.exp(-R / R_d))


def sigma_R_upper(R):
    """Upper uncertainty bound (+15%) on sigma_R."""
    return sigma_R(R, sigma_bulge=155., sigma_disk=80., R_p=1.8, R_d=4.5)


def sigma_R_lower(R):
    """Lower uncertainty bound (-15%) on sigma_R."""
    return sigma_R(R, sigma_bulge=125., sigma_disk=62., R_p=2.2, R_d=5.5)


def kappa(R, v_c=220.):
    """
    Epicyclic frequency for a flat rotation curve.
    kappa = sqrt(2) * v_c / R   [km/s/kpc]
    """
    return np.sqrt(2.) * v_c / R


def Omega(R, v_c=220.):
    """Circular angular velocity [km/s/kpc]."""
    return v_c / R


def compute_Qeff(R, sigma_bulge=140., sigma_disk=70., R_p=2., R_d=5.,
                 Sigma_s0=50., Sigma_g0=10., h_s=5., h_g=8.,
                 c_s=10., v_c=220.):
    """
    Effective two-component Toomre parameter (Romeo & Wiegert 2011).

    Parameters
    ----------
    R       : array-like, radius [kpc]
    Sigma_s0: float, central stellar surface density [M_sun/pc^2]
    Sigma_g0: float, central gas surface density [M_sun/pc^2]
    h_s     : float, stellar scale length [kpc]
    h_g     : float, gas scale length [kpc]
    c_s     : float, gas sound speed [km/s]

    Returns
    -------
    Q_eff : array-like
    """
    sig    = sigma_R(R, sigma_bulge, sigma_disk, R_p, R_d)
    kap    = kappa(R, v_c)
    Sig_s  = Sigma_s0 * np.exp(-R / h_s)
    Sig_g  = Sigma_g0 * np.exp(-R / h_g)

    # Single-component Q values (3.36 G factor for thin disk)
    Q_s = (sig * kap) / (3.36 * G_UNITS * 1e6 * Sig_s)
    Q_g = (c_s * kap) / (3.36 * G_UNITS * 1e6 * Sig_g)

    # Romeo & Wiegert weight factors
    W_s = 2. * sig * c_s / (sig**2 + c_s**2)
    W_g = 2. * c_s**2    / (sig**2 + c_s**2)

    return 1. / (W_s / Q_s + W_g / Q_g)


def resonance_radii(Omega_b, v_c=220.):
    """
    OLR radius for flat rotation curve.
    R_OLR = (v_c / Omega_b) * (1 + 1/sqrt(2))
    """
    return (v_c / Omega_b) * (1. + 1. / np.sqrt(2.))


# ════════════════════════════════════════════════════════════
# FIGURE 1 — sigma_R and Q_eff profiles
# ════════════════════════════════════════════════════════════

def make_fig1(outfile='fig1_profiles.pdf'):
    R = np.linspace(0.5, 25., 400)

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.2))  # MNRAS double column ~17.4cm

    # ── Left panel: sigma_R ──────────────────────────────
    ax = axes[0]
    ax.fill_between(R, sigma_R_lower(R), sigma_R_upper(R),
                    alpha=0.25, color='steelblue',
                    label=u'\u00b115% uncertainty')
    ax.plot(R, sigma_R(R), color='steelblue', lw=2,
            label=r'$\sigma_R$(R) model')
    ax.axvline(9., color='gray', ls=':', lw=1.2)
    ax.set_xlabel(r'$R$ (kpc)')
    ax.set_ylabel(r'$\sigma_R$ (km s$^{-1}$)')
    ax.set_xlim(0., 25.); ax.set_ylim(50., 165.)
    ax.legend()
    ax.set_title('Velocity Dispersion Profile')

    # ── Right panel: Q_eff ───────────────────────────────
    ax = axes[1]
    Q_nom = compute_Qeff(R)
    Q_hi  = compute_Qeff(R, sigma_bulge=155., sigma_disk=80.,
                         R_p=1.8, R_d=4.5,
                         Sigma_s0=43., Sigma_g0=8.5)
    Q_lo  = compute_Qeff(R, sigma_bulge=125., sigma_disk=62.,
                         R_p=2.2, R_d=5.5,
                         Sigma_s0=57.5, Sigma_g0=11.5)

    ax.fill_between(R, Q_lo, Q_hi, alpha=0.25, color='darkorange',
                    label='Propagated uncertainty')
    ax.plot(R, Q_nom, color='darkorange', lw=2,
            label='Qeff(R)')
    ax.axhline(1.0, color='red',  ls='--', lw=1.2,
               label='Q = 1')
    ax.axvline(9.,  color='gray', ls=':',  lw=1.2,
               label='R_lock = 9 kpc')
    ax.set_xlabel(r'$R$ (kpc)')
    ax.set_ylabel(r'$Q_{\rm eff}$')
    ax.set_xlim(0., 25.); ax.set_ylim(0.8, 2.0)
    ax.legend(fontsize=9)
    ax.set_title('Stability Profile')

    plt.tight_layout()
    plt.savefig(outfile, dpi=200, bbox_inches='tight')
    plt.close()
    print(f'  {outfile}  ✓')


# ════════════════════════════════════════════════════════════
# FIGURE 2 — Resonance overlap frequency diagram
# ════════════════════════════════════════════════════════════

def make_fig2(outfile='fig2_resonance.pdf'):
    v_c  = 220.
    Ob   = 42.                           # bar pattern speed [km/s/kpc]
    Os   = v_c / 9.                      # spiral pattern speed
    R    = np.linspace(1., 20., 400)
    Om   = Omega(R, v_c)
    kap  = kappa(R, v_c)

    R_OLR = resonance_radii(Ob, v_c)    # ≈ 8.95 kpc
    R_CR  = v_c / Os                     # = 9.0  kpc
    Delta = 2.3                          # resonance width [kpc]

    fig, ax = plt.subplots(figsize=(3.35, 3.0))  # MNRAS single column ~8.5cm

    ax.plot(R, Om,          color='black',     lw=2,
            label='Omega(R)')
    ax.plot(R, Om - kap/2., color='steelblue', lw=2,
            label='Omega - kappa/2  (OLR locus)')
    ax.plot(R, Om + kap/2., color='steelblue', lw=2, ls='--',
            label='Omega + kappa/2  (ILR locus)')
    ax.axhline(Ob, color='darkorange', lw=2,
               label=f'Omega_b = {Ob:.0f} km/s/kpc')
    ax.axhline(Os, color='seagreen',   lw=2,
               label=f'Omega_s = {Os:.1f} km/s/kpc')

    # Vertical markers
    ax.axvline(R_OLR, color='darkorange', ls=':', lw=1.2)
    ax.axvline(R_CR,  color='seagreen',   ls=':', lw=1.2)

    # Resonance overlap window
    ax.axvspan(R_OLR - Delta/2., R_OLR + Delta/2.,
               alpha=0.14, color='gold',
               label='Delta R_res = sigma_R/kappa')

    # Annotations
    ax.annotate('OLR', xy=(R_OLR, Ob), xytext=(R_OLR + 0.7, Ob + 5.),
                fontsize=10, color='darkorange',
                arrowprops=dict(arrowstyle='->', color='darkorange', lw=1.2))
    ax.annotate('CR',  xy=(R_CR,  Os), xytext=(R_CR  + 0.7, Os + 5.),
                fontsize=10, color='seagreen',
                arrowprops=dict(arrowstyle='->', color='seagreen',   lw=1.2))

    ax.set_xlabel(r'$R$ (kpc)')
    ax.set_ylabel(r'Angular velocity (km s$^{-1}$ kpc$^{-1}$)')
    ax.set_xlim(1., 18.); ax.set_ylim(0., 120.)
    ax.legend(fontsize=9, loc='upper right')
    ax.set_title('Resonance Overlap Diagram')

    plt.tight_layout()
    plt.savefig(outfile, dpi=200, bbox_inches='tight')
    plt.close()
    print(f'  {outfile}  ✓')


# ════════════════════════════════════════════════════════════
# FIGURE 3 — Torque balance and angular momentum flux
# ════════════════════════════════════════════════════════════

def make_fig3(outfile='fig3_torque.pdf'):
    v_c   = 220.
    Ob    = 42.
    Os    = v_c / 9.
    R_OLR = resonance_radii(Ob, v_c)
    R_CR  = v_c / Os
    h     = 2.3   # resonance width [kpc]

    R = np.linspace(0.5, 20., 500)

    # Gaussian torque profiles (Equations 18–19)
    T_bar = -(R / R_OLR)**2 * np.exp(-((R - R_OLR) / h)**2)
    T_sp  = +(R / R_CR )**2 * np.exp(-((R - R_CR)  / h)**2)
    F_L   = T_bar + T_sp

    fig, ax = plt.subplots(figsize=(3.35, 2.8))  # MNRAS single column

    ax.plot(R, T_bar, color='steelblue',  lw=2,
            label='T_bar(R)  (Inner Braking)')
    ax.plot(R, T_sp,  color='seagreen',   lw=2,
            label='T_sp(R)  (Outer Support)')
    ax.plot(R, F_L,   color='darkorange', lw=2.5, ls='--',
            label='F_L(R)  (Net flux)')
    ax.axhline(0., color='black', lw=0.8)
    ax.axvline(9., color='gray',  lw=1.2, ls=':')

    # Shade inner braking / outer support regions
    ax.fill_between(R, F_L, 0., where=(R <  9.), alpha=0.08,
                    color='steelblue')
    ax.fill_between(R, F_L, 0., where=(R >= 9.), alpha=0.08,
                    color='seagreen')

    # Zero-crossing annotation
    ax.annotate('F_L(R_lock) = 0',
                xy=(9., 0.), xytext=(11., 0.18),
                fontsize=10,
                arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    ax.set_xlabel(r'$R$ (kpc)')
    ax.set_ylabel(r'Torque density (arb. units)')
    ax.set_xlim(0.5, 20.); ax.set_ylim(-0.50, 0.50)
    ax.legend(fontsize=9)
    ax.set_title('Torque Balance and Angular Momentum Flux Density')

    plt.tight_layout()
    plt.savefig(outfile, dpi=200, bbox_inches='tight')
    plt.close()
    print(f'  {outfile}  ✓')


# ════════════════════════════════════════════════════════════
# FIGURE 4 — Tracer distributions T=0 and T=1 Gyr
# ════════════════════════════════════════════════════════════

def run_tracer_simulation(N=100_000, T_max=1.0, dt=0.001,
                           v_c_kms=220., R0=9.0, sigma_R0=80.,
                           seed=42):
    """
    Leapfrog tracer simulation in a fixed logarithmic potential.

    Parameters
    ----------
    N        : int,   number of tracer particles
    T_max    : float, simulation duration [Gyr]
    dt       : float, time-step [Gyr]
    v_c_kms  : float, circular velocity [km/s]
    R0       : float, ring radius [kpc]
    sigma_R0 : float, initial radial velocity dispersion [km/s]
    seed     : int,   random seed

    Returns
    -------
    x0, y0 : initial positions [kpc]
    xf, yf : final positions   [kpc]
    """
    np.random.seed(seed)
    v_c  = v_c_kms  * KMS_TO_KPC_PER_GYR
    sig0 = sigma_R0 * KMS_TO_KPC_PER_GYR

    # ── Initial conditions (ring + inner disk) ──────────
    N_ring = int(0.70 * N);  N_disk = N - N_ring

    R_ring = R0 + np.random.normal(0., 0.6, N_ring)
    t_ring = np.random.uniform(0., 2.*np.pi, N_ring)

    R_disk = np.abs(np.random.normal(4.0, 1.5, N_disk))
    t_disk = np.random.uniform(0., 2.*np.pi, N_disk)

    R_all = np.concatenate([R_ring, R_disk])
    t_all = np.concatenate([t_ring, t_disk])

    x0 = R_all * np.cos(t_all)
    y0 = R_all * np.sin(t_all)

    # ── Velocity initialisation ──────────────────────────
    vR = np.random.normal(0., sig0, N)
    vT = v_c * (R0 / R_all)**0.5
    vx = vR * np.cos(t_all) - vT * np.sin(t_all)
    vy = vR * np.sin(t_all) + vT * np.cos(t_all)

    x = x0.copy(); y = y0.copy()

    def accel(x, y):
        r2 = x**2 + y**2 + 1e-8
        f  = -v_c**2 / r2
        return f * x, f * y

    # ── Leapfrog integration ─────────────────────────────
    ax_, ay_ = accel(x, y)
    n_steps  = int(T_max / dt)

    for _ in range(n_steps):
        vx  += ax_ * dt / 2.
        vy  += ay_ * dt / 2.
        x   += vx  * dt
        y   += vy  * dt
        ax_, ay_ = accel(x, y)
        vx  += ax_ * dt / 2.
        vy  += ay_ * dt / 2.

    return x0, y0, x, y


def make_fig4(outfile='fig4_tracers.pdf'):
    print('  Running tracer simulation (N=100,000, T=1 Gyr)...')
    x0, y0, xf, yf = run_tracer_simulation()

    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.5))  # MNRAS double column
    lim  = 14
    bins = 120

    theta_c = np.linspace(0., 2.*np.pi, 300)

    for ax, (xd, yd), title, cmap in zip(
            axes,
            [(x0, y0), (xf, yf)],
            [r'Initial State ($T = 0$)',
             r'Evolved State ($T = 1$ Gyr)'],
            ['Blues', 'Oranges']):

        ax.hexbin(xd, yd, gridsize=bins, cmap=cmap,
                  extent=[-lim, lim, -lim, lim], mincnt=1)
        ax.plot(9.*np.cos(theta_c), 9.*np.sin(theta_c),
                'w--', lw=1.3, alpha=0.8,
                label=r'$R = 9$ kpc ring')
        ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
        ax.set_aspect('equal')
        ax.set_xlabel(r'$x$ (kpc)')
        ax.set_ylabel(r'$y$ (kpc)')
        ax.set_title(title)
        ax.legend(fontsize=9, loc='upper right')

    fig.suptitle(
        r'Tracer Orbital Coherence over 1.2 Gyr  ($N = 10^5$,'
        r' fixed potential)',
        fontsize=11, y=1.01)

    plt.tight_layout()
    plt.savefig(outfile, dpi=200, bbox_inches='tight')
    plt.close()
    print(f'  {outfile}  ✓')


# ════════════════════════════════════════════════════════════
# MAIN
# ════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('M31 Stability Framework — generating figures\n')
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    print('\nAll figures saved to current directory.')
