# Excepciones

numberOne = 5
numberTwo = 1

numberTwo = '1'

# Try except

try:
    print (numberOne + numberTwo)
    print ('No se ha producido error')
except:
    print ('Se ha producido un error')

# Try except else

try:
    print (numberOne + numberTwo)
    print ('No se ha producido error')
except:
    # Se ejecuta si se produce una excepción
    print ('Se ha producido un error')
else:
    # Se ejecuta si no se produce una excepción
    print ('La ejecución continúa correctamente')
finally:
    # Se ejecuta pase lo que pase
    print ('La ejecución continúa')

# Captura de excepciones por tipo

try:
    print (numberOne + numberTwo)
    print ('No se ha producido error')
except TypeError:
    # Solo se ejecuta si se da el TypeError
    # Se ejecuta si se produce una excepción
    print ('Se ha producido un error')


