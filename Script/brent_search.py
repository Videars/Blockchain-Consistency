import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from matplotlib.widgets import Slider

def f1(x, c, s):
    return (1 - (2 * (1 - s - x)) / c) * (1 - s - x) - x

def f2(x, c, s):
    return (1 - s - x) * np.exp(-(2 * (1 - s - x)) / c) - x

c_values_between_0_and_2 = np.linspace(0.1, 1.9, 10)
c_values_between_2_and_3 = np.linspace(2, 3, 7)
c_values_between_3_and_4 = np.linspace(3.2, 4, 4)
c_values_above_4 = np.random.exponential(scale=20, size=10) + 4
c_values_specific = np.array([10, 20, 60, 100])
c_values_1 = np.unique(np.concatenate([c_values_between_2_and_3, c_values_between_3_and_4, c_values_above_4, c_values_specific]))
c_values_2 = np.unique(np.concatenate([c_values_between_0_and_2, c_values_1]))
c_values_1.sort()
c_values_2.sort()

lower_bound = 0
upper_bound = 1

def update(val):
    s = slider_s.val
    x_max_values_f1 = []
    x_max_values_f2 = []

    for c in c_values_1:
        try:
            max_x_f1 = brentq(f1, lower_bound, upper_bound, args=(c, s))
            x_max_values_f1.append(max_x_f1)
        except ValueError:
            x_max_values_f1.append(lower_bound)

    for c in c_values_2:
        try:
            max_x_f2 = brentq(f2, lower_bound, upper_bound, args=(c, s))
            x_max_values_f2.append(max_x_f2)
        except ValueError:
            x_max_values_f2.append(lower_bound)

    ax.clear()
    ax.plot(c_values_1, x_max_values_f1, marker='o', markersize=2, linestyle='-', linewidth=0.2, color='b', label='Pass')
    ax.plot(c_values_2, x_max_values_f2, marker='o', markersize=2, linestyle='-', linewidth=0.2, color='r', label='Markov')

    ax.set_xscale('log')
    ax.set_xlabel('c values (logarithmic scale)')
    ax.set_ylabel('Maximum value of ' + r'$\rho$')
    ax.set_title('Maximum value of '+r'$\rho$'+' for which consistency still holds')
    ax.grid(True, which='both', linestyle='--', linewidth=0.2)
    ax.set_xticks([1, 2, 4, 10, 30, 60, 100])
    ax.set_xticklabels([1, 2, 4, 10, 30, 60, 100])
    ax.legend()

    plt.draw()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.35)

ax_slider_s = plt.axes([0.25, 0.05, 0.5, 0.03])
slider_s = Slider(ax_slider_s, r'$\sigma$', 0, 1, valinit=0, valstep=0.01)

update(0)

slider_s.on_changed(update)

plt.figtext(0.5, 0.18, r'$f1(\rho, c, \sigma) = \left(1 - \frac{2 (1 - \sigma - \rho)}{c}\right) (1 - \sigma - \rho) - \rho$', ha='center', color='blue', fontsize=10)
plt.figtext(0.5, 0.12, r'$f2(\rho, c, \sigma) = (1 - \sigma - \rho) e^{-\frac{2 (1 - \sigma - \rho)}{c}} - \rho$', ha='center', color='red', fontsize=10)

plt.show()
