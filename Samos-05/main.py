# Самостійна робота 5
import math
import time
from input_handler import get_input, get_input_with_predefined
from sine_calculator import approx_sin_calculation
from performance_analyzer import analyze_performance
from output_display import display_output

while True:
    choice = input("\nВиберіть дію ('m' - ввести дані вручну, 'a' - аналіз продуктивності, 'q' - вихід): ").lower()

    if choice == "m":
        rad, eps = get_input()
        start_time = time.perf_counter()
        result, iterations = approx_sin_calculation(rad, eps)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        display_output(result, iterations, elapsed_time)
    elif choice == "a":
        plot_size = (12, 8)
        RANDOM_rad_values = [math.radians(10), math.radians(20), math.radians(90), 3, 6, 10]
        RANDOM_eps_values = [1e-2, 1e-5, 1e-8, 1e-11]
        analyze_performance(RANDOM_rad_values, RANDOM_eps_values, (12, 8))

        print("\nПриклади викликів з використанням обробки великих радіан:")
        rad_large1 = 713
        rad_large2 = 714
        eps_default = 1e-6

        effective_rad1, _ = get_input_with_predefined(rad_large1, eps_default)
        start_time_large1 = time.perf_counter()
        result_large1, iterations_large1 = approx_sin_calculation(effective_rad1, eps_default)
        end_time_large1 = time.perf_counter()
        elapsed_time_large1 = end_time_large1 - start_time_large1
        display_output(result_large1, iterations_large1, elapsed_time_large1)

        effective_rad2, _ = get_input_with_predefined(rad_large2, eps_default)
        start_time_large2 = time.perf_counter()
        result_large2, iterations_large2 = approx_sin_calculation(effective_rad2, eps_default)
        end_time_large2 = time.perf_counter()
        elapsed_time_large2 = end_time_large2 - start_time_large2
        display_output(result_large2, iterations_large2, elapsed_time_large2)
    elif choice == "q": break
    else:
        print("Невірний вибір. Будь ласка, введіть 'manual' або 'analyze'.")