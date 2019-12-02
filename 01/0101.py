import os
os.chdir(os.path.dirname(__file__))
total = 0
with open("input", "r") as fh_:
    for line in fh_:
        total += int(int(line.strip())/3) - 2
print(total)