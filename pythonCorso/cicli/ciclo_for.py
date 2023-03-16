# CICLO FOR
# serve ad iterare una sequenza: se abbiamo già una lista di elementi ad esempio

lista_citta = ["milano", "veneiza", "roma"]
# per ogni elemento citta nella collezione di elementi della lista_citta fai qualcosa: print(citta)
for citta in lista_citta:
    print(citta)
print("stop")

# cilco for con una stringa
stringa = "anguria"
for lettera in stringa:
    print(lettera)
print("stop")

# ciclo for con range

for x in range(6):
    print(x)
print("stop") 

# in questo caso il cilco for viene sempre fatto con il range ma con "continue" gli dico di saltare il valore con il tre e quando ha finito di stampare con l'else gli dico di scrivere "ho finito"
for x in range(6):
    if x == 3:
        continue
    print(x)
else:
    print("ho finito")
