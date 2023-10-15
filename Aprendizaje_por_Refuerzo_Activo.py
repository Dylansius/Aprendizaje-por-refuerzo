import random

# Definir un entorno sencillo con dos estados y dos acciones posibles.
# El objetivo es que el agente aprenda la política óptima mediante interacciones con el entorno.

# Definir las recompensas en el entorno.
rewards = [-1, 1]

# Hiperparámetro de exploración (probabilidad de explorar en lugar de explotar).
epsilon = 0.2

# Función de valor inicializada aleatoriamente.
Q = [0, 0]

# Parámetro de descuento.
gamma = 0.9

# Número de episodios de aprendizaje.
num_episodes = 1000

for episode in range(num_episodes):
    state = 0  # Estado inicial
    while True:
        # Selección de acción (exploración vs. explotación)
        if random.random() < epsilon:
            action = random.choice([0, 1])
        else:
            action = Q.index(max(Q))
        
        # Interacción con el entorno y obtención de recompensa
        next_state = action
        reward = rewards[next_state]
        
        # Actualización de la función de valor Q
        Q[state] += 0.1 * (reward + gamma * max(Q) - Q[state])
        
        state = next_state
        
        if state == 1:  # Estado objetivo
            break

print("Funcion de valor Q aprendida:")
print(Q)

