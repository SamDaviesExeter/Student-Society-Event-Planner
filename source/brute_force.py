import utility

#FOCUS ON BUDGET
constraint = "budget"
constraints_position = {"time": 0,"budget": 1}
values = {"name": 0,"time ": 1, "cost": 2, "enjoyment": 3 }

input_file = "assets/input_small.txt"

def get_constraint(): # itterate threw a for loop for both values later for extra credit
    return constraints_position[constraint]

def get_value():
    if constraint == "budget":
        return values["cost"]
    elif constraint == "time":
        return values["time"]

def val_per_enjoyment(activity,position):
    # get the enjoyment 
    # get the value to be computed with position
    array = activity.split()
    enjoyment = array[values["enjoyment"]]
    value = array[position]
    return float(value) / float(enjoyment)

def main():
    file = utility.get_file()
#get constraint to use
    max_constraint_value = utility.get_target(get_constraint())
    values_position = get_value()
    print(max_constraint_value)
    print(values_position)
#then get the activties 
    list_activitys = utility.get_activites(file)
    print(list_activitys)
    for x in range(len(list_activitys)):
        v = val_per_enjoyment(list_activitys[x],values_position)
        print(v)
#calculate cost per value ie time per enjoyment 
#then make sure constraint can be filled 

main()
