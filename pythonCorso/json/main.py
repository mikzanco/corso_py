#  ci serve se vogliamo collegare python a qualcosa di front-end, con js posso inviare le cose con ajax


# come leggere JSON in python
# impotiamo json che è una stringa
import json

x = '{"nome": "Luca", "cognome": "Rossi", "eta": 25}'

y = json.loads(x)
# per legger eun json serve loads
print(y["nome"])

# come passare da python a json
d = {
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25
}

# lo creo sotto forma di dict e poi vado a creare un json

p = json.dumps(d)
# e mi crea una stringa
print(p)

# come formattare un json
f = {
    "nome": "Luca", 
    "cognome": "Rossi", 
    "eta": 25,
    "isOnline": False,
    "interessi": ["calcio", "basket"],
    "moneteInTasca": 4.35,
    "fidanzata": None
}

# con indent=4 possiamo formattare e farlo diventare su più righe anzichè su una riga sola, per formattarlo in ordine alfabetico e renderlo ancora più leggibile usiamo sort_keys=True
e = json.dumps(f, indent=4, sort_keys=True)

print(e)