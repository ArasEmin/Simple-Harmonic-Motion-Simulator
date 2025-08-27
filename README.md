https://img.shields.io/badge/Python-3.6%252B-blue?logo=python
https://img.shields.io/badge/NumPy-1.20%252B-blue?logo=numpy
https://img.shields.io/badge/Matplotlib-3.3%252B-blue?logo=matplotlib
https://img.shields.io/badge/License-MIT-green

https://img.shields.io/badge/Open%2520in-GitHub%2520Codespaces-blue?logo=github
https://zenodo.org/badge/DOI/10.5281/zenodo.123456789.svg

Fiziksel sistemlerin simülasyonu için Python tabanlı interaktif bir araç

https://via.placeholder.com/800x400.png?text=Harmonic+Motion+Simulation+GIF

📖 Proje Hakkında
Basit Harmonik Hareket Simülatörü, fiziksel sistemlerin davranışlarını anlamak ve görselleştirmek için geliştirilmiş Python tabanlı bir simülasyon aracıdır. Bu proje, yay ve kütle sistemlerinin harmonik hareketini hem sayısal hem de analitik yöntemlerle modelleyerek fizik öğrencileri, eğitimciler ve meraklıları için interaktif bir öğrenme deneyimi sunar.

Proje, klasik mekaniğin temel prensiplerini uygulamalı olarak gösterirken aynı zamanda Python programlama, bilimsel hesaplamalar ve veri görselleştirme tekniklerini bir aray getiriyor.

✨ Özellikler
📊 Çift Çözüm Yöntemi: Sayısal ve analitik çözümlerin karşılaştırmalı analizi

🎨 İnteraktif Görselleştirme: Zaman serisi grafikleri ve animasyonlar

⚡ Enerji Analizi: Kinetik, potansiyel ve toplam enerji değişimlerinin izlenmesi

🔧 Parametre Esnekliği: Kolayca değiştirilebilen fiziksel parametreler

📱 Gerçek Zamanlı Simülasyon: Canlı animasyon desteği

📈 Veri Dışa Aktarma: Grafikleri PNG formatında kaydetme

🛠️ Kurulum
Ön Koşullar
Python 3.6 veya üzeri

pip (Python paket yöneticisi)

Gerekli bağımlılıkları yükleyin:
bash
pip install numpy matplotlib

🚀 Kullanım
Temel Kullanım
bash
# Standart simülasyon (grafiklerle)
python main.py

# Gerçek zamanlı animasyon modu
python main.py --realtime

# Özel parametrelerle çalıştırma
python main.py --mass 2.0 --k 15.0 --time 5
Komut Satırı Seçenekleri
Parametre	Açıklama	Varsayılan Değer
--mass	Kütle (kg)	1.0
--k	Yay sabiti (N/m)	10.0
--x0	Başlangıç konumu (m)	0.5
--v0	Başlangıç hızı (m/s)	0.0
--time	Simülasyon süresi (s)	10
--realtime	Gerçek zamanlı animasyon	False
Programatik Kullanım
Projeyi kendi Python kodunuzda da kullanabilirsiniz:

python
from physics_engine import HarmonicOscillator
from visualization import simulate_and_plot

# Özel parametrelerle osilatör oluşturma
oscillator = HarmonicOscillator(mass=2.0, k=15.0, x0=0.3)

# Simülasyonu çalıştırma ve görselleştirme
simulate_and_plot(oscillator)

📁 Proje Yapısı
text
harmonic-motion-simulator/
├── main.py                 # Ana uygulama giriş noktası
├── physics_engine.py       # Fizik motoru ve hesaplamalar
├── visualization.py        # Görselleştirme fonksiyonları
├── constants.py            # Sabitler ve yapılandırma
