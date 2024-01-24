
sampleParagraph = 'The cityscape is a bustling hive of activity as people are rushing to their destinations. Tall buildings are reaching towards the sky, and the streets are filled with the sounds of honking horns and the chatter of pedestrians. The atmosphere is charged with energy, and neon lights are illuminating the urban landscape. In the midst of the commotion, street vendors are setting up their stalls, and the aroma of various cuisines is wafting through the air. Despite the chaos, there is a sense of unity among the diverse crowd, and the city is a vibrant tapestry of different cultures and lifestyles.'
# =====================================================
toBeList = ['am', 'is', 'are', 'was', 'were']
sampleParagraph = sampleParagraph.replace('.', '').replace(',', '').lower()
wordList = sampleParagraph.split()
# =====================================================
totalWords = len(wordList)
# =====================================================
wordSet = set(wordList)
uniqueWords = len(wordSet)
# =====================================================
toBeCount = 0
for word in wordList:
    if word.lower() in toBeList:
        toBeCount += 1
# =====================================================
print('')
print('Total number of words: {}'.format(totalWords))
print('Number of unique words: {}'.format(uniqueWords))
print('Total number of \"to be\": {}'.format(toBeCount))
for toBe in toBeList:
    print('number of word \"{}\": {}'.format(toBe, wordList.count(toBe)))
