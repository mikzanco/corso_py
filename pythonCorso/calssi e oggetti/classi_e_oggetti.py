# classi e oggetti
# andare a creare degli stampini che si utilizzano per ricreare degli oggetti derivanti da questo stampino: lo stampino è la classe

#  Il parametro self ci aiuta a capire di che oggetto/istanza/persona in questo caso stiamo parlando. Va definito sempre come primo parametro, essendo che viene preso automaticamente poi non dobbiamo inserirlo

# COS'è UN ISTANZA? è appunto il determinato oggetto persona1 perchè è dell'istanza di Persona() 'DERIVA DA': oggetto stampato da quello stampino 

# lo stampino è la classe e l'oggetto è appunto l'oggetto che viene stampato 
class Persona:
    # creo il costruttore cioè una funzione chiamata atomaticamente
    def __init__(self, nome, cognome):

        # self è il riferimento a se stesso: all'istanza, self di persona1 fa riferimento a persona1 e self di persona2 fa riferimento a persona2

        # self.attributto/proprietà in questo caso nome e cognome sono attributi e si chiamano anche proprietà
        self.nome = nome
        self.cognome = cognome
    
    # questo è un metodo ed è trasversale su tutta la classe Persona
    def saluta(self):
        # senza self non capirebbe a chi ci riferiamo e darebbe errore.
        print("Ciao sono " + self.nome)

# persona1 e persona2 sono l'oggetto che stampo dallo stampino Persona()  
persona1 = Persona("Luca", "Rossi")
# oggetto =  di istanza Persona("parametri", "parametri")
persona2 = Persona("Marco", "Verdi")

# per eliminare un oggetto posso usare 'del' e indicare l'oggetto da elimnare, se voglio posso eliminare solo la sua proprietà e la sua proprietà da eliminare:

del persona1
del persona1.nome


print(persona1.nome)