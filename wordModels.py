

class SegmentedWord:    
    def __init__(self, prefix: str, stem: str, suffix: str) -> None:
        self.prefix: str = prefix
        self.stem: str = stem
        self.suffix: str = suffix



class WordSolution:
    def __init__(self, phoneticSpelling: str, meaning: str, tense: str, root:str, verbForm:str) -> None:
        self.phoneticSpelling: str = phoneticSpelling
        self.meaning: str = meaning
        self.tense: str = tense
        self.tense: str = self.setTense(tense)
        self.root: str = root
        self.verbForm: str = verbForm

    def setTense(self, tense: str) -> str:
        trueTense = tense
        if trueTense[0] == ",":
            trueTense = trueTense[2:]

        if len(trueTense) >= 2 and trueTense[-2] == ",":
            trueTense = trueTense[:-2]

        return trueTense

    def __str__(self) -> str:
        return (
            "WordSolution [phoneticSpell="
            + self.phoneticSpelling
            + ", meaning="
            + self.meaning
            + ", tense="
            + self.tense
            + ", root="
            + self.root
            + ", verbForm="
            + self.verbForm
            + "]"
        )



class WordCombination:
    def __init__(self, prefix, stem, suffix) -> None:
        self.prefix:str = prefix
        self.stem:str = stem
        self.suffix: str = suffix
        self.combinationSolutions: list = []

    def addSolution(self, solution):
        self.combinationSolutions.append(solution)

    def __str__(self) -> str:
        return "Prefix: " + self.prefix + "\nStem: " + self.stem + "\nSuffix: " + self.suffix;
        



