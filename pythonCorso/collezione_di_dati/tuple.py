# Le tuple sono collezioni dordinate ma immutabili. Permettono duplicati

# - spiegazione termini
    # -ordinato: la collezione ha ordine ben definito e l'aggiunta di elemnti non incide (index)
    # -indicizzato: possimao accedere agli elementi tramite indice (index)
    # -modificabile: possiamo aggiungere , cambiare e rimuovere elementi una volta creata la tabella
    # -immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    # -permette duplicati: possono esserci elementi con lo stesso valore
    
x = ("milano", "roma", "napoli")
# print(type(x))
print(x)

# if "milano" in x:
#     print("ok")
    
# non si può modificare ma c'è un excamotage utilizzando i costrtturo list() e tuble()
y = list(x)
y[0] = "venzia"
x = tuple(y)
print(x)

lista_citta = x
for i in range(len(lista_citta)):
    print(lista_citta[i])
    
# per unire le tuple qui abbiamo a disposizione solo il +

# ci sono due metodi count() index()



# esercizio 
print('----------------esercizi-----------------')
x = ('ciao', 'nio', 'Lozzo', 'gatto', 'miao', 'domegge', 'napoli')
for string in x:
    if  len(string) % 2 == 0: 
        print(string)