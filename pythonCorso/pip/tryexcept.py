#  26 Try Except

# gli dico: prova  afarmi questo print
try:
    print(x)
except:
    # se non funziona try usa except, usando pass posso non passare niente a schermo
    print("c'è stato un errore")
else: #se va tutto bene mi stampi il try e quello che viene nell'else, ma non nell'except.
    print("nessun problmea")
finally: #con finally stampo quaclosa in ogni caso: che sia andato tutto bene il try o che ci sia stato l'errore e quindi except
    print("finally")