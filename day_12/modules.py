# Write a function which generates a six digit/character random_user_id

import random
import string

def generar_id_usuario_aleatorio():
    # Combinar letras y números para formar el ID
    caracteres = string.ascii_letters + string.digits
    # Generar un ID aleatorio de 6 caracteres
    id_usuario_aleatorio = ''.join(random.choices(caracteres, k=6))
    return id_usuario_aleatorio

# Ejemplo de uso
id_generado = generar_id_usuario_aleatorio()
print(f"El ID de usuario generado es: {id_generado}")


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    # Pedir al usuario el número de caracteres por ID
    num_caracteres = int(input("Introduce el número de caracteres por ID: "))
    # Pedir al usuario el número de IDs que se deben generar
    num_ids = int(input("Introduce el número de IDs que deseas generar: "))
    
    # Generar los IDs
    ids_generados = []
    caracteres = string.ascii_letters + string.digits  # Letras y números
    for _ in range(num_ids):
        id_usuario = ''.join(random.choices(caracteres, k=num_caracteres))
        ids_generados.append(id_usuario)
    
    # Devolver la lista de IDs generados
    return '\n'.join(ids_generados)

# Ejemplo de uso
print(user_id_gen_by_user())

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    # Generar tres valores aleatorios entre 0 y 255
    rojo = random.randint(0, 255)
    verde = random.randint(0, 255)
    azul = random.randint(0, 255)
    # Retornar el color RGB en formato texto
    return f"RGB({rojo}, {verde}, {azul})"

# Ejemplo de uso
print(rgb_color_gen())
