# EREDITARIETà

# concetto per cui una classe figlia che ha una classe madre da cui deriva eredita tutto quello che ha la classe madre e può avere altre cose in più.


class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono ' + self.nome)

# la classse Insegannte estente e deriva dalla classe Persona
class Insegnante(Persona):
    #pass #con pass posso poi non mettere niente
    def __init__(self, nome, cognome, materia):
        # con super 'sopra' facciamo la derivazione da chi sta sopra:
        super().__init__(nome, cognome) 
        # non posso mettere sopra materia perchè non è una cosa che eredita e quindi creo un altro self
        self.materia = materia
    def saluta(self):
        print("Buongiorno sono " + self.nome + " " + self.cognome)
        

persona1 = Persona("Luca", "Rossi")
insegnante1 = Insegnante("Anna", "Neri", "Matematica")
# insegnante1.saluta() funzionerà perchp insegnante eredita da persona saluta e quindi la utilizza
insegnante1.saluta()
print(insegnante1.materia)

