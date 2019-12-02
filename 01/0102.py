import os
os.chdir(os.path.dirname(__file__))

def fuel_needed(mass):
    return(int(int(mass)/3) - 2)



total = 0
with open("input", "r") as fh_:
    for line in fh_:
        fuel = fuel_needed(int(line.strip()))

        while fuel > 0:
            total += fuel
            fuel = fuel_needed(fuel)
print(total)