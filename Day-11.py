def main():

    # inputs = "5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n4167524645\n2176841721\n6882881134\n4846848554\n5283751526"
    # rows = inputs.split("\n")

    inputs = open("inputs/day-11.txt", "r").read()
    rows = inputs.split("\n")
    
    countRow = 0
    octopuses = {}
    for row in rows:
        countColumn = 0
        positions = {}
        for octopus in row:
            x = countColumn
            positions[x, countRow] = int(octopus)
            countColumn += 1
        octopuses.update(positions)
        countRow += 1

    # increase energy level by one of each octopus

    count = 0
    allOctopusesFlashing = 0
    flashesAt100Steps = 0
    flashes = 0
    run = True
    
    while run:
        for i in octopuses:
            octopuses[i] += 1
            
        octopusesWithNineOrHigher = [i for i in octopuses if octopuses[i] > 9]
        while octopusesWithNineOrHigher:
            for x in list(octopusesWithNineOrHigher):
                adjacentLocations = GetAdjacentLocationsIncludingDiagonal(x, octopuses)
                for y in adjacentLocations:
                    energyLevel = octopuses[y]
                    if energyLevel != 0:
                        octopuses[y] += 1
                        energyLevel = octopuses[y]
                        if energyLevel > 9 and y not in octopusesWithNineOrHigher:
                            octopusesWithNineOrHigher.append(y)
                octopuses[x] = 0
                flashes += 1
                octopusesWithNineOrHigher = [i for i in octopuses if octopuses[i] > 9]
        
        octopusesFlashing = [i for i in octopuses if octopuses[i] == 0]
        if len(octopusesFlashing) == len(octopuses):
            run = False
            allOctopusesFlashing = count + 1
            
        count += 1
        if count == 100:
            flashesAt100Steps = flashes
        

    print(flashesAt100Steps) # 1617
    print(allOctopusesFlashing) # 258
    


def GetAdjacentLocationsIncludingDiagonal(location, heightMap):
    adjacentLocations = {}
    numberOfColumns, numberOfRows = max(heightMap)

    x, y = location
    right = x + 1, y
    left = x - 1, y
    down = x, y + 1
    up = x, y - 1
    upright = x + 1, y - 1
    upleft = x - 1, y - 1
    downright = x + 1, y + 1
    downleft = x - 1, y + 1

    if FirstColumn(x):
        if FirstRow(y):
            adjacentLocations = GetLocations(heightMap, (down, right, downright))
        elif MiddleRow(y, numberOfRows):
            adjacentLocations = GetLocations(heightMap, (down, downright, right, upright, up))
        elif LastRow(y, numberOfRows):
            adjacentLocations = GetLocations(heightMap, (right, upright, up))
    elif MiddleColumn(x, numberOfColumns):
        if FirstRow(y):
            adjacentLocations = GetLocations(heightMap, (down, downright, right, downleft, left))
        elif MiddleRow(y, numberOfRows):
            adjacentLocations = GetLocations(
                heightMap, (up, upright, right, downright, down, downleft, left, upleft))
        elif LastRow(y, numberOfRows):
            adjacentLocations = GetLocations(heightMap, (right, upright, up, upleft, left))
    elif LastColumn(x, numberOfColumns):
        if FirstRow(y):
            adjacentLocations = GetLocations(heightMap, (down, downleft, left))
        elif MiddleRow(y, numberOfRows):
            adjacentLocations = GetLocations(heightMap, (down, downleft, left, upleft, up))
        elif LastRow(y, numberOfRows):
            adjacentLocations = GetLocations(heightMap, (left, upleft, up))

    return adjacentLocations


def GetLocations(heightMap, positions):
    locations = {}
    for i in positions:
        locations[i] = heightMap[i]
    return locations


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