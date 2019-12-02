import os
os.chdir(os.path.dirname(__file__))


def main():
    with open("input", "r") as fh:
        program = [int(x) for x in fh.read().split(',')]
    
    # Set up for 0201-specific
    program[1] = 12
    program[2] = 2

    run_program(program)
    print(','.join(str(x) for x in program))
    print(program[0])


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