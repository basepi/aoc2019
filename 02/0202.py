import os
os.chdir(os.path.dirname(__file__))


def main():
    with open("input", "r") as fh:
        original_program = [int(x) for x in fh.read().split(',')]
    
    for x in range(100):
        for y in range(100):
            program = original_program[:]
            program[1] = x
            program[2] = y
            run_program(program)
            if program[0] == 19690720:
                print(x*100 + y)
                return


def run_program(program):
    pos = 0
    while program[pos] != 99 and pos < len(program):
        code = program[pos]
        if code == 1:
            x = program[program[pos + 1]]
            y = program[program[pos + 2]]
            program[program[pos + 3]] = x + y
        elif code == 2:
            x = program[program[pos + 1]]
            y = program[program[pos + 2]]
            program[program[pos + 3]] = x * y
        else:
            raise Exception(f"Unknown code found: {code}")

        pos += 4


if __name__ == "__main__":
    main()