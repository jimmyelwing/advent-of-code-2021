def main():
    # inputs = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
    # inputs = inputs.split("\n")

    inputs = open("inputs/day-9.txt", "r").read().split("\n")

    # this is a list of numbers, new line for each row of numbers

    positions = {}
    county = 0

    maxLengthOfRow = len(inputs[0]) - 1
    numberOfRows = 0
    for row in inputs:
        numberOfRows += 1
        countx = 0

        for number in row:
            x = countx
            y = county
            positions[x, y] = number
            countx += 1

        county += 1

    adjacentNumbers = []
    totalSum = 0

    for i in positions:
        number = int(positions[i])
        xposition = i[0]
        yposition = i[1]
        moveRight = xposition + 1
        moveLeft = xposition - 1
        moveDown = yposition + 1
        moveUp = yposition - 1

        if xposition == 0:
            if yposition == 0:
                adjacentNumbers = int(positions[xposition, moveDown]), int(
                    positions[moveRight, yposition])
            if yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = int(positions[xposition, moveDown]), int(
                    positions[moveRight, yposition]), int(positions[xposition, moveUp])
            if yposition == numberOfRows - 1:
                adjacentNumbers = int(positions[moveRight, yposition]), int(
                    positions[xposition, moveUp])
        elif xposition > 0 and xposition < maxLengthOfRow:
            if yposition == 0:
                adjacentNumbers = int(positions[xposition, moveDown]), int(
                    positions[moveRight, yposition]), int(positions[moveLeft, yposition])
            elif yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = int(positions[xposition, moveDown]), int(positions[moveRight, yposition]), int(
                    positions[moveLeft, yposition]), int(positions[xposition, (yposition-1)])
            elif xposition < maxLengthOfRow and yposition == numberOfRows - 1:
                adjacentNumbers = int(positions[moveRight, yposition]), int(
                    positions[moveLeft, yposition]), int(positions[xposition, (yposition-1)])
        elif xposition == maxLengthOfRow:
            if yposition == 0:
                adjacentNumbers = int(
                    positions[xposition, moveDown]), int(positions[moveLeft, yposition])
            if yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = int(positions[xposition, moveDown]), int(
                    positions[moveLeft, yposition]), int(positions[xposition, moveUp])
            elif yposition == numberOfRows - 1:
                adjacentNumbers = int(
                    positions[moveLeft, yposition]), int(positions[xposition, moveUp])

        if any(adjacentNumbers):
            smaller = False
            for i in adjacentNumbers:
                if number > i:
                    smaller = False
                    break
                elif number < i:
                    smaller = True
            if smaller:
                totalSum += number + 1

    print(totalSum)


if __name__ == "__main__":
    main()
