import polars as pl
# vérifier que suite croissante et pas plus de 2

test1 = (11,12,15,19,18)

df = pl.read_clipboard(has_header=False, separator=' ')

def prob(row:tuple) -> bool :

    liste = row[0]

    n_decrease = 0
    n_increase = 0

    for n, i in enumerate(liste) :

        if n == len(liste) - 1 :
            break

        # print(f"comparaison : {liste[n]} et {liste[n+1]}")

        n_decrease = n_decrease + 1 if liste[n] < liste[n+1] else n_decrease
        n_increase = n_increase + 1 if liste[n] > liste[n+1] else n_increase

        if liste[n] == liste[n+1] or abs(liste[n] - liste[n+1]) > 3 :
            return False

        if n_decrease > 0 and n_increase > 0 :
            return False

    return True

prob(test1)

test = df.map_rows(prob)
test.sum()

# test final
df = pl.read_clipboard(has_header=False)

def string_to_list(str_val:tuple) -> tuple :
    return [int(var) for var in str_val[0].split()],

df2 = df.map_rows(string_to_list)
df3 = df2.map_rows(prob)

df3.sum()