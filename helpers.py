from wordModels import WordCombination
import sqlite3

con = sqlite3.connect('aramorph.sqlite')

def runQuery(wordCombination: WordCombination):
    cursor = con.cursor()

    selectQuery = """SELECT DISTINCT 
    CONCAT(prefixes.VOC_FORM, stems.VOC_FORM, suffixes.VOC_FORM) AS VOC_FORM, 
    prefixes.GLOSS AS PRE_GLOSS, 
    stems.GLOSS AS STE_GLOSS, 
    suffixes.GLOSS AS SUF_GLOSS, 
    CONCAT(prefixes.POS_NICE, ', ', stems.POS_NICE, ', ', suffixes.POS_NICE) AS POS, 
    stems.ROOT, 
    stems.MEASURE 
    FROM stems 
    INNER JOIN tableAB 
    ON stems.CAT_ID=tableAB.stemCatId 
    INNER JOIN prefixes 
    ON tableAB.prefCatID=prefixes.CAT_ID 
    INNER JOIN tableBC 
    ON stems.CAT_ID=tableBC.stemCatID 
    INNER JOIN suffixes 
    ON tableBC.suffCatID=suffixes.CAT_ID 
    WHERE BINARY prefixes.FORM='%1$s' 
    AND BINARY stems.FORM='%2$s' 
    AND BINARY suffixes.FORM='%3$s' 
    AND EXISTS (SELECT * FROM tableAC WHERE tableAC.prefCatID=prefixes.CAT_ID AND tableAC.suffCatID=suffixes.CAT_ID);"""

    queryValues = (wordCombination.prefix, wordCombination.stem, wordCombination.suffix, )
    res = cursor.execute(selectQuery, queryValues)

    result = res.fetchall()

    for r in result:
        print(r)


