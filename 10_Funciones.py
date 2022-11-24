# Funciones

def mi_funcion(): # Declaramos la función
    print ('Esta es mi función')

mi_funcion() # Ejecutamos la función


def mi_funcion2(num1, num2): # Declaramos la función con parámetros
    print (num1 + num2)

mi_funcion2(3, 5) # Ejecutamos la función con los parámetros requeridos

def mi_funcion3(num1, num2):

    return num1 + num2 # Esto no devuelve nada si no lo guardamos en una variable

resultado = mi_funcion3(4, 5)
print (resultado)

def print_text(*text):
    print (text)

print_text('Marcos', 'Carmona', 'García') # Podemos pasar varios parámetros por el asterisco

