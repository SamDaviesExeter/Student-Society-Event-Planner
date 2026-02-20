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

def val_per_enjoyment(activity,position):
    # get the enjoyment 
    # get the value to be computed with position
    array = activity.split()
    enjoyment = array[values["enjoyment"]]
    value = array[position]
    return float(enjoyment) / float(value)

def dynamic_programming(activities, max_value, amount):
    field_index = get_value()
    dp = [[0] * (max_value + 1) for _ in range(amount + 1)]

    for i in range(1, amount + 1):
        parts = activities[i - 1].split()
        activity_cost = int(parts[field_index])
        activity_enjoyment = int(parts[values["enjoyment"]])

def main():
    #SUGGESTION
    #maybe use a linked list to then get the highest value per with val_per_enjoyment
    #if cost IE budget is not maximised maybe try diff combos with pairs close by in enjoyment / value
    ...


if __name__ == "__main__":
    main()
