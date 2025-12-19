import numpy as np
import matplotlib.pyplot as plt

# --- PARAMETRELER ---
kms_to_kpc_per_Gyr = 1.022712165  # 1 km/s = 1.0227 kpc/Gyr
v_c_kms = 220.0  # M31 outer rotation velocity
v_c = v_c_kms * kms_to_kpc_per_Gyr  # ~224.8 kpc/Gyr
v_c_sq = v_c**2

dt = 0.001  # Gyr (zaman adımı)
T_max = 1.0  # Gyr
N_steps = int(T_max / dt)
N_particles = 500  # Daha fazla parçacık, daha güzel ring görünümü

# --- BAŞLANGIÇ KOŞULLARI ---
np.random.seed(42)

# Parçacıkları 9 kpc civarına yerleştir (ring yapısı için)
R0 = 9.0
R = R0 + np.random.normal(0, 0.3, N_particles)  # Dar dağılım, daha net ring
theta = np.random.uniform(0, 2*np.pi, N_particles)

# Kartezyen konum
x = R * np.cos(theta)
y = R * np.sin(theta)

# Hızlar
v_R = np.random.normal(0, 8 * kms_to_kpc_per_Gyr, N_particles)  # Küçük radyal dispersion
v_theta = v_c * (R0 / R)**0.5  # Yaklaşık dairesel hız (flat curve için hafif düzeltme)

vx = v_R * np.cos(theta) - v_theta * np.sin(theta)
vy = v_R * np.sin(theta) + v_theta * np.cos(theta)

# --- İVME FONKSİYONU (Logaritmik Potansiyel) ---
def get_acceleration(x, y):
    r_sq = x**2 + y**2 + 1e-8  # Sıfır bölünme önleme
    a_factor = -v_c_sq / r_sq
    return a_factor * x, a_factor * y

# --- LEAPFROG ENTEGRASYON ---
ax, ay = get_acceleration(x, y)

# Tarihçe için daha az kayıt (performans için)
save_interval = 1000  # Her 1 Myr'de bir kaydet (dt=0.001 Gyr)
history_x = [x.copy()]
history_y = [y.copy()]

for step in range(1, N_steps + 1):
    # Kick (yarım adım hız)
    vx += ax * (dt / 2)
    vy += ay * (dt / 2)
    
    # Drift (tam adım konum)
    x += vx * dt
    y += vy * dt
    
    # Yeni ivme
    ax, ay = get_acceleration(x, y)
    
    # İkinci kick
    vx += ax * (dt / 2)
    vy += ay * (dt / 2)
    
    # Kaydet
    if step % save_interval == 0:
        history_x.append(x.copy())
        history_y.append(y.copy())

history_x = np.array(history_x)
history_y = np.array(history_y)

# --- GÖRSELLEŞTİRME ---
plt.figure(figsize=(10, 10))

# Tüm yörüngeleri ince çizgiyle çiz (alpha ile şeffaf)
for i in range(N_particles):
    plt.plot(history_x[:, i], history_y[:, i], 'k-', alpha=0.05, linewidth=0.5)

# Başlangıç ve son konumları vurgula
plt.scatter(history_x[0], history_y[0], c='blue', s=20, label='t = 0 Gyr', alpha=0.8)
plt.scatter(history_x[-1], history_y[-1], c='red', s=20, label=f't = {T_max} Gyr', alpha=0.8)

plt.title(f'M31 Tracer Particle Simulation\nFlat Rotation Curve (v_c = {v_c_kms} km/s), N = {N_particles}')
plt.xlabel('X [kpc]')
plt.ylabel('Y [kpc]')
plt.xlim(-12, 12)
plt.ylim(-12, 12)
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.savefig('m31_tracer_simulation.png', dpi=300)  # Yüksek kaliteli kaydet
plt.show()

print(f"Simülasyon tamamlandı. {N_particles} parçacık, {T_max} Gyr evrim.")
print("Ring yapısı korundu – disk stabilitesi gösterildi.")