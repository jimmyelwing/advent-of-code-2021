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
        right = xposition + 1, yposition
        left = xposition - 1, yposition
        down = xposition, yposition + 1
        up = xposition, yposition - 1

        if xposition == 0:
            if yposition == 0:
                adjacentNumbers = GetNumbers(positions, (down, right))
            if yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (down, right, up))
            if yposition == numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (right, up))
        elif xposition > 0 and xposition < maxLengthOfRow:
            if yposition == 0:
                adjacentNumbers = GetNumbers(positions, (down, right, left))
            elif yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (up, right, left, down))
            elif xposition < maxLengthOfRow and yposition == numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (right, left, up))
        elif xposition == maxLengthOfRow:
            if yposition == 0:
                adjacentNumbers = GetNumbers(positions, (down,left))
            if yposition > 0 and yposition < numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (down,left,up))
            elif yposition == numberOfRows - 1:
                adjacentNumbers = GetNumbers(positions, (left, up))

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

def GetNumbers(positions, directions):
    adjacentNumbers = []
    for i in directions:
        adjacentNumbers.append(int(positions[i]))
    return adjacentNumbers 

if __name__ == "__main__":
    main()
