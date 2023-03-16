# Stringhe

# le stringhe multiriga si fanno con tripli apici """prova""" 

# gli array --------------------------

x = "prova numero uno"

print(x[7])
# mi ritornerà la u perchè è posizionata al INDICE 7 e via cosi e lo spazio viene comunque contato
print(len(x))
# in questo caso mi va a prendere la lunghezza della stringa x tenendo conto anche degli spazi e risulta 16

# questo è il loop della stringa
for carattere in x:
    print(carattere)
    
    
# posso andare a prendere parti di stringa

z = "ciao sono io"

print(x[:2])
# mi prendere tutte le lettere o parti della stringa fino all'indice 2
print(x[4:])
# mi prendere tutte le lettere o parti della stringa dopo l'indice 4
print(x[2:8])
# mi prendere tutte le lettere o parti della stringa in un range compreso nel range di indici 2 e 8
print(x[-4:])
# si parte dal indice che è quartultimo e mi prendere le ultime 4 lettere della stringa


# PER MODIFICARE UNA STRINGA SI UTILIZZANO 

print(x.upper())
print(x.lower())
print(x.strip())
print(x.split())
print(x.replace("o", "x"))


# CON FORMAT POSSO FARE DELLE CONCATENAZIONI PARTICOLARI:

x = 23
prova = "Ciao sono Luca e sono nato il {}"

print(prova.format(x)) 
# mi restituisce la stringa 'Ciao sono Luca e sono nato il 19' mettendo il 19 del format nelle parentesi graffe {}

# gli escape dei caratteri si fa con il \:
x = "sono io che \"faccio\" la polenta "
