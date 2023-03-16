# I set sono collezioni non ordinate e perciò non indicizzate. Non permettono duplicati

# - spiegazione termini
    # -ordinato: la collezione ha ordine ben definito e l'aggiunta di elemnti non incide (index)
    # -indicizzato: possimao accedere agli elementi tramite indice (index)
    # -modificabile: possiamo aggiungere , cambiare e rimuovere elementi una volta creata la tabella
    # -immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    # -permette duplicati: possono esserci elementi con lo stesso valore
    
x = {"milano", "roma", "napolo"}
print(type(x))
print(len(x))

# si può usare set() com ecostruttore 
y = set(("parigi", "londra", "berlino"))
print(y)

# l'unico modo per accedere agli elmenti è il loop ma verranno sempre presenttai inmood diverso il che dimostra ch eon sono ordinati. 

for citta in x:
    print(citta)


# con .add() e .update() possimao agggiungere elementi
y = {"venezia", "lozzo"}
x.add("verona")
print(x)

x.update(y)
print(x)

# per rimuoverli abbimao diversi elmenti utilizzabili .remove(), .discard(), .pop(), .clear(), del

# per unire si possono usare 
# .union() union va a crare un nuovo set quidn igli devo dar eun nuovo nome e va ad escludere gli elemnti duplicati
# .update() unisce gli elmenti e va ad escludere gli elemnti duplicati 
# .intersection_update() aggiorna un set che abbiamo già ma prende solo i duplicati, se non ci sono no nli prende
# .intersection() va  a prendere i duplicati e quind i valoroi in comune e li mette in un nuovo set
# .symmetric_difference_update() lavoara su un set già esistente e elimina i doppioni e non comparirà proprio
# .symmetric_difference() crea un nuovo set dove unisce gli elemnti ma cancella gli elemnti che sono doppi senza metterli
