import random

# Parámetros
volumen_maximo = 500  # Volumen máximo de vehículos por hora
capacidad_via = 400   # Capacidad de la vía en vehículos por hora
simulaciones = 15000  # Número de simulaciones

# Contador para las veces que el volumen de tráfico excede la capacidad de la vía
excesos = 0

# Simulación
for _ in range(simulaciones):
    volumen_aleatorio = random.randint(0, volumen_maximo)  # Genera un volumen aleatorio
    if volumen_aleatorio > capacidad_via:
        excesos += 1

# Probabilidad de exceso de capacidad
probabilidad_exceso = excesos / simulaciones

print(probabilidad_exceso)
