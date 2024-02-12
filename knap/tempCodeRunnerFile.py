from utils import *


max_weight = int(input("Enter max weight: "))
values, weights = get_items()

print("Values:", values)
print("Weights:", weights)
print("Max Weight:", max_weight)
print('\n')

# Call genetic_algorithm function and capture the returned values
best_solution_01, best_value_01 = genetic_algorithm(values, weights, max_weight, unbounded=False)
best_solution_unbounded, best_value_unbounded = genetic_algorithm(values, weights, max_weight, unbounded=True)

# Print the best_solution and best_value
print("Best Solution For 0-1 Knapsack:", best_solution_01)
print("Best Value For 0-1 Knapsack:", best_value_01)

print('\n')

print("Best Solution For Unbounded Knapsack:", best_solution_unbounded)
print("Best Value For Unbounded Knapsack:", best_value_unbounded)