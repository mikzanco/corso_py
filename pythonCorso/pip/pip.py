# pip è un packet manager: funzionalità extra che andimo ad installare ed eliminare, è un gestore di pacchetti

import camelcase

c = camelcase.CamelCase()
frase = "ciao sono edo"
# mi metterà tutte le lettere iniziali in maiuscolo
print(c.hump(frase))

# 'pip list' per vedere i pacchetti installati.