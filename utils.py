def load_file(file):
    with open(file,"r",encoding = "utf8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines
