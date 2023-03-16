# formattazione Stringa
#  - formattazione base
#  - valori multipli
#  - indici
#  - indici nominali

peso = 74
altezza = 184
frase = "Ciao sono Michele e sono alto {}cm"

# posso formattare una stringa e salvarla in una variabile

frase = frase.format(altezza)
print(frase)

# o posso formattare una stringa direttamente in un print  e anceh in questo caso devo mettere in ordine a come poi verranno inseriti nella frase. in questo caso ho due valori.
frase1 = "Ciao sono Michele e sono alto {}cm, e peso {}kg"
print(frase1.format(altezza, peso))

# adesso utilizzo gl indici per indicare cosa e dove inserirlo
peso = 66
altezza = 180
eta = 21
frase2 = "Ciao sono Luca ho {1} anni e sono alto {0} cm per un peso di {2}kg"
# adesso nel print inserisco le info che voglio poi la frase vada a prendere: altezza avrà indice 0, eta 1 e peso 2. 
print(frase2.format(altezza, eta, peso))
