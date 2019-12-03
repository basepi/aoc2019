import os
os.chdir(os.path.dirname(__file__))


def main():
    with open("input", "r") as f:
        path1 = f.readline().strip().split(",")
        path2 = f.readline().strip().split(",")

    coord1 = calculate_coordinates(path1)
    coord2 = calculate_coordinates(path2)

    cross = coord1.keys() & coord2.keys()

    best = None
    best_coord = None
    for coord in cross:
        distance = coord1[coord] + coord2[coord]
        if not best or distance < best:
            best = distance
            best_coord = coord
        
    print(f"distance: {best}\ncoord: {best_coord}")


def calculate_coordinates(pth):
    """
    Create a set of tuples representing the coordinates that the path
    traverses, with a starting point at (0,0)
    """
    x = 0
    y = 0
    dist = 0
    coords = dict()
    for instruction in pth:
        direction = instruction[:1]
        distance = int(instruction[1:].strip())
        if direction.lower() == "d":
            for _ in range(distance):
                y -= 1
                dist += 1
                if (x, y) not in coords:
                    coords[(x, y)] = dist
        elif direction.lower() == "u":
            for _ in range(distance):
                y += 1
                dist += 1
                if (x, y) not in coords:
                    coords[(x, y)] = dist
        elif direction.lower() == "l":
            for _ in range(distance):
                x -= 1
                dist += 1
                if (x, y) not in coords:
                    coords[(x, y)] = dist
        elif direction.lower() == "r":
            for _ in range(distance):
                x += 1
                dist += 1
                if (x, y) not in coords:
                    coords[(x, y)] = dist
        else:
            raise Exception(f"Unknown direction {direction}")
    
    return coords


if __name__ == "__main__":
    main()