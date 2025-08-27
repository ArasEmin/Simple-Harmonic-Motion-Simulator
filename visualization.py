import matplotlib.pyplot as plt
import numpy as np
from physics_engine import HarmonicOscillator
from constants import *


def simulate_and_plot():
# Bu kısım simülasyonu çalıştırır ve GUI tasarımına aktarır.
    oscillator = HarmonicOscillator()
    time_points = np.arange(0, SIMULATION_TIME, TIME_STEP)     # Zaman dizisi

    # Simülasyon verileri
    positions = []
    velocities = []
    accelerations = []

    # Analitik çözüm verileri
    analytical_positions = []
    analytical_velocities = []
    analytical_accelerations = []

    # Simülasyonu çalıştır
    for t in time_points:
        x, v, a = oscillator.update()
        positions.append(x)
        velocities.append(v)
        accelerations.append(a)
        x_a, v_a, a_a = oscillator.analytical_solution(t)
        analytical_positions.append(x_a)
        analytical_velocities.append(v_a)
        analytical_accelerations.append(a_a)

    # Grafikleri oluştur
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

    # Konum grafiği
    ax1.plot(time_points, positions, label='Sayısal Çözüm')
    ax1.plot(time_points, analytical_positions, 'r--', label='Analitik Çözüm')
    ax1.set_ylabel('Konum (m)')
    ax1.legend()
    ax1.grid(True)

    # Hız grafiği
    ax2.plot(time_points, velocities, label='Sayısal Çözüm')
    ax2.plot(time_points, analytical_velocities, 'r--', label='Analitik Çözüm')
    ax2.set_ylabel('Hız (m/s)')
    ax2.legend()
    ax2.grid(True)

    # İvme grafiği
    ax3.plot(time_points, accelerations, label='Sayısal Çözüm')
    ax3.plot(time_points, analytical_accelerations, 'r--', label='Analitik Çözüm')
    ax3.set_xlabel('Zaman (s)')
    ax3.set_ylabel('İvme (m/s²)')
    ax3.legend()
    ax3.grid(True)

    plt.suptitle('Basit Harmonik Hareket Simülasyonu')
    plt.tight_layout()
    plt.savefig('harmonik_hareket.png')
    plt.show()

    # Enerji hesaplamaları
    kinetic_energy = [0.5 * MASS * v ** 2 for v in velocities]
    potential_energy = [0.5 * SPRING_CONSTANT * x ** 2 for x in positions]
    total_energy = [k + p for k, p in zip(kinetic_energy, potential_energy)]

    # Enerji grafiği
    plt.figure(figsize=(10, 6))
    plt.plot(time_points, kinetic_energy, label='Kinetik Enerji')
    plt.plot(time_points, potential_energy, label='Potansiyel Enerji')
    plt.plot(time_points, total_energy, label='Toplam Enerji')
    plt.xlabel('Zaman (s)')
    plt.ylabel('Enerji (J)')
    plt.title('Enerji Değişimi')
    plt.legend()
    plt.grid(True)
    plt.savefig('enerji_plot.png')
    plt.show()


def real_time_animation():
    try:
        import matplotlib.animation as animation
        from matplotlib.patches import Rectangle

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-0.5, 0.5)
        ax.set_aspect('equal')
        ax.grid(True)

        # Yay ve kütle çizimi
        spring, = ax.plot([], [], 'b-', lw=2)
        mass = Rectangle((0, 0), 0.2, 0.1, fc='r')
        ax.add_patch(mass)

        oscillator = HarmonicOscillator()

        def init():
            spring.set_data([], [])
            mass.set_xy((0 - 0.1, -0.05))  # Kütleyi merkezle
            return spring, mass

        def animate(i):
            x, v, a = oscillator.update()

            # Yayı çiz
            spring_x = np.linspace(-1, x, 100)
            spring_y = 0.05 * np.sin(spring_x * 10)
            spring.set_data(spring_x, spring_y)

            # Kütleyi güncelle
            mass.set_xy((x - 0.1, -0.05))

            return spring, mass

        ani = animation.FuncAnimation(fig, animate, frames=int(SIMULATION_TIME / TIME_STEP),
                                      init_func=init, blit=True, interval=TIME_STEP * 1000)

        plt.title('ARS Gerçek Zamanlı Harmonik Hareket Simülasyonu')
        plt.savefig('rt_animasyon.gif', writer='pillow', fps=30)
        plt.show()

    except ImportError:
        print("Gerçek zamanlı animasyon için matplotlib güncel sürümü gereklidir.")