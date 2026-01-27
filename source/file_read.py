

def read_file(file):
    with open(file, "r") as f:
        file = f.readlines()
    f.close()
    return file

print(read_file("assets/input_small.txt"))