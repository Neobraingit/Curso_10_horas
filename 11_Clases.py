# Clases

class Personavacía:
    pass

print (Personavacía())

class Persona: # Declaramos la clase
    def __init__(self, nombre, apellido, alias = 'Sin alias'):
        self.nombre = nombre
        self.apellido = apellido
        self.alias = alias

    def andar(self):
        print (f'Está caminando {hombre.alias}')


hombre =  Persona('Marcos', 'Carmona') # Instanciamos un elemento de la clase Persona
print (hombre.nombre)
print (f'Tu apellido es {hombre.apellido}')
print (hombre.andar())
niño = Persona('David', 'Carmona', 'Mons') # Instanciamos un elemento de la clase Persona
print (niño.alias)
print (f'Tu nombre es {niño.nombre}')
print (f' Está caminando {niño.nombre}')
