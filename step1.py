import polars as pl
from math import abs

# Exemple
df = pl.DataFrame({'col1': [3, 4, 2, 1,3,3], 'col2': [4,3,5,3,9,3]})

# méthode :
# - sort les 2 colonnes
# - calcule la différence
# - somme
df2 = (
    df
    .with_columns(
        col1_sort = pl.col('col1').sort(),
        col2_sort = pl.col('col2').sort(),
    )
    .with_columns(
        diff = (pl.col('col1_sort') - pl.col('col2_sort')).abs(),
    )
)

df2.select(pl.sum("diff"))

# cas réel

# récupération à partir du clipboard
df = pl.read_clipboard(has_header=False)

# nettoyage
df2 = (
    df
    .with_columns(
        col_split = pl.col("column_1").str.split("   ").alias("split_str")
    )
    .with_columns(
        col1 = pl.col('col_split').list.get(0).cast(pl.Int64),
        col2 = pl.col('col_split').list.get(1).cast(pl.Int64),
    )
    .drop("column_1","col_split")
)

df2 = (
    df2
    .with_columns(
        col1_sort = pl.col('col1').sort(),
        col2_sort = pl.col('col2').sort(),
    )
    .with_columns(
        diff = (pl.col('col1_sort') - pl.col('col2_sort')).abs(),
    )
)

df2.select(pl.sum("diff"))