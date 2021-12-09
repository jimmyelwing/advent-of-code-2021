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

    numberOfRows -= 1
    
    leastNumbers = []

    # (0, 0): 2
    # (0, 1): 1

    adjacentNumbers = []

    for i in positions:
        number = int(positions[i])
        xposition = i[0]
        yposition = i[1]
    
        test1 = 0
        count = 0

        if xposition == 0 and yposition == 0:
            adjacentNumber1 = int(positions[xposition, (yposition + 1)])
            adjacentNumber2 = int(positions[(xposition + 1), yposition])

            if number < adjacentNumber1 and number < adjacentNumber2:
                adjacentNumbers.append(number)

        elif xposition > 0 and yposition == 0 and xposition < maxLengthOfRow:
            adjacentNumber1 = int(positions[xposition, (yposition + 1)])
            adjacentNumber2 = int(positions[(xposition + 1), yposition])
            adjacentNumber3 = int(positions[(xposition - 1), yposition])
            if number < adjacentNumber1 and number < adjacentNumber2 and number < adjacentNumber3:
                adjacentNumbers.append(number)
            # add

        elif (xposition == maxLengthOfRow and yposition == 0):
            adjacentNumber1 = int(positions[xposition, yposition + 1])
            adjacentNumber2 = int(positions[(xposition - 1), yposition])

            if number < adjacentNumber1 and number < adjacentNumber2:
                adjacentNumbers.append(number)

        elif xposition == 0 and yposition > 0 and yposition < numberOfRows:
            adjacentNumber1 = int(positions[xposition, (yposition + 1)])
            adjacentNumber2 = int(positions[(xposition + 1), yposition])
            adjacentNumber3 = int(positions[xposition, (yposition - 1)])

            if number < adjacentNumber1 and number < adjacentNumber2 and number < adjacentNumber3:
                adjacentNumbers.append(number)

        elif xposition > 0 and yposition > 0 and xposition < maxLengthOfRow and yposition < numberOfRows:
            adjacentNumber1 = int(positions[xposition, (yposition + 1)])
            adjacentNumber2 = int(positions[(xposition + 1), yposition])
            adjacentNumber3 = int(positions[(xposition - 1), yposition])
            adjacentNumber4 = int(positions[xposition, (yposition-1)])
            if number < adjacentNumber1 and number < adjacentNumber2 and number < adjacentNumber3 and number < adjacentNumber4:
                adjacentNumbers.append(number)
            # add

        elif (xposition == maxLengthOfRow and yposition > 0 and yposition < numberOfRows):
            adjacentNumber1 = int(positions[xposition, yposition + 1])
            adjacentNumber2 = int(positions[(xposition - 1), yposition])
            adjacentNumber3 = int(positions[xposition, (yposition - 1)])
            
            if number < adjacentNumber1 and number < adjacentNumber2 and number < adjacentNumber3:
                adjacentNumbers.append(number)
            
        elif xposition == 0 and yposition == numberOfRows:
            adjacentNumber2 = int(positions[(xposition + 1), yposition])
            adjacentNumber3 = int(positions[xposition, (yposition - 1)])

            if number < adjacentNumber2 and number < adjacentNumber3:
                adjacentNumbers.append(number)

        elif xposition > 0 and xposition < maxLengthOfRow and yposition == numberOfRows:
            adjacentNumber2 = int(positions[(xposition + 1), yposition])
            adjacentNumber3 = int(positions[(xposition - 1), yposition])
            adjacentNumber4 = int(positions[xposition, (yposition-1)])
            if number < adjacentNumber2 and number < adjacentNumber3 and number < adjacentNumber4:
                adjacentNumbers.append(number)
            # add

        elif (xposition == maxLengthOfRow and yposition == numberOfRows):
            adjacentNumber2 = int(positions[(xposition - 1), yposition])
            adjacentNumber3 = int(positions[xposition, (yposition - 1)])
            
            if number < adjacentNumber2 and number < adjacentNumber3:
                adjacentNumbers.append(number)


    totalSum = sum([i + 1 for i in adjacentNumbers])
    
    print(totalSum)


if __name__ == "__main__":
    main()
