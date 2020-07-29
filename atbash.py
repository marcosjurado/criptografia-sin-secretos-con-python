# Cifra atbash
print('Este programa cifra o descifra un mensaje mediante la cifra Atbash')

import pyperclip

# Alfabetos empleados
CLARO = 'abcdefghijklmnopqrstuvwxyz '
CIFRADO = 'ZYXWVUTSRQPONMLKJIHGFEDCBA '

# Almacena la forma cifrada/descifrada del texto
salida = ''

# Guarda el texto introducido
texto = input('Introduce un texto: ')

# Ejecuta el cifrado/descifrado letra a letra
for simbolo in texto.lower():
    if simbolo in CLARO:
        # Identifica la posicion de cada simbolo
        indice = CLARO.index(simbolo)
        # Anade un nuevo simbolo al texto cifrado/descifrado
        salida += CIFRADO[indice]

# Imprime en pantalla el resultado
print(salida)

# Copia el mensaje al portapapeles
pyperclip.copy(salida)
