import time
import sys
import utility
import brute_force as bf
import dynamic as dp
import os

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

def run_planner(file_path):
    utility.input_file = file_path
    file_data = utility.get_file()
    n_activities = utility.get_number_activities(file_data)
    list_activities = utility.get_activities(file_data)
    available_time = utility.get_target(0)
    available_budget = utility.get_target(1)

    print(f"\nProcessing File: {os.path.basename(file_path)}")
    print(f"\nAvailable Time: {available_time}h | Available Budget: £{available_budget}")

    run_bf = True
    if n_activities > 22:
        print(f"The input size is large ({n_activities} activites)")
        if n_activities < 25:
            print(f"The brute force will check {2**n_activities} combinations")
            response = input("This will take a long time. Would you like to continue? (y/n): ")
        response == "n"
        if response.lower() != "y":
            run_bf = False
            print("Skipping brute force (input file too large)\n")

    if run_bf:
        start = time.time()
        bf_results = bf.brute_force(list_activities,available_time,available_budget, n_activities)
        bf_exec = time.time() - start
        print_results("Brute force algorithm", bf_results[1],bf_results[0], bf_results[3], bf_results[2], bf_exec)

    start = time.time()
    dp_results = dp.dynamic_programming(list_activities,available_time,available_budget,n_activities)
    dp_exec = time.time() - start
    print_results("Dynamic programming algorithm", dp_results[1], dp_results[0], dp_results[3], dp_results[2], dp_exec)

def main():
    test_folder = "assets"

    if not os.path.exists(test_folder):
        print(f"{test_folder} folder not found.")
        return

    #filters to look for txt files
    files = sorted([f for f in os.listdir(test_folder) if f.endswith('.txt')])

    #checks if any files exist
    if not files:
        print("No .txt files found in assets")
        return
    #completes algorithms for all input files
    for filename in files:
        run_planner(os.path.join(test_folder, filename))
    print("All files completed")
    

if __name__ == "__main__":
    main()
