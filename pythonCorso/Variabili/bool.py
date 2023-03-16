# valori Boolean


x = True
y = False

# x = true non me lo prende e mi da errore perchè la prima lettera deve essere maiuscola

if 5 < 10:
    print("sono MINORE di 10")
else:
    print("sono MAGGIORE di 10")
# questo è l'utilizzo delle varibili e mi restituirà "sono MINORE di 10" che è il punto in cui l'if risulta True

print(bool(1))

# ritorna true
# mentre fosse 0 sarebbe false

pane = 0
if pane:
    print("non serve andare a prendere il prane ")
else: 
    print("uscire a prendere il pane")
# pane 0 didica che non c'è pane e quindi l'if sarebbe false e passa all'else e mi dirà quindi "uscire a prendere il pane"