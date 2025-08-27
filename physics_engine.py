import numpy as np
from constants import *

class HarmonicOscillator:
    def __init__(self, mass=MASS, k=SPRING_CONSTANT,
                 x0=INITIAL_POSITION, v0=INITIAL_VELOCITY):
        self.mass = mass
        self.k = k
        self.position = x0
        self.velocity = v0
        self.acceleration = -k * x0 / mass
        self.time = 0
        self.omega = np.sqrt(k / mass)  # Açısal frekans

    def update(self, dt=TIME_STEP):
        self.acceleration = -self.k * self.position / self.mass     # İvme hesapla (F = -kx, a = F/m)
        self.velocity += self.acceleration * dt                     # Hızı güncelle
        self.position += self.velocity * dt                         # Konumu güncelle
        self.time += dt                                             # Zamanı güncelle

        return self.position, self.velocity, self.acceleration

    def analytical_solution(self, t):
        A = INITIAL_POSITION
        phi = 0  # Faz açısı (başlangıçta maksimum uzama)
        x = A * np.cos(self.omega * t + phi)
        v = -A * self.omega * np.sin(self.omega * t + phi)
        a = -A * self.omega ** 2 * np.cos(self.omega * t + phi)
        return x, v, a