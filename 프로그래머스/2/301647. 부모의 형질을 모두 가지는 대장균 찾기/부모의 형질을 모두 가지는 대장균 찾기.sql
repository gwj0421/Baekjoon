SELECT ed1.ID AS ID,ed1.GENOTYPE AS GENOTYPE,ed2.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA ed1
JOIN ECOLI_DATA ed2 ON ed1.PARENT_ID = ed2.ID
WHERE ed1.GENOTYPE & ed2.GENOTYPE = ed2.GENOTYPE
ORDER BY ID ASC