import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbor = [current[i] + random.uniform(-epsilon, epsilon) for i in range(dim)]
        neighbor = [max(bounds[i][0], min(bounds[i][1], neighbor[i])) for i in range(dim)]
        neighbor_value = func(neighbor)

        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value
        elif abs(neighbor_value - current_value) < epsilon:
            break

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value
        elif abs(candidate_value - best_value) < epsilon:
            break

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        temp *= cooling_rate

        if temp < epsilon:
            break

        neighbor = [current[i] + random.uniform(-1, 1) for i in range(dim)]
        neighbor = [max(bounds[i][0], min(bounds[i][1], neighbor[i])) for i in range(dim)]
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temp):
            current, current_value = neighbor, neighbor_value

    return current, current_value


if __name__ == "__main__":
  # Межі для функції
  bounds = [(-5, 5), (-5, 5)]

  # Виконання алгоритмів
  print("Hill Climbing:")
  hc_solution, hc_value = hill_climbing(sphere_function, bounds)
  print("Розв'язок:", hc_solution, "Значення:", hc_value)

  print("\nRandom Local Search:")
  rls_solution, rls_value = random_local_search(sphere_function, bounds)
  print("Розв'язок:", rls_solution, "Значення:", rls_value)

  print("\nSimulated Annealing:")
  sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
  print("Розв'язок:", sa_solution, "Значення:", sa_value)