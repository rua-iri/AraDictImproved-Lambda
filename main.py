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







# testing below
blah = WordSolution('a', 'b', 'c', 'd', 'e')
print(blah)
print(blah.__str__())
print(blah.__repr__())

