def count_words(filePath):
    with open(filePath) as f:
        file_contents = f.read()
    spl = file_contents.split();
    return len(spl)

def create_dictionary(filePath):
    letterDict = {}
    with open(filePath) as f:
        file_contents = f.read()
    words = file_contents.split()
    for word in words:
        word = word.lower()
        for i in word:
            if (i in letterDict.keys()):
                letterDict[i] = letterDict[i] + 1
            else:
                letterDict[i] = 1
    return letterDict

def sort_on(items):
    return items["num"]

def create_ordered_dicts(bigDict):
    littleDicts=[]
    for i in bigDict.keys():
        littleDict = {}
        letter = i
        count = bigDict[i]
        littleDict["char"] = letter
        littleDict["num"] = count
        littleDicts.append(littleDict)
    littleDicts.sort(reverse=True, key=sort_on)
    return(littleDicts)
