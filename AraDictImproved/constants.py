

DB_SELECT_QUERY="""SELECT DISTINCT 
prefixes.VOC_FORM || stems.VOC_FORM || suffixes.VOC_FORM AS VOC_FORM,
prefixes.GLOSS AS PRE_GLOSS, 
stems.GLOSS AS STE_GLOSS, 
suffixes.GLOSS AS SUF_GLOSS, 
prefixes.POS_NICE || ', ' || stems.POS_NICE || ', ' || suffixes.POS_NICE AS POS, 
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
WHERE prefixes.FORM=(?) 
AND stems.FORM=(?) 
AND suffixes.FORM=(?) 
AND EXISTS 
(SELECT * 
FROM tableAC 
WHERE tableAC.prefCatID=prefixes.CAT_ID 
AND tableAC.suffCatID=suffixes.CAT_ID);"""