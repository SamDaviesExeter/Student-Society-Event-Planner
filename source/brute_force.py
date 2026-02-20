import utility

#FOCUS ON BUDGET
constraint = "budget"
constraints_position = {"time": 0,"budget": 1}
values = {"name": 0,"time": 1, "cost": 2, "enjoyment": 3 }

input_file = "assets/input_small.txt"

def get_constraint(): # itterate threw a for loop for both values later for extra credit
    return constraints_position[constraint]

def get_value():
    if constraint == "budget":
        return values["cost"]
    elif constraint == "time":
        return values["time"]

def brute_force(activities,max_value,amount):
    #2^n therefore 2 for loops
    #check ie acc0 acc1 acc2 then acc1 acc2 acc3 ... for example 
    # power set basically
    values_position = get_value() 
    highest_enjoyment = 0 
    highest_sequence = []
    cost = 0 
    for x in range(2**amount):
        tmp_enjoyment = 0
        tmp_sequence = []
        tmp_cost = 0 

        for y in range(amount):
            if(x & (1 << y)) > 0: # bitwise AND operation and a bit shift by of 1 y places left 
                tmp_sequence.append(activities[y])

        #now from temp sequence get the cost of every activity and the enjoyment and add it up
        for y in range(len(tmp_sequence)):
            tmp_cost += utility.get_int_value_array(get_value(),tmp_sequence[y].split())
            tmp_enjoyment += utility.get_int_value_array(values["enjoyment"],tmp_sequence[y].split())

        if tmp_cost <= max_value and highest_enjoyment <= tmp_enjoyment:
            highest_sequence = tmp_sequence.copy()
            highest_enjoyment = tmp_enjoyment
            cost = tmp_cost
        
    return highest_enjoyment, highest_sequence , cost

def main():
    
    file = utility.get_file()
    #get constraint to use
    max_constraint_value = utility.get_target(get_constraint())
    print(max_constraint_value)
    #then get the activties 
    list_activitys = utility.get_activites(file)
    print(list_activitys)
    n_activities = utility.get_number_activities(file)
    print(brute_force(list_activitys,max_constraint_value,n_activities))
#calculate cost per value ie time per enjoyment 
#then make sure constraint can be filled 

main()
