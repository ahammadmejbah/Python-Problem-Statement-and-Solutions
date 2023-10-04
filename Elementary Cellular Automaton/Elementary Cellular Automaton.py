import numpy as np
import matplotlib.pyplot as plt

def elementary_cellular_automaton(rule, num_generations, initial_state=None):
    if initial_state is None:
        initial_state = np.zeros(num_generations, dtype=int)
        initial_state[num_generations // 2] = 1  # Initial state with a single active cell in the middle

    rule_bin = np.array([int(bit) for bit in format(rule, '08b')])  # Convert rule to binary
    automaton = np.zeros((num_generations, len(initial_state)), dtype=int)
    automaton[0] = initial_state

    for generation in range(1, num_generations):
        for cell in range(1, len(initial_state) - 1):
            neighborhood = automaton[generation - 1, cell - 1:cell + 2]
            automaton[generation, cell] = rule_bin[np.sum(neighborhood * np.array([4, 2, 1]))]

    return automaton

# Define parameters
rule_number = 30
num_generations = 50

# Simulate and visualize the automaton
automaton = elementary_cellular_automaton(rule_number, num_generations)
plt.imshow(automaton, cmap='binary', interpolation='nearest')
plt.title(f"Elementary Cellular Automaton Rule {rule_number}")
plt.show()
