

def read_file(file):
    try:
        with open(file, "r") as f:
            file = f.readlines()
            
    finally:
        f.close()
    return file

print(read_file("assets/input_small.txt"))