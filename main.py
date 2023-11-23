from wordSolution import WordSolution

harakatList = ["َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ"]


class SegmentedWord:
    
    def __init__(self, prefix: str, stem: str, suffix: str) -> None:
        self.prefix = prefix
        self.stem = stem
        self.suffix = suffix




def runAnalyser(arabicWord: str) -> list[str]:
    arabicWord = removeDiacritics(arabicWord)
    solutionsList = []

    



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
find all possible combinations to make up word
"""
def segmentWord(word) -> set:
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






# testing below
blah = WordSolution('a', 'b', 'c', 'd', 'e')
print(blah)
print(blah.__str__())

