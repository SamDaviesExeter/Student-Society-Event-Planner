import file_opperations

#FOCUS ON BUDGET
constraint = "budget"
constraints_position = {"time": 0,"budget": 1}

def get_constraint(): # itterate threw a for loop for both values later
    return constraints_position[constraint]

constraint_value =file_opperations.get_targeted_constraint("assets/input_small.txt",get_constraint())


