# LE FUNZIONI

# i parametri in questo cado è tipo_pasta
# l'argometo lo inserisoc qunado il programma sta andando e in queesto esempio è fusilli 

def fai_la_pasta(tipo_pasta, metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if metti_sugo:
        print("prepara sugo")
    
fai_la_pasta("fusilli", True)


def fai_somma(num1, num2):
    somma = num1 + num2
    return somma
x = fai_somma(2, 2)
print(x)


