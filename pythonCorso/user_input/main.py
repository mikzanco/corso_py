#  26 User Input

# creiamo un dict:
persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25
}

# andiamo a fare delle operazion che salviamo in una tupla e quindi con le parentesi ()
operazioni = ("aggiungere", "modificare", "eliminare")

# per far partire il nostro programma lo facciamo partire da def start
def start():
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]: #lo andimao a prendere da operazioni sopra e con 0 prendiamo aggiungere.
        x = input("Aggiungi chiave:valore separati da una virgola:  ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        pass
    elif operazione == operazioni[2]:
        pass

def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

while True:
    start()
