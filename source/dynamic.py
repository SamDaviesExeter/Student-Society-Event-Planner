import utility
from data_strucs import stack_struc
#creates a dictionary mapping for easy acces to activites data columns
values = {"name": 0,"time": 1, "cost": 2, "enjoyment": 3 }

def dynamic_programming(activities, max_time,max_budget, amount):

    #parse the activies before entering the loops to avoid unnecessary computation
    parsed_activities = [a.split() for a in activities]


    #creates a 3D table with [item index][time limit][budget limit]
    #the state represents the maximum enjoyment for the first i items with time t and budget b
    dp = [[[0 for _ in range(max_budget +1)] for _ in range(max_time + 1)] for _ in range(amount +1)]


    #this fills the table of activites
    for i in range(1, amount + 1):
        activity_time = int(parsed_activities[i-1][values["time"]])
        activity_cost = int(parsed_activities[i-1][values["cost"]])
        activity_enjoyment = int(parsed_activities[i-1][values["enjoyment"]])
        for t in range(max_time + 1):
            for b in range(max_budget + 1):
                #this is the default case where the optimal value is the same without adding this item
                dp[i][t][b] = dp[i-1][t][b]

                #checks if we have enough time and budget for the activity then if adding the activity is better
                if activity_time <= t and activity_cost <= b:
                    with_activity = dp[i-1][t - activity_time][b - activity_cost] + activity_enjoyment
                    
                    #stores the higher value of including vs skipping
                    if with_activity > dp[i][t][b]:
                        dp[i][t][b] = with_activity

    #retraces the steps to find selected items
    highest_sequence_stack = stack_struc.stack() # using stack struc
    current_t, current_b = max_time, max_budget
    
    for i in range(amount, 0, -1):
        #if the value in this cell is differnt from the one above then the item at index i was included in the optimal set
        if dp[i][current_t][current_b] != dp[i-1][current_t][current_b]:
            activity = activities[i-1]
            highest_sequence_stack.push(activity)
            #reduces the remaining capacity based on the activites requirements
            current_t -= int(parsed_activities[i-1][values["time"]])
            current_b -= int(parsed_activities[i-1][values["cost"]])

    #we need to reverse the list because we backtracked from the last item to the first
    highest_sequence = highest_sequence_stack.reverse_stack()
    
    #calculates final stats
    total_enjoyment = dp[amount][max_time][max_budget]
    final_cost = sum(int(a.split()[values["cost"]]) for a in highest_sequence)
    final_time = sum(int(a.split()[values["time"]]) for a in highest_sequence)

    return total_enjoyment, highest_sequence, final_cost, final_time

def main():

    #SUGGESTION
    #maybe use a linked list to then get the highest value per with val_per_enjoyment
    #if cost IE budget is not maximised maybe try diff combos with pairs close by in enjoyment / value
    file = utility.get_file()
    
    #gets both targets
    max_time = utility.get_target(0)
    max_budget = utility.get_target(1)
    
    list_activities = utility.get_activities(file)
    n_activities = utility.get_number_activities(file)
    
    print(f"Constraints: Time <= {max_time}, Budget <= £{max_budget}")
    
    #execution of the dynamic programming algorithm
    results = dynamic_programming(list_activities, max_time, max_budget, n_activities)
    

    #prints the results of the algorithm
    print("\nDP Optimal Solution Found")
    print(f"Enjoyment: {results[0]}")
    print(f"Activities: {results[1]}")
    print(f"Total Cost: £{results[2]}")
    print(f"Total Time: {results[3]} hours")

if __name__ == "__main__":
    main()