import random
import time
import os
import matplotlib.pyplot as plt
import utility
import brute_force as bf
import dynamic as dp

def generate_random_input(n, filename, max_time=99, max_budget=999):
  activities = []
  for i in range(n):
    name = f"Activity{i+1}"
    time_required = random.randint(1, 9) 
    cost = random.randint(5, 30)
    enjoyment = random.randint(1, 10)
    activities.append(f"{name} {time_required} {cost} {enjoyment}")
    
    with open(f"assets/{filename}", "w") as f:
      f.write(f"{n}\n")
      f.write(f"{max_time} {max_budget}\n")
      for act in activities:
        f.write(act + "\n")

# Random input file generation https://realpython.com/python-random/

def run_algorithms(file_path):
  file_data = utility.read_file(file_path)
  n_activities = utility.get_number_activities(file_data)
  activities = utility.get_activities(file_data)
  max_time = utility.get_target(0)
  max_budget = utility.get_target(1)

  # bf
  bf_time = None
  if n_activities < 25:
    start = time.time()
    bf_results = bf.brute_force(activities, max_time, max_budget, n_activities)
    bf_time = time.time() - start
  else:
    print(f"Skipping brute force for n={n_activities} (too slow)")
  
  # dp
  start = time.time()
  dp_results = dp.dynamic_programming(activities, max_time, max_budget, n_activities)
  dp_time = time.time() - start

  return bf_time, dp_time

  # timing code https://docs.python.org/3/library/time.html

def main():
  ns = [10, 15, 20, 25, 30]
  bf_times = []
  dp_times = []

  if not os.path.exists("assets"):
    os.mkdir("assets")

  for n in ns:
    filename = f"input_{n}.txt"
    max_time = random.randint(75, 130)
    max_budget = random.randint(800, 1200)
    generate_random_input(n, filename, max_time, max_budget)
    file_path = f"assets/{filename}"
    print(f"Running the algorithms on {filename}...")
    
    bf_time, dp_time = run_algorithms(file_path)
    bf_times.append(bf_time)
    dp_times.append(dp_time)

  
  ns_bf = [n for n, t in zip(ns, bf_times) if t is not None]
  bf_plot_times = [t for t in bf_times if t is not None]

  plt.figure(figsize=(10, 5))
  plt.plot(ns_bf, bf_plot_times, marker='x', label='Brute Force')
  plt.plot(ns, dp_times, marker='o', label='Dynamic Programming')
  plt.title('Execution Time against No. of Activities')
  plt.xlabel('No. of Activities (n)')
  plt.ylabel('Execution Time (seconds)')
  plt.legend()
  plt.grid(True)
  plt.savefig("execution_time_plot.png")
  plt.show()

  plt.figure(figsize=(10,5))
  plt.plot(ns_bf, bf_plot_times, marker='x', label='Brute Force')
  plt.plot(ns, dp_times, marker='o', label='Dynamic Programming')
  plt.title('Execution Time (Log Scale) against No. of Activities')
  plt.xlabel('No. of Activities (n)')
  plt.ylabel('Execution Time (seconds, log scale)')
  plt.yscale('log')
  plt.legend()
  plt.grid(True, which='both')
  plt.savefig("execution_time_log_plot.png")
  plt.show()

  speedup = [bf/dp for bf, dp in zip(bf_times, dp_times) if bf is not None]
  plt.figure(figsize=(10, 5))
  plt.bar([str(n) for n in ns_bf], speedup, color='lightcyan')
  plt.title('Speedup Factor: Brute Force Time & Dynamic Programming Time')
  plt.xlabel('No. of Activities (n)')
  plt.ylabel('Speedup Factor')
  plt.savefig("speedup_plot.png")
  plt.show()

  print("\nSummary Table:")
  print("n\tBF(s)\tDP(s)\tSpeedup")
  for i, n in enumerate(ns):
    bf_val = f"{bf_times[i]:.4f}" if bf_times[i] is not None else "Skipped"
    dp_val = f"{dp_times[i]:.4f}"
    speed_val = f"{bf_times[i]/dp_times[i]:.2f}" if bf_times[i] is not None else "-"
    print(f"{n}\t{bf_val}\t{dp_val}\t{speed_val}")

if __name__ == "__main__":
  main()
      
