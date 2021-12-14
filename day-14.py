from collections import Counter

def main():
    #inputs = "NNCB\n\nCH -> B\nHH -> N\nCB -> H\nNH -> C\nHB -> C\nHC -> B\nHN -> C\nNN -> C\nBH -> H\nNC -> B\nNB -> B\nBN -> B\nBB -> N\nBC -> B\nCC -> N\nCN -> C"
    inputs = open("inputs/day-14.txt", "r").read()

    result1 = PartOne(inputs)
    # result = PartTwo(inputs)
    
    print("Part one", result1) # 1588 / 3247
 

def PartOne(inputs) -> int:
    polymeterTemplate, *pairInsertions = inputs.splitlines()
    pairInsertions = list(filter(None, pairInsertions))
    
    count = 0
    string = polymeterTemplate
    while count < 10:
        string = GetString(string, pairInsertions)
        count += 1
    
    res = Counter(string)
    mostFrequent, lessFrequent = max(res, key = res.get), min(res, key = res.get)
    mostFrequentCount = len([i for i in string if i == mostFrequent])
    lessFrequentCount = len([i for i in string if i == lessFrequent])
    
    result = mostFrequentCount - lessFrequentCount

    return result

def PartTwo(inputs) -> int:
    test = 0
    

def GetString(polymeterTemplate, pairInsertions) -> str:
    newPosition = 0
    newString = ""
    string = ""
    for x in polymeterTemplate:
        letters = polymeterTemplate[newPosition:newPosition+2]
        for i in pairInsertions:
            letters2, insert = i.split(" -> ")
            if letters2 == letters:
                if string == "":
                    newString = letters[:1] + insert + letters[-1]
                else:
                    newString += insert + letters[-1]
                string = newString
        newPosition += 1
    
    return string
    
if __name__ == "__main__":
    main()