

input_file = "assets/input_small.txt"

def read_file(file:str)-> list[str]:
    with open(file, "r") as f:
        file_array = f.read().splitlines()

    return file_array

def split_lines(array:list):
    number_act = array[0]
    constraints = array[1]
    activites = array[2:]
    return number_act, constraints, activites

def get_file_path():
    return input_file

def get_file():
    return read_file(get_file_path())

def get_number_activities(array:list):
    return int(array[0])

def get_max_constraints(array:list):
    return array[1]

def get_activities(array:list):
    return array[2:]

def split_constraints(constraints:str)-> list[str]:
    return constraints.split() #time index 0 , budget index 1

def get_constranint(constraint:int,array:list[str])-> str:
    return array[constraint]

def get_targeted_constraint(file_path,choice):
    file = read_file(file_path)
    number_act, constraints, activites = split_lines(file)
    constraints_split = split_constraints(constraints)
    con = get_constranint(choice,constraints_split)
    return con

def get_target(choice):
    file = get_file()
    constraints = get_max_constraints(file)
    constraints_split = split_constraints(constraints)
    con = get_constranint(choice,constraints_split)
    return int(con)

def get_int_value_array(position,array):
    return int(array[position])

if __name__ == "__main__":
    ...
    
