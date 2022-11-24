# Condicionales
my_condition = True

if my_condition: # Aquí, si no se indica nada, se da por hecho que es True
    print ('Se ejecuta la condición del if')

my_condition = 5 * 2

if my_condition >= 10: # Si se cumple la condición
    print ('Se cumple la condición')
else: # Si no se cumple la condición
    print ('La condición no se cumple')

print ('La ejecución continúa') # Esto está fuera del if

my_condition = 'Perro'
if my_condition == 'Perro' or 'Gato': # También se puede usar and y not
    print ('La condición se cumple')
elif my_condition == 'Gato':
    print ('Me llamo Marcos')

my_string = ''
if my_string == '':
    print ('El string está vacío')

