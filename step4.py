import numpy as np

# Exemple
text = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
text2 = text.strip()
# numpy with it ?
    
# Split the text into lines and then into characters
text_matrix = np.array([list(line) for line in text2.split('\n')])

# Méthode :
# on déroule toute la matrice
# pour tout X, on va regarder dans chaque direction si la lettre suivante est M
# on doit faire attention à pas dépasser la taille de la matrice

def calculer_nb_xmas_at_position(xpos, ypos, text_matrix) :

    nb_xmas = 0

    #pas de x en position initiale
    if text_matrix[xpos,ypos] != 'X' :
        return nb_xmas

    for x in range(-1,2) :
        for y in range(-1,2) :

            # éviter les bords supérieurs avec numpy qui renvoie l'autre côté avec un index négatif
            if xpos + x * 3 < 0 or ypos + y * 3 < 0 or (x== 0 and y == 0) :
                continue 

            try : 
                sortie = (
                    text_matrix[xpos,ypos] + 
                    text_matrix[xpos + x,ypos + y] + 
                    text_matrix[xpos + x * 2,ypos + y * 2] + 
                    text_matrix[xpos + x * 3,ypos + y * 3]
                ) 

                # print(sortie)

                if sortie == 'XMAS' :
                    nb_xmas = nb_xmas + 1
            except :
                sortie = 'prob'

            # print(sortie)

    return nb_xmas


nb_xmas_total = 0

for xpos in range(0,text_matrix.shape[0]) :
    for ypos in range(0,text_matrix.shape[1]) :

        nb_xmas_total = nb_xmas_total + calculer_nb_xmas_at_position(xpos, ypos, text_matrix)

print(nb_xmas_total)

# Cas réel
with open('step4_text.txt', 'r') as file:
    data = file.read()
data2 = data.strip().split("\n")

# Split the text into lines and then into characters
text_matrix = np.array([list(line) for line in data2])

nb_xmas_total = 0

for xpos in range(0,text_matrix.shape[0]) :
    for ypos in range(0,text_matrix.shape[1]) :

        nb_xmas_total = nb_xmas_total + calculer_nb_xmas_at_position(xpos, ypos, text_matrix)

print(nb_xmas_total)
