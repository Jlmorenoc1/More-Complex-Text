numofTexts= int(input("Number of texts: "))
awlList=[]
textList = []
for i in range(numofTexts):
    word = input("Text: ")
    awl = len(word.split())/len(word)
    awlList.append(awl)
    textList.append(word)
lowawl = min(awlList)
lowawlIndex = awlList.index(lowawl)
lowword = textList[lowawlIndex]
print("The most complext text is: ", lowawlIndex + 1)