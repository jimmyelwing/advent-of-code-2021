def main():
    inputs = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
    inputs = inputs.split("\n")

    inputs = open("inputs/day-9.txt", "r").read().split("\n")

    print(PartOne(inputs))

def PartOne(inputs):

    positions = GetPositionsFromInputs(inputs)
    numberOfColumns, numberOfRows = max(positions)

    adjacentNumbers = []
    totalSum = 0

    for position in positions:
        number = int(positions[position])
        x,y = position
    
        right = x + 1, y
        left = x - 1, y
        down = x, y + 1
        up = x, y - 1

        if FirstColumn(x):
            if FirstRow(y):
                adjacentNumbers = GetNumbers(positions, (down, right))
            elif MiddleRow(y, numberOfRows):
                adjacentNumbers = GetNumbers(positions, (down, right, up))
            elif LastRow(y, numberOfRows):
                adjacentNumbers = GetNumbers(positions, (right, up))
        elif MiddleColumn(x, numberOfColumns):
            if FirstRow(y):
                adjacentNumbers = GetNumbers(positions, (down, right, left))
            elif MiddleRow(y, numberOfRows):
                adjacentNumbers = GetNumbers(
                    positions, (up, right, left, down))
            elif LastRow(y, numberOfRows):
                adjacentNumbers = GetNumbers(positions, (right, left, up))
        elif LastColumn(x, numberOfColumns):
            if FirstRow(y):
                adjacentNumbers = GetNumbers(positions, (down, left))
            elif MiddleRow(y, numberOfRows):
                adjacentNumbers = GetNumbers(positions, (down, left, up))
            elif LastRow(y, numberOfRows):
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

    return totalSum

def GetPositionsFromInputs(inputs):
    positions = {}
    county = 0
    for row in inputs:
        countx = 0
        for number in row:
            x = countx
            y = county
            positions[x, y] = number
            countx += 1
        county += 1
        
    return positions


def GetNumbers(positions, directions):
    adjacentNumbers = []
    for i in directions:
        adjacentNumbers.append(int(positions[i]))
    return adjacentNumbers


def FirstRow(y):
    return y == 0


def MiddleRow(y, numberOfRows):
    return y > 0 and y < numberOfRows


def LastRow(y, numberOfRows):
    return y == numberOfRows


def FirstColumn(x):
    return x == 0


def MiddleColumn(x, numberOfColumns):
    return x > 0 and x < numberOfColumns


def LastColumn(x, numberOfColumns):
    return x == numberOfColumns


if __name__ == "__main__":
    main()
