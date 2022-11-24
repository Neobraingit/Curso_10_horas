# Diccionarios
my_dict = {'Animal' : 'Gato', 'Persona' : 'Marcos', 'Cosa' : 'Toyota'}
print (type(my_dict))
my_other_dict = {'Peso' : 95, 'Color' : 'Rojo', 'Edades' : {47, 45, 34}} # Añadimos como valor un set
print (my_other_dict)
print (len(my_dict))
print (my_other_dict['Peso']) # Accedemos al valor de la clave dada
my_other_dict['Peso'] = 'Juan' # Cambiamos el valor de la clave Peso
print (my_other_dict['Peso'])
my_other_dict['Calle']  = 'Avnda La Argentina' # Añadimos un nuevo par clave:valor
print (my_other_dict)
del my_other_dict['Calle'] # Borramos un par clave:valor
print (my_other_dict)
print ('Juan' in my_other_dict) # Accedemos al valor booleano aunque dará False por estar buscando por el valor
print ('Color' in my_other_dict) # Aquí nos dará True por estar buscando por clave
print (my_other_dict.items)
print (my_other_dict.keys()) # Nos retorna las claves
print (my_other_dict.values()) # Nos retorna todos los valores
print (my_other_dict.fromkeys('Peso')) # Hay que pasarle valores
