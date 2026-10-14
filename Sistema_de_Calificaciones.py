# 1. Definición inicial del vector con 5 calificaciones
calificaciones = [85, 67, 92, 74, 58]

print("=========================================")
print("     SISTEMA AVANZADO DE CALIFICACIONES    ")
print("=========================================")

# 2. Mostrar todas las calificaciones utilizando un ciclo
print("\n1. Listado inicial de calificaciones:")
for i, nota in enumerate(calificaciones):
    print(f"   Estudiante {i + 1} (Índice {i}): {nota}")

# 3. Mostrar una calificación determinada utilizando su índice
indice_buscado = 2
print(f"\n2. Calificación consultada en el índice [{indice_buscado}]: {calificaciones[indice_buscado]}")

# 4. Operaciones de cálculo (Promedio, Máxima y Mínima)
suma_total = sum(calificaciones)
cantidad = len(calificaciones)
promedio = suma_total / cantidad
calificacion_alta = max(calificaciones)
calificacion_baja = min(calificaciones)

print(f"\n3. Estadísticas generales:")
print(f"   - Promedio del grupo: {promedio:.2f}")
print(f"   - Calificación más alta: {calificacion_alta}")
print(f"   - Calificación más baja: {calificacion_baja}")

# 5. Contar aprobados y reprobados usando condiciones 'if'
aprobados = 0
reprobados = 0

for nota in calificaciones:
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

print(f"\n4. Conteo de rendimiento (Nota mínima aprobatoria: 70):")
print(f"   - Estudiantes aprobados: {aprobados}")
print(f"   - Estudiantes reprobados: {reprobados}")

# 6. Modificar una calificación utilizando su índice
indice_a_modificar = 4
nueva_nota = 78
print(f"\n5. Modificando la calificación del índice [{indice_a_modificar}] (era {calificaciones[indice_a_modificar]})...")
calificaciones[indice_a_modificar] = nueva_nota

# 7. Mostrar nuevamente el vector actualizado y recalcular
print("\n=========================================")
print("       VECTOR Y ESTADÍSTICAS ACTUALIZADAS ")
print("=========================================")
print("Nuevas calificaciones:", calificaciones)

# Recalcular aprobados y promedio tras la modificación
nuevo_promedio = sum(calificaciones) / len(calificaciones)
print(f"Nuevo promedio del grupo: {nuevo_promedio:.2f}")