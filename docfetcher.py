myfile = open("entries.csv", "rt")

for line in myfile:
    print("\"" + line.rstrip("\n, ") + "\", ", end="")