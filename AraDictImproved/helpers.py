from wordModels import WordCombination, WordSolution
import sqlite3
import constants

con = sqlite3.connect('aramorph.sqlite')
con.row_factory = sqlite3.Row
selectQuery = constants.DB_SELECT_QUERY

def runQuery(wordCombination: WordCombination):
    cursor = con.cursor()
    queryValues = (wordCombination.prefix, wordCombination.stem, wordCombination.suffix, )
    
    res = cursor.execute(selectQuery, queryValues)

    result = res.fetchall()

    for r in result:

        glossMeaning: str = r['PRE_GLOSS']

        if '<verb>' in r['SUF_GLOSS']:
            glossMeaning += ' ' + r['SUF_GLOSS']
            glossMeaning.replace('<verb>', r['STE_GLOSS'])
        else:
            glossMeaning += ' ' + r['STE_GLOSS'] 
            glossMeaning += ' ' + r['SUF_GLOSS']

        wordSolution = WordSolution(
            phoneticSpelling=r['VOC_FORM'], 
            meaning=glossMeaning, 
            tense=r['POS'], 
            root=r['ROOT'],
            verbForm=r['MEASURE'])
        
        wordCombination.addSolution(wordSolution)

        
        




