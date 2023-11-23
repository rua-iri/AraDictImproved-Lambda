from wordModels import WordSolution, SegmentedWord, WordCombination
import helpers

harakatList = ["َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ"]


def runAnalyser(arabicWord: str) -> list[str]:
    arabicWord = removeDiacritics(arabicWord)
    solutionsList = []
    possibleSegments = segmentWord(arabicWord)


    # Iterate through each possible segment combination
    for segment in possibleSegments:
        prefix: str = segment.prefix
        stem: str = segment.stem
        suffix: str = segment.suffix


        wordCombination = WordCombination(prefix=prefix, stem=stem, suffix=suffix)
        helpers.runQuery(wordCombination=wordCombination)



"""
Remove all short vowels from the word so that the
database can be queried without issue
"""
def removeDiacritics(word: str) -> str:
    for haraka in harakatList:
        word.replace(haraka, "")

    return word



"""
Splits a word in prefix + stem + suffix combinations.
Find all possible combinations to make up word
"""
def segmentWord(word: str) -> set:
    possibleSegments = set()
    prefixLength: int = 0
    suffixLength: int = 0

    while prefixLength <= 4 and prefixLength < len(word):
        prefix: str = word[:prefixLength]
        stemLength: int = len(word) - prefixLength
        suffixLength = 0

        while stemLength >= 1 and suffixLength <= 6:
            stem: str = word[prefixLength:prefixLength+stemLength]
            suffix: str = word[prefixLength+stemLength:prefixLength+stemLength+suffixLength]
            possibleSegments.add(SegmentedWord(prefix=prefix, stem=stem, suffix=suffix))
            stemLength-=1
            suffixLength+=1
        
        prefixLength+=1
    
    return possibleSegments




if __name__=="__main":
    runAnalyser('العربية')



