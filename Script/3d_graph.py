import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator

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

sigma_values = np.linspace(0, 1, 25)

rho_values_f1 = np.zeros((len(sigma_values), len(c_values_1)))
rho_values_f2 = np.zeros((len(sigma_values), len(c_values_2)))

lower_bound = 0
upper_bound = 1

for i, c in enumerate(c_values_1):
    for j, s in enumerate(sigma_values):
        try:
            rho_values_f1[j, i] = brentq(f1, lower_bound, upper_bound, args=(c, s))
        except ValueError:
            rho_values_f1[j, i] = lower_bound

for i, c in enumerate(c_values_2):
    for j, s in enumerate(sigma_values):
        try:
            rho_values_f2[j, i] = brentq(f2, lower_bound, upper_bound, args=(c, s))
        except ValueError:
            rho_values_f2[j, i] = lower_bound

c_values_1 = np.log10(c_values_1)
c_values_2 = np.log10(c_values_2)

C1, S1 = np.meshgrid(c_values_1, sigma_values)
C2, S2 = np.meshgrid(c_values_2, sigma_values)

fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={"projection": "3d"}, figsize=(14, 7))

# Plot the surfaces for both functions
surf1 = ax1.plot_surface(C1, S1, rho_values_f1, cmap=cm.viridis, linewidth=0, antialiased=False)
ax1.set_title('Pass: '+ r'$f1(\rho, \sigma, c)=\left(1 - \frac{2 (1 - \sigma - \rho)}{c}\right) (1 - \sigma - \rho) - \rho$', color='b')
ax1.set_xlabel('c (log scale)', color='#00008B')
ax1.set_ylabel(r'$\sigma$', color='#00008B')
ax1.set_zlabel('Maximum value of ' + r'$\rho$', color='#00008B')
ax1.set_zlim(0, 1)
ax1.zaxis.set_major_locator(LinearLocator(10))
ax1.zaxis.set_major_formatter('{x:.02f}')
ax1.view_init(elev=20., azim=-140)

surf2 = ax2.plot_surface(C2, S2, rho_values_f2, cmap=cm.viridis, linewidth=0, antialiased=False)
ax2.set_title('Markov: ' + r'$f2(\rho, \sigma, c)=(1 - \sigma - \rho) \exp\left(-\frac{2 (1 - \sigma - \rho)}{c}\right) - \rho$', color='r')
ax2.set_xlabel('c (log scale)', color='#00008B')
ax2.set_ylabel(r'$\sigma$', color='#00008B')
ax2.set_zlabel('Maximum value of ' + r'$\rho$', color='#00008B')
ax2.set_zlim(0, 1)
ax2.zaxis.set_major_locator(LinearLocator(10))
ax2.zaxis.set_major_formatter('{x:.02f}')
ax2.view_init(elev=20., azim=-140)

xticks=[1, 2, 4, 10, 30, 60, 100]    

ax1.set_xticks(np.log10(xticks))
ax1.set_xticklabels(xticks)
ax1.tick_params(axis='x', rotation=-35)

ax2.set_xticks(np.log10(xticks))
ax2.set_xticklabels(xticks)
ax2.tick_params(axis='x', rotation=-35)

# Combine the data for a single color mapping
combined_rho_values = np.concatenate((rho_values_f1.flatten(), rho_values_f2.flatten()))
vmin, vmax = combined_rho_values.min(), combined_rho_values.max()

# Create a single horizontal colorbar
fig.subplots_adjust(bottom=0.1)
cbar_ax = fig.add_axes([0.2, 0.05, 0.6, 0.03])
mappable = cm.ScalarMappable(cmap=cm.viridis)
mappable.set_array(combined_rho_values)
mappable.set_clim(vmin, vmax)
fig.colorbar(mappable, cax=cbar_ax, orientation='horizontal')

plt.show()
