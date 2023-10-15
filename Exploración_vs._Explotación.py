import random

# Hiperparámetro ? (probabilidad de exploración).
epsilon = 0.2

# Función de valor de acciones (en este caso, valores arbitrarios).
action_values = [0.2, 0.5, 0.8, 0.1]

def choose_action():
    if random.random() < epsilon:
        # Exploración: selección aleatoria de una acción.
        return random.choice(range(len(action_values)))
    else:
        # Explotación: selección de la acción con el valor más alto.
        return action_values.index(max(action_values))

# Ejemplo de uso:
action = choose_action()
print("Accion seleccionada:", action)

