import utility

values = {"name": 0,"time": 1, "cost": 2, "enjoyment": 3 }
constraints = {"time":0, "budget":1}

def greedscore(activity, maxbudget, maxtime):
    maxbudget = float(maxbudget)
    maxtime = float(maxtime)
    time = int(activity[1])
    budget = int(activity[2])
    enjoyment = int(activity[3])
    if maxbudget != 0:
        normalisedbudget = budget / maxbudget
    else:
        normalisedbudget = 0
    if maxtime != 0:
        normalisedtime = time / maxtime
    else:
        normalisedtime = 0
    denominator = normalisedbudget + normalisedtime
    if denominator == 0:
        return 0
    return enjoyment / denominator

def greedyapproach(activities,max_time,max_budget,amount):
    split_activities = [a.split() for a in activities]
    sortedactivities = sorted(split_activities, key=lambda a: greedscore(a, max_budget, max_time), reverse=True)
    selected = []
    totalbudget = 0
    totaltime = 0
    totalenjoyment = 0
    for a in sortedactivities:
        if (totalbudget + int(a[values["cost"]]) <= max_budget and totaltime + int(a[values["time"]]) <= max_time):
            selected.append(a)
            totalbudget += int(a[values["cost"]])
            totaltime += int(a[values["time"]])
            totalenjoyment += int(a[values["enjoyment"]])
    selected = [" ".join(a) for a in selected]
    return totalenjoyment, selected, totalbudget, totaltime


    
def main():
    file = utility.get_file()

    max_time = utility.get_target(0)
    max_budget = utility.get_target(1)
    
    list_activities = utility.get_activities(file)
    n_activities = utility.get_number_activities(file)
    
    print(f"Constraints: Time <= {max_time}, Budget <= £{max_budget}")
 
    results = greedyapproach(list_activities, max_time, max_budget, n_activities)

    print("\nDP Optimal Solution Found")
    print(f"Enjoyment: {results[0]}")
    print(f"Activities: {results[1]}")
    print(f"Total Cost: £{results[2]}")
    print(f"Total Time: {results[3]} hours")

if __name__ == "__main__":
    main()