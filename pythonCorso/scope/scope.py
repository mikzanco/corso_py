# scope

# scope è la disponibilità di una variabile nel nostro codice, noi abbiamo variabili in delle funzioni e variabili fuori.
# scope indica la regione in cui la varbaile che ci interessa è disponibile.

# lo scope può essere locale o globale

# scope locale e quidi dentro a una funzione:

def funzione():
    x = 400

    return x

x = funzione()
print(x)
# print(x) non funziona se non metto un return che mi permette di lavorarci anche fuori. a quel punto segno x = funzione() e cosi avrò portato furoi la varibile x = 400 dalla funzione

# vado adesso a creare y una variabile globale: se scritte al di fuori di una funzioen saranno globali.

y = 300

def funzione():
    print(y)

funzione()

# la keyword globale seve per lavorare con variabili globali dentro a funzioni:

z = 500

def function():
    global z
    z = 100
    print(z)

function()
print(z)
