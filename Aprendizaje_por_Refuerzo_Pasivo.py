import random

# Definir el entorno
num_states = 2
num_actions = 2

# Definir la matriz de recompensas
# En este ejemplo, utilizamos una matriz de recompensas simple
rewards = [
    [1, 0],
    [0, 1]
]

# Definir la política del experto
# En este ejemplo, el experto toma acciones aleatorias
def expert_policy(state):
    return random.randint(0, num_actions - 1)

# Parámetros de aprendizaje
learning_rate = 0.1
discount_factor = 0.9

# Aprendizaje por refuerzo pasivo
num_episodes = 1000
state = 0  # Estado inicial

for episode in range(num_episodes):
    action = expert_policy(state)  # El agente sigue la política del experto
    next_state = random.randint(0, num_states - 1)  # El entorno cambia aleatoriamente
    reward = rewards[state][action]
    
    # Actualizar la política del agente (aprendizaje pasivo)
    # En este ejemplo, el agente no aprende, pero puedes implementar una actualización si lo deseas.
    
    # Mostrar información sobre el episodio
    print(f"Episodio {episode}: Estado={state}, Accion={action}, Recompensa={reward}, Proximo Estado={next_state}")
    
    state = next_state  # Actualizar el estado

print("Aprendizaje por Refuerzo Pasivo completado.")

