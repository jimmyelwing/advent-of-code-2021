def main():
    # inputs = "[({(<(())[]>[[{[]{<()<>>\n[(()[<>])]({[<{<<[]>>(\n{([(<{}[<>[]}>{[]{[(<()>\n(((({<>}<{<{<>}{[]{[]{}\n[[<[([]))<([[{}[[()]]]\n[{[{({}]{}}([{[{{{}}([]\n{<[[]]>}<{[{[{[]{()[[[]\n[<(<(<(<{}))><([]([]()\n<{([([[(<>()){}]>(<<{{\n<{([{{}}[<[[[<>{}]]]>[]]"
    # inputs = inputs.split("\n")
    
    inputs = open("inputs/day-10.txt", "r").read().split("\n")

    print(PartOne(inputs)) # 26397 / 367227
    print(PartTwo(inputs)) # 288957 / 3583341858
    
def PartOne(inputs):
    symbols = ("[", "]"), ("(", ")"), ("{", "}"), ("<", ">")
    
    
    firstIncorrectClosingCharacters = []
    for row in inputs:
        rowSymbols = []
        for symbol in row:
            if symbol in [x[0] for x in symbols]:
                rowSymbols.append(symbol)
            else:
                latestSymbol = rowSymbols[-1]
                closingSymbol = [x[1] for x in symbols if x[0] == latestSymbol]
                if symbol == closingSymbol[0]:
                    rowSymbols.pop()
                else:
                    firstIncorrectClosingCharacters.append(symbol)
                    break
    
    totalSum = 0
    for i in firstIncorrectClosingCharacters:
        if i == ")":
            totalSum += 3
        if i == "]":
            totalSum += 57
        if i == "}":
            totalSum += 1197
        if i == ">":
            totalSum += 25137
            
    return totalSum 
    
def PartTwo(inputs):
    symbols = ("[", "]"), ("(", ")"), ("{", "}"), ("<", ">")
    
    
    incorrectRows = []
    for row in inputs:
        rowSymbols = []
        for symbol in row:
            if symbol in [x[0] for x in symbols]:
                rowSymbols.append(symbol)
            else:
                latestSymbol = rowSymbols[-1]
                closingSymbol = [x[1] for x in symbols if x[0] == latestSymbol]
                if symbol == closingSymbol[0]:
                    rowSymbols.pop()
                else:
                    incorrectRows.append(row)
                    break
    incompleteRows = inputs
    for i in incorrectRows:
        if i in incompleteRows:
            incompleteRows.remove(i)
    
    missingsClosings = []
    missingClosingsPerRow = []
    incompleteRowsMissingClosing = []
    for row in incompleteRows:
        rowSymbols = []
        for symbol in row:
            if symbol in [x[0] for x in symbols]:
                rowSymbols.append(symbol)
            else:
                latestSymbol = rowSymbols[-1]
                closingSymbol = [x[1] for x in symbols if x[0] == latestSymbol]
                if symbol == closingSymbol[0]:
                    rowSymbols.pop()
                else:
                    incorrectRows.append(row)
                    break
        incompleteRowsMissingClosing.append(rowSymbols)
                
    for row in incompleteRowsMissingClosing:
        missingsClosings = []
        for i in row:
            closingSymbol = [x[1] for x in symbols if x[0] == i]
            missingsClosings.append(closingSymbol)
        missingClosingsPerRow.append(missingsClosings)
    
    scorePerLine = []
    for i in missingClosingsPerRow:
        totalScore = 0
        for y in reversed(i):
            totalScore *= 5
            if (y[0] == ")"):
                totalScore += 1
            if y[0] == "]":
                totalScore += 2
            if y[0] == "}":
                totalScore += 3
            if y[0] == ">":
                totalScore += 4
        scorePerLine.append(totalScore)
    
    scorePerLine = sorted(scorePerLine)
    totalScore = scorePerLine[int(abs(len(scorePerLine)/2))]
    
    return totalScore 
    
    
if __name__ == "__main__":
    main()