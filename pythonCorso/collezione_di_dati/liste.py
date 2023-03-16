# Le liste sono collezioni dordinate e modificabili. Permettono duplicati

# - spiegazione termini
    # -ordinato: la collezione ha ordine ben definito e l'aggiunta di elemnti non incide (index)
    # -indicizzato: possimao accedere agli elementi tramite indice (index)
    # -modificabile: possiamo aggiungere , cambiare e rimuovere elementi una volta creata la tabella
    # -immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    # -permette duplicati: possono esserci elementi con lo stesso valore
    
x = ["milano", "roma", "napoli", "venezia"]
y = ["ciao", 909, False]

# ci da il tipo di collezione di dati che è in questo caso sono liste
# print(type(x))
# print(type(y))

# lunghezza della lista: quantità degli elementi ch eci sono nella lista
# print(len(x))
# print(len(y))

# si può creare una lista anche con il costruttore list()
z = list(("milano", "roma", "napoli"))
# print(type(z))


# per ACCEDERE AGLI ELEMENTI DELLA LISTA CON SINGOLO INDICE, RANGE, NEGATIVO
# print(x[1])
# print(x[:-1])

# modificare utilizzando gli inidici o il range
# x[1:3] = ["lozzo", "bergamo"]
# print(x)

# con .append 'appendo' in fondo l'elemento che sto aggiungendo
x.append('lozzo')

# con .insert usiamo un numero per decidere dove inserire l'elmento 
x.insert(1, "brescia")
print(x)

# con .extend andiamo a fare un append ma di una nuova lista che già esiste
y = ["brescia", "udine"]
x.extend(y)
print(x)

# con .remove scelgo quale elmento togliere indicandolo 

# con .pop vado ad eliminare qualunque elmento si trovi in ultima posizione o se gli do unindice mi rimuove l'elemento con quel indice

# con .clear vado proprio a svuotare la lista ma questa continuerà ad esistere come un array vuoto []

# ciclare la lista

for citta in x:
    print(citta)
print("STOP")
    
for i in range(len(x)):
    print(x[i])
print("STOP")

i = 0
while i < len(x):
    print(x[i])
    i += 1
print("STOP")


# list coprehension
lista_citta = ["udine", "roma", "verona", "pordenone"]
j = ["milano" for citta in lista_citta if citta != "roma"]
print(j)
# [expression for item in lista if condizione == True]

# .sort mi organizza in ordine alfabetico o numerico la lista con .sort(reverse=True) in senso decrescente
lista_citta.sort()
print(lista_citta)
lista_citta.sort(reverse=True)
print(lista_citta)

# per unire più liste insieme : +, appen() che rihciede un cilco while, extend()



# esercizio 
print('----------------esercizi-----------------')
list = [3, 6, 7, 8 , 11, 32, 33]
for numero in list:
    if numero % 3 == 0: print(numero)