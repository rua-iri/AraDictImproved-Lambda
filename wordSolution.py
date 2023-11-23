class WordSolution:
    def __init__(self, phoneticSpelling, meaning, tense, root, verbForm) -> None:
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
