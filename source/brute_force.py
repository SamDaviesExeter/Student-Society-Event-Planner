import utility


values = {"name": 0,"time": 1, "cost": 2, "enjoyment": 3 }

input_file = "assets/input_1000.txt"


def brute_force(activities,max_time,max_budget,amount):
    #2^n therefore 2 for loops
    #check ie acc0 acc1 acc2 then acc1 acc2 acc3 ... for example 
    # power set basically
    highest_enjoyment = -1
    highest_sequence = []
    final_cost = 0 
    final_time = 0

    split_activities = [a.split() for a in activities]
    #split activites outside of loop so we dont recalculate it 2^n times

    for x in range(2**amount):
        tmp_enjoyment = 0
        tmp_sequence = []
        tmp_cost = 0 
        tmp_time = 0

        for y in range(amount):
            if(x & (1 << y)) > 0: # bitwise AND operation and a bit shift by of 1 y places left 
                activity_data = split_activities[y]
                tmp_sequence.append(activities[y])

                tmp_time += int(activity_data[values["time"]])
                tmp_cost += int(activity_data[values["cost"]])
                tmp_enjoyment += int(activity_data[values["enjoyment"]])

        if tmp_time <= max_time and tmp_cost <= max_budget:
            # if valid check if its the most enjoyable so far
            if tmp_enjoyment > highest_enjoyment:
                highest_enjoyment = tmp_enjoyment
                highest_sequence = tmp_sequence.copy()
                final_cost = tmp_cost
                final_time = tmp_time
        
    return highest_enjoyment, highest_sequence , final_cost, final_time

def main():
    
    file = utility.get_file()
    #get constraint to use

    max_time = utility.get_target(0)
    max_budget = utility.get_target(1)
    
    #then get the activties 
    list_activities = utility.get_activities(file)
    print(list_activities)
    n_activities = utility.get_number_activities(file)

    results = brute_force(list_activities, max_time, max_budget, n_activities)
    
    print("\nOptimal Solution Found")
    print(f"Enjoyment: {results[0]}")
    print(f"Activities: {results[1]}")
    print(f"Total Cost: £{results[2]}")
    print(f"Total Time: {results[3]} hours")

if __name__ == "__main__":
    main()
