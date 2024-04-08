import sys
import os
import time
from ortools.algorithms.python import knapsack_solver
from utils import load_data

current_path = os.getcwd()
result = 'result.csv'
test_dir = os.path.join(current_path, 'test_case')
test_file = 's000.kp'

with open(result, mode='w') as file:
    print('Group', 'Test', 'Range test', 'Computed value', 'Total weight', 'Time', 'isOptimal', file=file, sep=',')
    for group in os.listdir(test_dir):
        group_path = os.path.join(test_dir, group)
        for test in os.listdir(group_path):
            test_path = os.path.join(group_path, test)
            for range_test in os.listdir(test_path):
                file_path = os.path.join(test_path, range_test, test_file)
                number, capacity, values, weight = load_data(file_path)

                solver = knapsack_solver.KnapsackSolver(
                    knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
                    "KnapsackExample",
                    )   

                capacities = []
                capacities.append(capacity) 
                weights = [weight]
                solver.init(values, weights, capacities)
                solver.set_time_limit(180)
                start = time.perf_counter()
                computed_value = solver.solve()
                end = time.perf_counter()
                run_time = end - start

                packed_items = []
                packed_weights = []
                total_weight = 0
                isOptimal = solver.is_solution_optimal()
                for i in range(len(values)):
                    if solver.best_solution_contains(i):
                        packed_items.append(i)
                        packed_weights.append(weights[0][i])
                        total_weight += weights[0][i]              

                print(group, test, range_test, computed_value, total_weight, run_time, isOptimal, sep=',')
                print(group, test, range_test, computed_value, total_weight, run_time, isOptimal, file=file, sep=',')