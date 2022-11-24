# Bucles
'''Los bucles nos sirven para iterar y pasar por el mismo código varias veces'''

# While

my_bucle = 10
while my_bucle == 10:
    print ('Se cumple la condición')
    my_bucle += +1
else:
    print (my_bucle)

# For

my_string = input('Introduce una frase: ') # Iteramos un string
for i in my_string:
    print (i)

my_list = ['Perro', 'Gato', 'Caballo', 'Cebra'] # Iteramos una lista
for i in my_list:
    print (i)

my_set = {'Marcos', 'David', 'Eva', 'Marta'} # Iteramos un set
for i in my_set:
    print (i)

my_dict = {'Nombre' : 'Marcos', 'Apellido' : 'Carmona'} # Iteramos un diccionario
for i in my_dict.values():
    print (i)






