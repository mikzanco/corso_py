# I dictionary sono collezioni dordinate e modificabili. Non permettono duplicati

# - spiegazione termini
    # -ordinato: la collezione ha ordine ben definito e l'aggiunta di elemnti non incide (index)
    # -indicizzato: possimao accedere agli elementi tramite indice (index)
    # -modificabile: possiamo aggiungere , cambiare e rimuovere elementi una volta creata la tabella
    # -immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    # -permette duplicati: possono esserci elementi con lo stesso valore
    
# insieme di coppie chiave valora come gli oggetti in js: chiave a sinistra valore a destra!
persona = {
    "nome": "Luca",
    "cosgnome": "rossi",
    "eta": 25   
}
print(type(persona))
# come accedere agli elementi, con .get(prendo il valore della chiave che inserisco)
print(persona.get("nome"))

# come accedere agli elementi, con .keys()prendo le chiavi
print(persona.keys())

# come accedere agli elementi, con .values()prendo i valori
print(persona.values())

# come accedere agli elementi, con .items()prendo una lista di tuple con la chiave il valore che corrisponde
print(persona.items())

# in questo modo controllo se una chiave esiste 
print("nome" in persona)
# ------------------------------------------------------------------------------------------------------

# con questo modo posso andare a cambiare il valore delle chiavi che imposto nelle quadre
persona["nome"] = "Michele"
# sono due metodi uguali quello sopra e quello sotto
# persona.update({"nome": "marco"})

# .pop(k) k sta per chiave e inserisco la chiave: valore ch evolgio eliminare. con .popitem() vado ad eliminare l'ultima chiave: valore

# per ciclare values() per cilcare i valori, keys() per le chiavi, items() per ricevere una tupla dell'item chiave: valore
for x in persona:
    print(persona[x])
    
for x, y in persona.items():
    print(x, y)
    
# dict annidati
studente = {
    "nome": "marco",
    "cognome": "zanco",
    "eta" : 25,
    "indirizzo": {
        "citta": "roma",
        "cap": "00930",
        "via": "campo dei fiori",
        "civico": 34
    }    
}
print(studente["indirizzo"]["civico"])