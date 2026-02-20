import time
import sys
import utility
import brute_force as bf
import dyanimic as dp

def print_results(algorithm_name, selected, total_enjoyment, total_time, toatl_cost, exec_time):
    print(f" ---{algorithm_name}---")
    print("Selected activities:")
    for a in selected:
        parts = a.split()
        print(f" - {parts[0]} ({parts[1]} hours, £{parts[2]}, enjoyment {parts[3]})")
    print(f"Total enjoyment: {total_enjoyment}")
    print(f"Total time used: {total_time} hours")
    print(f"Total cost: £{total_cost}")
    print(f"Execution time: {exec_time:.3f} seconds")
    print()

def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        utility.input_file = input_file

    else:
        input_file = utility.input_file

    file = utility.get_file()
    n_activities = utility.get_number_activities(file)
    list_activities = utility.get_activities(file)
    available_time = utility.get_target(0)
    available_budget = utility.get_target(1)

    print(" EVENT PLANNER RESULTS ")
    print("-----------------------")
    print(f"Input File: {input_file}")
    print(f"Time available: {available_time} hours")
    print(f"Available budget: £{available_budget}")
    print()

    start = time.time()
    bf_enjoyment, bf_selected, bf_cost, bf_time = bf.brute_force(list_activities, utility.get_target(bf.get_constraint()), n_activities)
    bf_exec = time.time() - start
    print_results("Brute force algorithm", bf_selected, bf_enjoyment, bf_time, bf_cost, bf_exec)

    start = time.time()
    dp_enjoyment, dp_selected, dp_cost, dp_time = dp.brute_force(list_activities, utility.get_target(dp.get_constraint()), n_activities)
    dp_exec = time.time() - start
    print_results("Dynamic programming algorithm", dp_selected, dp_enjoyment, dp_time, dp_cost, dp_exec)

    print(f"Time available: {available_time} hours | Time used: {bf_time} hours")
    print(f"Available budget: £{available_budget} | Budget used: £{bf_cost}")

if __name__ == "__main__":
    main()
