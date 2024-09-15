import numpy as np
import math
import matplotlib.pyplot as plt

# Function to clear memoization dictionaries
def clear_memo():
    global memo_P, memo_Delta
    memo_P = {}
    memo_Delta = {}

# Function to calculate Delta
def calculate_Delta(k, s):
    if (k, s) in memo_Delta:
        return memo_Delta[(k, s)]
    
    if s - 1 >= k:
        result = 1
    elif s == -1:
        result = 0
    else:
        result = union * calculate_P(k-1, s) + h_delta * calculate_Delta(k-1, s-1) + delta_silent * calculate_P(k-1, s-1)
    
    memo_Delta[(k, s)] = result
    return result

# Function to calculate P
def calculate_P(k, s):
    if (k, s) in memo_P:
        return memo_P[(k, s)]
    
    if s >= k:
        result = 1
    elif s == -1:
        result = 0
    else:
        delta_state = calculate_Delta(k, s)
        result = h * delta_state + a * calculate_P(k, s + 1)
    
    memo_P[(k, s)] = result
    return result

# Initialize parameters for multiple c and a values
c_values = [1, 4, 60]
sleepy_fraction = 0.1
corrupts = [0.25, 0.40]
k_values = np.arange(2, 16, 2)

# Plotting the solutions for P(k, 0)
color_map = {1: 'purple', 4: 'orange', 60: 'green'}
plt.figure(figsize=(10, 6))

for corrupt in corrupts:
    if corrupt == 0.25:
        line_style = '--'
        adv_label = "25% Adv"
    else:
        line_style = '-'
        adv_label = "40% Adv"
    
    for c in c_values:
        # Global parameters
        corrupt_fraction = corrupt
        honest_fraction = 1 - sleepy_fraction - corrupt_fraction
        h = honest_fraction
        a = corrupt_fraction

        delta_silent = math.exp(-1/c)

        h_delta = 1 - math.exp(-(honest_fraction/2) / c)
        a_delta = 1 - math.exp(-corrupt_fraction / c)

        union = 1 - math.exp(-(corrupt_fraction + (honest_fraction/2)) / c)

        # Clear previous memoization
        clear_memo()

        # Calculate P_0(k) for each k
        results = []
        for k in k_values:
            result = calculate_P(k, 0)
            results.append(result)

        # Plot the results
        plt.plot(k_values, results, line_style, label=f'{adv_label}' if c == c_values[0] else "", color=color_map[c])


# Adding legend with both attacker percentages and c values
from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], color='black', lw=2, linestyle='-', label='40% Adv'),
    Line2D([0], [0], color='black', lw=2, linestyle='--', label='25% Adv'),
    Line2D([0], [0], color='purple', lw=2, linestyle='-', label='c=1'),
    Line2D([0], [0], color='orange', lw=2, linestyle='-', label='c=4'),
    Line2D([0], [0], color='green', lw=2, linestyle='-', label='c=60')
]

plt.legend(handles=custom_lines, loc='best')

plt.xlabel(r'$k$')
plt.ylabel(r'$P_0(k)$')
plt.yscale('log')
plt.title('Probability of winning the fork sustain attack game')
plt.grid(True)
plt.show()


# Section for determining T-consistency (k for P(k, 0) < P_max)
# Define the maximum acceptable probability for T-consistency
P_max = 1e-6  # Maximum acceptable probability

# Initialize a dictionary to store the calculated k values for T-consistency
T_values = {}

# Find the k needed to reach the T-consistency for each configuration of c and a
for corrupt in corrupts:
    for c in c_values:
        # Global parameters
        corrupt_fraction = corrupt
        honest_fraction = 1 - sleepy_fraction - corrupt_fraction
        h = honest_fraction
        a = corrupt_fraction

        delta_silent = math.exp(-1/c)

        h_delta = 1 - math.exp(-(honest_fraction/2) / c)
        a_delta = 1 - math.exp(-corrupt_fraction / c)

        union = 1 - math.exp(-(corrupt_fraction + (honest_fraction/2)) / c)

        # Clear memoization
        clear_memo()

        # Calculate P_0(k) for increasing k until P(k, 0) < P_max
        T_found = False
        k = 2
        while not T_found:
            result = calculate_P(k, 0)
            if result < P_max:
                T_values[(corrupt, c)] = k
                T_found = True
            k += 1

# Print the calculated T-consistency values (k)
print("Calculated T-consistency (k for P(k, 0) < P_max):")
for (corrupt, c), T in T_values.items():
    print(f"For a = {corrupt}, c = {c}: T = {T}")
