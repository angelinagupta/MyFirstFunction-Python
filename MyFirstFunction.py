def countingWords():
    fileName = input("Enter the full path of a file")
    wordCount = 0
    file = open(fileName, 'r')
    for line in file:
        words  = line.split()
        wordCount = wordCount + len(words)
    
    print(wordCount)

countingWords()