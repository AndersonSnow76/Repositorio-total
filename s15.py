# Crear un Diccionario
# Se crea un diccionario llamado informacion_personal con datos ficticios.
informacion_personal = {
    "nombre": "Ana López",
    "edad": 35,
    "ciudad": "Madrid",
    "profesion": "Ingeniera de Software"
}

print(f"Diccionario Inicial: {informacion_personal}")

# ---

# Acceder y Modificar Valores

# Acceder al valor de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"La ciudad actual es: {ciudad_actual}")

# Modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"
print(f"La ciudad ha sido modificada a: {informacion_personal['ciudad']}")

# La clave "profesion" ya existe, por lo que no es necesario agregarla
# en un paso separado si ya se creó en el diccionario inicial.
# Si la hubiéramos omitido, el código para agregarla sería:
# informacion_personal["profesion"] = "Ingeniera de Software"
# Pero como ya está, este paso se omite o se interpreta como la inicialización.
# Dejaremos la clave como está para seguir con los siguientes pasos.

# ---

# Verificar Existencia de Claves

# Verificar si la clave "telefono" existe en el diccionario.
if "telefono" not in informacion_personal:
    # Si no existe, se agrega con un número de teléfono ficticio.
    informacion_personal["telefono"] = "0982033141"
    print("La clave 'telefono' no existía y ha sido agregada.")
else:
    print("La clave 'telefono' ya existe.")

# ---

# Eliminar una Clave

# Eliminar la clave "edad" del diccionario usando pop().
# Usamos pop() para también obtener el valor que se elimina (opcional).
edad_eliminada = informacion_personal.pop("edad")
print(f"Se ha eliminado la clave 'edad' (Valor: {edad_eliminada}).")

# ---

# Imprimir el Diccionario Final

# Imprimir el diccionario resultante después de todas las operaciones.
print("\n---")
print("Diccionario Final con la información personal actualizada:")
print(informacion_personal)
