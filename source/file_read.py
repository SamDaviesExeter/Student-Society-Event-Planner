

def read_file(file:str)-> list[str]:
    with open(file, "r") as f:
        file_array = f.read().splitlines()

    return file_array

def split_lines(array:list):
    number_act = array[0]
    constraints = array[1]
    activites = array[2:]
    return number_act, constraints, activites

def split_constraints(constraints:str)-> list:
    return constraints.split()


print(split_constraints("10 200"))
