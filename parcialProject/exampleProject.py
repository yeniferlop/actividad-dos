# Conversión de tipos de datos
entero = 10
decimal = 10.5
cadena = "123"

# Convertir entero a decimal
entero_a_decimal = float(entero)
print(f"Entero a decimal: {entero_a_decimal}")

# Convertir decimal a entero
decimal_a_entero = int(decimal)
print(f"Decimal a entero: {decimal_a_entero}")

# Convertir cadena a entero
cadena_a_entero = int(cadena)
print(f"Cadena a entero: {cadena_a_entero}")

# Multilíneas de cadenas
multilinea = """Esta es una cadena
de múltiples líneas
en Python."""
print(multilinea)

# Función len()
longitud = len(multilinea)
print(f"Longitud de la cadena multilinea: {longitud}")

# Sub cadenas
cadena = "Hola, mundo!"

# Obtener los primeros n caracteres de una cadena
n = 5
primeros_n = cadena[:n]
print(f"Primeros {n} caracteres: {primeros_n}")

# Obtener los caracteres de en medio de una cadena
medio = cadena[len(cadena)//2 - 1:len(cadena)//2 + 1]
print(f"Caracteres de en medio: {medio}")

# Obtener los últimos n caracteres de una cadena
ultimos_n = cadena[-n:]
print(f"Últimos {n} caracteres: {ultimos_n}")

# Función upper()
mayusculas = cadena.upper()
print(f"Cadena en mayúsculas: {mayusculas}")

# Función lower()
minusculas = cadena.lower()
print(f"Cadena en minúsculas: {minusculas}")


# Función strip()
cadena_con_espacios = "   Hola, mundo!   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(f"Cadena sin espacios: '{cadena_sin_espacios}'")

# Función replace()
cadena_reemplazada = cadena.replace("mundo", "Python")
print(f"Cadena reemplazada: {cadena_reemplazada}")

# Función split()
palabras = cadena.split(", ")
print(f"Palabras separadas: {palabras}")

# Formato de cadenas F-String
nombre = "Juan"
edad = 30
f_string = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(f_string)