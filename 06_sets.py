# Sets
my_set = {'Perro', 'Gato', 'Caballo', 'Cochino'}
print (type(my_set)) # Sabemos de qué tipo es el dato que hemos creado
print (len(my_set)) # Nos dice cuantos elementos hay en el set
print (my_set.add('Serpiente')) # Añadimos un elemento al set
print (my_set)
'''Un set no es una estructura ordenada'''
'''Un set no admite elementos repetidos'''
print ('Gato' in my_set) # Nos dará un valor booleano
print (my_set.remove('Gato')) # Borramos un elemento
print (my_set)
print (my_set.clear()) # Vacía el set
print (my_set)
my_other_set = {1, 2, 3, 4}
del my_set # Borramos el set completamente



