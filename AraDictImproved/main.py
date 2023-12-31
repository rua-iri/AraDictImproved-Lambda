from cProfile import Profile
from functools import wraps
import json
from pstats import SortKey, Stats
from wordModels import SegmentedWord, WordCombination
import helpers

# harakatList = ["َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ"]
harakatList = ["َ", "ً", "ُ", "ٌ", "ِ", "ٍ", "ْ", "ّ"]

def lambda_handler(event, context):
    lookupWord = event['queryStringParameters'].get('word')
    wordMeanings = runAnalyser(lookupWord)

    if(wordMeanings==[]):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "No Meanings Found"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps(wordMeanings)
        }


def profile(func):
    """Decorator to profile a function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = Profile()
        result = profiler.runcall(func, *args, **kwargs)
        stats = Stats(profiler)
        stats.sort_stats(SortKey.TIME)
        stats.print_stats()
        return result

    return wrapper

@profile
def runAnalyser(arabicWord: str) -> list[str]:
    arabicWord = removeDiacritics(arabicWord)
    solutionsList: list = []
    possibleSegments = segmentWord(arabicWord)

    # Iterate through each possible segment combination
    for segment in possibleSegments:
        prefix: str = segment.prefix
        stem: str = segment.stem
        suffix: str = segment.suffix

        wordCombination = WordCombination(prefix=prefix, stem=stem, suffix=suffix)
        helpers.runQuery(wordCombination=wordCombination)

        try: 
            for solution in wordCombination.combinationSolutions:
                print(solution.toDict())
                solutionsList.append(solution.toDict())
        except Exception as e:
            print(e)
        
    return solutionsList



"""
Remove all short vowels from the word so that the
database can be queried without issue
"""
def removeDiacritics(word: str) -> str:
    for haraka in harakatList:
        word = word.replace(haraka, "")

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


