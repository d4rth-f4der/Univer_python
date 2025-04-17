import time
import matplotlib.pyplot as plt
from sine_calculator import approx_sin_calculation

def analyze_performance(rad_values_input: list, eps_values_input: list, plot_figsize = (10, 6)):

    rad_values = rad_values_input
    eps_values = eps_values_input
    performance_data = []

    print("Вимірювання продуктивності:")
    for rad in rad_values:
        for eps in eps_values:
            start_time = time.perf_counter()
            result, iterations = approx_sin_calculation(rad, eps)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            performance_data.append({
                "rad": rad,
                "eps": eps,
                "result": result,
                "iterations": iterations,
                "time": elapsed_time
            })
            print(f"rad={rad:.2f}, eps={eps}, iterations={iterations}, time={elapsed_time:.6f}s")

    # Побудова графіка залежності часу виконання від кількості ітерацій
    iterations_data = [res["iterations"] for res in performance_data]
    time_data = [res["time"] for res in performance_data]

    plt.figure(figsize=plot_figsize)
    plt.scatter(iterations_data, time_data)
    plt.xlabel("Кількість ітерацій")
    plt.ylabel("Час виконання (секунди)")
    plt.title("Залежність часу виконання від кількості ітерацій")
    plt.grid(True)
    plt.show()