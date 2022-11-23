# Variables
''' Hay que intentar declararlas en minúsculas'''

mi_variable = 'My variable string'
print (mi_variable)

mi_intvariable = 123
print (f'Esto es una variable numérica, {mi_intvariable}')

mi_boolvariable = False
print (f'Esto es una variable de tipo booleana: {mi_boolvariable}')

print (f'Print puede llevar varios argumentos: {mi_variable} {mi_intvariable} {mi_boolvariable}')

print (f'Convertimos un entero en string:',str(mi_intvariable))

# Concatenación de variables
print (mi_variable + mi_variable)

# Saber la longitud de una variable
print (len(mi_variable))

#  Declaración de múltiples variables en una sola línea
variable_1, variable_2 = 'Perro', 'Gato'
print (variable_2)
print (variable_1)

# Input nos pedirá introducir datos
variable_input = input('Introduce un dato: ')
print (variable_input)


