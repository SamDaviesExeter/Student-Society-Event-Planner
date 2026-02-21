import time
import sys
import utility
import brute_force as bf
import dynamic as dp

def print_results(algorithm_name, selected, total_enjoyment, total_time, total_cost, exec_time):
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

    run_bf = True
    if n_activities > 25:
        print(f"The input size is large ({n_activities} activites)")
        print(f"The brute force will check {2**n_activities} combinations")
        response = input("This will take a long time. Would you like to continue? (y/n): ")
        if response.lower() != "y":
            run_bf = False
            print("Skipping brute force\n")

    if run_bf:
        start = time.time()
        bf_results = bf.brute_force(list_activities,available_time,available_budget, n_activities)
        bf_exec = time.time() - start
        print_results("Brute force algorithm", bf_results[1],bf_results[0], bf_results[3], bf_results[2], bf_exec)

    start = time.time()
    dp_results = dp.dynamic_programming(list_activities,available_time,available_budget,n_activities)
    dp_exec = time.time() - start
    print_results("Dynamic programming algorithm", dp_results[1], dp_results[0], dp_results[3], dp_results[2], dp_exec)

    print(f"Time available: {available_time} hours | Time used: {dp_results[3]} hours")
    print(f"Available budget: £{available_budget} | Budget used: £{dp_results[2]}")

if __name__ == "__main__":
    main()
