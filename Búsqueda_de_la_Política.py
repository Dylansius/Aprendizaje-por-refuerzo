# Definir el entorno como una cuadrícula
grid = [
    [0, 0, 0, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 1]  # El 1 representa el estado objetivo
]

# Tamaño de la cuadrícula
rows = len(grid)
cols = len(grid[0])

# Inicializar la política aleatoriamente
policy = [["" for _ in range(cols)] for _ in range(rows)]

# Parámetro de descuento
gamma = 0.9

# Realizar la búsqueda de política iterativamente
num_iterations = 100
for _ in range(num_iterations):
    policy_stable = True  # Verificar si la política se ha vuelto estable

    # Crear una función de utilidad para almacenar los valores
    utility = [[0 for _ in range(cols)] for _ in range(rows)]

    # Para cada estado en la cuadrícula
    for x in range(rows):
        for y in range(cols):
            state = (x, y)
            if grid[x][y] == 1:  # Estado objetivo
                continue

            # Acciones posibles (arriba, abajo, izquierda, derecha)
            actions = ["up", "down", "left", "right"]
            action_values = []

            # Calcular el valor de las acciones
            for action in actions:
                if action == "up":
                    next_x, next_y = x - 1, y
                elif action == "down":
                    next_x, next_y = x + 1, y
                elif action == "left":
                    next_x, next_y = x, y - 1
                elif action == "right":
                    next_x, next_y = x, y + 1

                # Verificar si la acción es válida (dentro de la cuadrícula)
                if 0 <= next_x < rows and 0 <= next_y < cols:
                    action_value = grid[next_x][next_y] + gamma * utility[next_x][next_y]
                    action_values.append(action_value)

            if action_values:  # Verificar si hay valores de acciones
                # Elegir la acción con el mayor valor
                best_action_index = action_values.index(max(action_values))
                best_action = actions[best_action_index]

                # Actualizar la política si la mejor acción es diferente de la política actual
                if policy[x][y] != best_action:
                    policy_stable = False
                    policy[x][y] = best_action

    # Si la política es estable, salimos temprano
    if policy_stable:
        break

# Mostrar la política óptima
for row in policy:
    print(" ".join(row))
