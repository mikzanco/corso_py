# Lavorare con i file
# - introduzione al file handling (gestione)
    # r - Read: apre il file per leggere, errore se non esiste
    # a - Append: apre il file per appendere. crea il file se non esiste
    # w - Write: apre il file per scrivere, crea il file se non esiste
    # x - Create: crea il file, errore se esiste
# - aprire un file 
# - leggere un file: intero o una parte
# - scrivere in un file 
# - creare un file 
# - eliminare file (check) e eliminare cartella

f = open("testo.txt")
print(f.read())