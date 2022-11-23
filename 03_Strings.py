# Strings
my_string = 'Mi string'
print (len(my_string)) # Nos dice el largo de un string
print (my_string + ' Me llamo Marcos') # Concatenamos dos strings

my_new_line = 'Esto es otro string\npara hacer el salto de línea'
print (my_new_line)

my_string_tabulation  = ' \tEsto es una tabulación'
print (my_string_tabulation)

# Formateo
name, surname, edad = 'Marcos', 'Carmona', 47
print (f'Mi nombre es {name} {surname} y mi edad es {edad} años de edad ')

# Desempaquetado de caracteres
languaje = 'Python'
a, b, c, d, e, f = 'Python' # Hacemos una varibale por cada caracter del string
print (a)
print (b)

# División (slicing)
languaje_slice = languaje[1:3]
print (languaje_slice)

# Reverse
nombre = 'Marcos Carmona García'
print (nombre[::-1])

# Stride
nombre = 'Marcos Carmona García'
print (nombre[1:2:3])

# Métodos
print (len(nombre))
print (nombre.capitalize()) # La primera letra nos la pone en mayúsculas
print (nombre.upper()) # Nos lo pone en mayúsculas
print (nombre.count('s')) # Nos dice cuantos hay del objeto que le indiquemos
print (nombre.isnumeric()) # Nos dice si es números
print (nombre.lower()) # En minúsculas
print (nombre.isupper()) # Comprueba si está en mayúsculas
print (nombre.startswith('py')) # Preguntamos si empieza con el objeto que le indiquemos


