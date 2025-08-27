from visualization import simulate_and_plot, real_time_animation
import argparse


def main():
    parser = argparse.ArgumentParser(description='Basit Harmonik Hareket Simülatörü')
    parser.add_argument('--realtime', action='store_true',
                        help='Gerçek zamanlı animasyonu çalıştır')

    args = parser.parse_args()

    if args.realtime:
        real_time_animation()
    else:
        simulate_and_plot()


if __name__ == "__main__":
    main()